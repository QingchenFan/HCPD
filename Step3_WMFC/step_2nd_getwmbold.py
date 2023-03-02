import nibabel as nib
import os
import numpy as np
from nilearn import image
from nilearn.image import smooth_img
from scipy.io import savemat
subpath = '/home/cuizaixu_lab/fanqingchen/DATA_C/data/HCPD/HCPD_BIDS/derivatives/fmriprep'
subid = os.listdir(subpath)

#subid = ['sub-HCD0001305', 'sub-HCD0008117', 'sub-HCD0021614']
for i in subid:
    #  对分割出的标准空间下的白质进行重采样，到全脑BOLD数据的大小、分辨率
    reslist = []
    print('participant-', i, 'start...')
    wmlabelpath = '/home/cuizaixu_lab/fanqingchen/DATA_C/data/HCPD/wmdata/resampleWM/'+i+'_space-MNI152NLin6Asym_label-WM_probseg.nii.gz'  #  这个分割出的白质数据，为了制作mask
    wmlabeldata = nib.load(wmlabelpath)
    wmmask = wmlabeldata.get_data()
    wmmask[wmmask >= 0.6] = 1.0
    wmmask[wmmask < 0.6] = 0.0
    nib.Nifti1Image(wmmask, wmlabeldata.affine, wmlabeldata.header).to_filename('/home/cuizaixu_lab/fanqingchen/DATA_C/data/HCPD/wmdata/wmmask/'+i+'_wmmask.nii.gz')
    print('WM mask done!')
    #  通过得到的白质mask,提取白质的BOLD信号
    BOLDdatapath = '/home/cuizaixu_lab/fanqingchen/DATA_C/data/HCPD/HCPD_xcpd/derivatives/xcp_abcd/'+i+'/func/'+i+'_task-rest_space-MNI152NLin6Asym_desc-residual_smooth_bold.nii.gz'
    BOLDdata = smooth_img(BOLDdatapath, fwhm=0)  # 91x109x91x478 1*1*1
    print('Bolddatashape-', BOLDdata.shape[3])
    for j in range(0, BOLDdata.shape[3]):
        res = wmmask * image.index_img(BOLDdata, j).get_data()
        reslist.append(res)
    wmBold = np.array(reslist).transpose(1, 2, 3, 0)  # 不改变维度，图像会发生旋转，所以这里transpose一下
    print(i, '-wmBold-', wmBold.shape)
    nib.Nifti1Image(wmBold, BOLDdata.affine, BOLDdata.header).to_filename('/home/cuizaixu_lab/fanqingchen/DATA_C/data/HCPD/wmdata/wmBold/'+i+'_task-rest_space-MNI152NLin6Asym_desc-residual_smooth_WMbold.nii.gz')

    WMBoldpath = '/home/cuizaixu_lab/fanqingchen/DATA_C/data/HCPD/wmdata/wmBold/'+i+'_task-rest_space-MNI152NLin6Asym_desc-residual_smooth_WMbold.nii.gz'
    WMBoldData = nib.load(WMBoldpath).get_data()
    WMBoldData = WMBoldData.transpose(3, 0, 1, 2)
    print('WMBoldData.shape-', WMBoldData.shape)
    WMBoldParr = np.reshape(WMBoldData, (478, 91 * 109 * 91))

    JHU_ICBMPath = '/home/cuizaixu_lab/fanqingchen/DATA_C/data/HCPD/wmdata/wmAtlas/rICBM_DTI_81_WMPM_60p_FMRIB58_resample.nii.gz'
    JHU_ICBMData = nib.load(JHU_ICBMPath)
    JHU_ICBMParr = JHU_ICBMData.get_data()
    JHU_ICBMParr = np.reshape(JHU_ICBMParr, (1, 91 * 109 * 91))
    roilist = []
    for r in range(1, 69):
        index = np.where(JHU_ICBMParr == r)
        roi = WMBoldParr[:, index[1]]  # ROI内所有的voxel
        totalvoxel = roi.shape[1]
        print('totalvoxel-1:', totalvoxel)
        count = 0
        for j in range(0, roi.shape[1]):  # 遍历每一个体素，roi.shape[1] = 体素个数
            if ~np.any(roi[:, j]):
                totalvoxel = totalvoxel - 1
                count = count + 1
        sum = np.sum(roi, axis=1)
        print('sum.shape-', sum.shape)
        print('totalvoxel-2:', totalvoxel)
        print('count-', count)
        roiBoldsum = sum / totalvoxel
        print('roiBoldsum.shape-', roiBoldsum.shape)
        roilist.append(roiBoldsum)
    print('roilist-len', len(roilist))
    roiMatrix = np.array(roilist)
    print('--roiMatrix--', roiMatrix.shape)
    resFC = np.corrcoef(roiMatrix)  # rowvar=False 列与列算相关；rowvar=False 行与行算相关
    savemat('/home/cuizaixu_lab/fanqingchen/DATA_C/data/HCPD/wmdata/wmFC/'+i+'_FC.mat', {'data': resFC})






