import nibabel as nib
import os
import numpy as np
from nilearn import image
from nilearn.image import smooth_img
subpath = '/home/cuizaixu_lab/fanqingchen/DATA_C/data/HCPD/HCPD_BIDS/derivatives/fmriprep'
subid = os.listdir(subpath)

reslist = []
for i in subid:
    wmdata = '/home/cuizaixu_lab/fanqingchen/DATA_C/data/HCPD/wmmask/resampleWM/'+i+'_space-MNI152NLin2009cAsym_label-resampleWM_probseg.nii.gz'
    wmmask = nib.load(wmdata).get_data()
    wmmask[wmmask >= 0.6] = 1.0
    wmmask[wmmask < 0.6] = 0.0

    BOLDdatapath = '/home/cuizaixu_lab/fanqingchen/DATA_C/data/HCPD/HCPD_xcpd/derivatives/xcp_abcd/'+i+'/func/'+i+'_task-rest_space-MNI152NLin2009cAsym_desc-residual_smooth_bold.nii.gz'
    BOLDdata = smooth_img(BOLDdatapath)
    for j in range(0, BOLDdata.shape[3]):
        res = wmmask * image.index_img(BOLDdata, j)
        reslist.append(res)
    wmBold = np.array(reslist)
    nib.Nifti1Image(wmBold, BOLDdata.affine, BOLDdata.header).to_filename('/home/cuizaixu_lab/fanqingchen/DATA_C/data/HCPD/HCPD_WMBOLD/'+i+'_task-rest_space-MNI152NLin2009cAsym_desc-residual_smooth_WMbold.nii.gz')








