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
for i in subid:
    wmdata = '/home/cuizaixu_lab/fanqingchen/DATA_C/data/HCPD/HCPD_BIDS/derivatives/fmriprep/'+i+'/fmriprep/'+i+'/anat/'+i+'_space-MNI152NLin2009cAsym_label-WM_probseg.nii.gz'
    bolddata = '/home/cuizaixu_lab/fanqingchen/DATA_C/data/HCPD/HCPD_xcpd/derivatives/xcp_abcd/'+i+'/func/'+i+'_task-rest_space-MNI152NLin2009cAsym_desc-residual_smooth_bold.nii.gz'
    if not os.path.exists(wmdata) or not os.path.exists(bolddata):
        print(i)
        continue
    outdata = resample_to_img(source_img=wmdata, target_img=bolddata)
    nib.Nifti1Image(outdata.get_data(), outdata.affine, outdata.header).to_filename('/home/cuizaixu_lab/fanqingchen/DATA_C/data/HCPD/wmmask/resampleWM/'+i+'_space-MNI152NLin2009cAsym_label-resampleWM_probseg.nii.gz')
