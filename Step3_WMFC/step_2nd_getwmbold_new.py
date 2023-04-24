import sys

import nibabel as nib
import os
import numpy as np
from nilearn import image
from nilearn.image import smooth_img

subpath = '/ibmgpfs/cuizaixu_lab/fanqingchen/data/HCPD/HCPD_BIDS/derivatives/fmriprep'
subid = os.listdir(subpath)

# subid = ['sub-HCD0001305', 'sub-HCD0008117']
for i in subid:
    #  对分割出的标准空间下的白质进行重采样，到全脑BOLD数据的大小、分辨率
    reslist = []
    print('participant-', i, 'start...')
    wmmaskpath = '/ibmgpfs/cuizaixu_lab/fanqingchen/data/HCPD/HCPD_BIDS/derivatives/fmriprep/'+i+'/fmriprep/'+i+'/anat/'+i+'_space-MNI152NLin6Asym_res-2_label-WM_probseg.nii.gz'  #  这个分割出的白质数据，为了制作mask
    if not os.path.exists(wmmaskpath):
        print('no mask subid-', i)
        continue
    wmmaskdata = nib.load(wmmaskpath)
    wmmask = wmmaskdata.get_data()
    wmmask[wmmask >= 0.6] = 1.0
    wmmask[wmmask < 0.6] = 0.0
    nib.Nifti1Image(wmmask, wmmaskdata.affine, wmmaskdata.header).to_filename('/home/cuizaixu_lab/fanqingchen/DATA_C/data/HCPD/wmdata/wmmask/'+i+'_wmmask.nii.gz')
    print('WM mask done!')

    #  通过得到的白质mask,提取白质的BOLD信号
    BOLDdatapath = '/ibmgpfs/cuizaixu_lab/fanqingchen/data/HCPD/HCPD_xcpd/xcp_abcd/'+i+'/func/'+i+'_task-REST1_acq-AP_space-MNI152NLin2009cAsym_desc-residual_smooth_bold.nii.gz'
    if not os.path.exists(BOLDdatapath):
        print('no boldpath subid-', i)
        continue
    BOLDdata = smooth_img(BOLDdatapath, fwhm=0)  # 91x109x91x478 1*1*1
    print('Bolddatashape-', BOLDdata.shape[3])
    for j in range(0, BOLDdata.shape[3]):
        res = wmmask * image.index_img(BOLDdata, j).get_data()
        reslist.append(res)
    wmBold = np.array(reslist).transpose(1, 2, 3, 0)  # 不改变维度，图像会发生旋转，所以这里transpose一下
    print(i, '-wmBold-', wmBold.shape)
    nib.Nifti1Image(wmBold, BOLDdata.affine, BOLDdata.header).to_filename(
        '/home/cuizaixu_lab/fanqingchen/DATA_C/data/HCPD/wmdata/wmBold/' + i + '_task-REST1_acq-AP_space-MNI152NLin2009cAsym_desc-residual_smooth_wmbold.nii.gz')
