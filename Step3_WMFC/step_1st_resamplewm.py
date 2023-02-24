

import nibabel as nib
import glob
from nilearn.image import resample_to_img
import os
# wmpath = '/home/cuizaixu_lab/fanqingchen/DATA_C/data/HCPD/HCPD_BIDS/derivatives/fmriprep/*/fmriprep/*/anat/*space-MNI152NLin2009cAsym_label-WM_probseg.nii.gz'
# datawmpath = sorted(glob.glob(wmpath))
#
# boldpath = '/home/cuizaixu_lab/fanqingchen/DATA_C/data/HCPD/HCPD_xcpd/derivatives/xcp_abcd/*/func/*_task-rest_space-MNI152NLin2009cAsym_desc-residual_smooth_bold.nii.gz'
# boldpath = sorted(glob.glob(boldpath))

subpath = '/home/cuizaixu_lab/fanqingchen/DATA_C/data/HCPD/HCPD_BIDS/derivatives/fmriprep'
subid = os.listdir(subpath)
Louwangzhiyu = ['sub-HCD1906457', 'sub-HCD2239247', 'sub-HCD2311633', 'sub-HCD2203933', 'sub-HCD2223131', 'sub-HCD2240030', 'sub-HCD2229547',
       'sub-HCD2333340', 'sub-HCD2322335', 'sub-HCD2236140','sub-HCD2300426','sub-HCD2302430', 'sub-HCD2207840', 'sub-HCD2220428',
       'sub-HCD2286155','sub-HCD2254243','sub-HCD2301428','sub-HCD2310328','sub-HCD2264549','sub-HCD2256651','sub-HCD2211932','sub-HCD2216437','sub-HCD2335344','sub-HCD2304737'
       ]  # "漏网之鱼"
for i in subid:
    wmdata = '/home/cuizaixu_lab/fanqingchen/DATA_C/data/HCPD/HCPD_BIDS/derivatives/fmriprep/'+i+'/fmriprep/'+i+'/anat/'+i+'_space-MNI152NLin2009cAsym_label-WM_probseg.nii.gz'
    bolddata = '/home/cuizaixu_lab/fanqingchen/DATA_C/data/HCPD/HCPD_xcpd/derivatives/xcp_abcd/'+i+'/func/'+i+'_task-rest_space-MNI152NLin2009cAsym_desc-residual_smooth_bold.nii.gz'
    if not os.path.exists(wmdata) or not os.path.exists(bolddata):
        print(i)
        continue
    outdata = resample_to_img(source_img=wmdata, target_img=bolddata)
    nib.Nifti1Image(outdata.get_data(), outdata.affine, outdata.header).to_filename('/home/cuizaixu_lab/fanqingchen/DATA_C/data/HCPD/wmmask/resampleWM/'+i+'_space-MNI152NLin2009cAsym_label-resampleWM_probseg.nii.gz')


