import nibabel as nib
import numpy as np
from scipy.io import savemat
# path = '/Users/fan/Documents/Data/HCPData/HCPDtest/sub-HCD0021614_task-rest_space-MNI152NLin2009cAsym_desc-residual_smooth_bold.nii.gz'
# data = nib.load(path)
# datanp = data.get_data()
# # print(datanp.shape)
# # print(datanp[:, :, :, 0].shape)
# matrix1 = datanp[:, :, :, 50]
#
# import nibabel as nib
# from nilearn import image
# from nilearn.image import smooth_img
# result_img=smooth_img(path, fwhm=0)  # 存储图像，smooth_img 返回一个NiftiImage对象
# print(result_img.shape[3])
# # print('result_img\n', result_img)
# # print('显示原始图像的尺寸\n', result_img.shape)  # 显示原始图像的尺寸
# first_rsn = image.index_img(result_img, 50)  # 显示一个时间点为50时的三维数据
# # print(type(first_rsn.get_data()))
# #savemat('sub-HCD0021614_func_schaefer.mat', {'data': first_rsn.get_data()})
# #print('显示三维图像的尺寸\n', first_rsn.get_data())  # 显示三维图像的尺寸
# matrix2 = first_rsn.get_data()

import nibabel as nib
import os
import numpy as np
from nilearn import image
from nilearn.image import smooth_img

subid = ['sub-HCD0001305', 'sub-HCD0008117', 'sub-HCD0021614']  # 'sub-HCD0001305', 'sub-HCD0008117',

for i in subid:
    reslist = []
    print('被试：', i, '开始...')
    wmdatapath = '/Users/fan/Documents/Data/HCPData/HCPDtest/'+i+'_space-MNI152NLin6Asym_label-WM_probseg.nii.gz'
    wmdata = nib.load(wmdatapath)
    wmmask = wmdata.get_data()
    wmmask[wmmask >= 0.6] = 1.0
    wmmask[wmmask < 0.6] = 0.0
    nib.Nifti1Image(wmmask, wmdata.affine, wmdata.header).to_filename('/Users/fan/Documents/Data/HCPData/HCPDtest/newdata/'+i+'_wmmask.nii.gz')
    print('WM mask done!')

    BOLDdatapath = '/Users/fan/Documents/Data/HCPData/HCPDtest/'+i+'_task-rest_space-MNI152NLin6Asym_desc-residual_smooth_bold.nii.gz'
    BOLDdata = smooth_img(BOLDdatapath, fwhm=0)  # 91x109x91x478 1*1*1
    print('Bolddatashape-', BOLDdata.shape[3])
    for j in range(0, BOLDdata.shape[3]):
        res = wmmask * image.index_img(BOLDdata, j).get_data()
        reslist.append(res)
    wmBold = np.array(reslist).transpose(1, 2, 3, 0)  # 不改变维度，图像会发生旋转，所以这里transpose一下
    print(i, '-wmBold-', wmBold.shape)
    nib.Nifti1Image(wmBold, BOLDdata.affine, BOLDdata.header).to_filename('/Users/fan/Documents/Data/HCPData/HCPDtest/newdata/'+i+'_task-rest_space-MNI152NLin6Asym_desc-residual_smooth_WMbold.nii.gz')

    WMBoldpath = '/Users/fan/Documents/Data/HCPData/HCPDtest/newdata/'+i+'_task-rest_space-MNI152NLin6Asym_desc-residual_smooth_WMbold.nii.gz'
    WMBoldData = nib.load(WMBoldpath).get_data()
    WMBoldData = WMBoldData.transpose(3, 0, 1, 2)
    print('WMBoldData.shape-', WMBoldData.shape)
    WMBoldParr = np.reshape(WMBoldData, (478, 91 * 109 * 91))

    JHU_ICBMPath = '/Users/fan/Documents/Data/HCPData/JHU_ICBM/rICBM_DTI_81_WMPM_60p_FMRIB58_resample.nii.gz'
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
    savemat('/Users/fan/Documents/Data/HCPData/HCPDtest/HCPDFC/'+i+'_FC.mat', {'data': resFC})




