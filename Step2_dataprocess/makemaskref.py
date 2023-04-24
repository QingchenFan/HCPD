import sys
from shutil import copy
import os
from nilearn import image
from nilearn.image import smooth_img
import nibabel as nib
subid = sys.argv[1]
print('sub', subid)

subpath = '/ibmgpfs/cuizaixu_lab/fanqingchen/data/HCPD/sMRI_processed_20210514'
HCPDpath = '/ibmgpfs/cuizaixu_lab/fanqingchen/data/HCPD/fmriprep_rest_no_MSM'
# subpath = '/ibmgpfs/cuizaixu_lab/fanqingchen/data/HCP/fmriprep_REST1_NMSM'
# HCPDpath = '/ibmgpfs/cuizaixu_lab/fanqingchen/data/HCP/fmriprep_REST1_NMSM'

# print('subid[4:]-', subid[4:])
# maskpath = subpath + '/' + subid + '/func/'+subid+'_task-REST1_acq-LR_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz'
# print('maskpath-', maskpath)
# if not os.path.exists(maskpath):
#         print('*subid*', subid)
#         exit()
# antmast = HCPDpath + '/' + subid + '/anat/' + subid + '_desc-brain_mask.nii.gz'
# copy(maskpath, antmast)


# rest1_ap = HCPDpath + '/' + subid + '/func/' + subid + '_task-REST1_acq-AP_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz'
# rest1_pa = HCPDpath + '/' + subid + '/func/' + subid + '_task-REST1_acq-PA_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz'
# rest2_ap = HCPDpath + '/' + subid + '/func/' + subid + '_task-REST2_acq-AP_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz'
# rest2_pa = HCPDpath + '/' + subid + '/func/' + subid + '_task-REST2_acq-PA_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz'
# boxpath = HCPDpath + '/' + subid
#
#
#
# print('rest1_ap', rest1_ap)
# copy(maskpath, rest1_ap)
# copy(maskpath, rest1_pa)
# copy(maskpath, rest2_ap)
# copy(maskpath, rest2_pa)

bold_rest1_ap = HCPDpath + '/' + subid + '/func/' + subid + '_task-REST1_acq-AP_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz'
bold_rest1_pa = HCPDpath + '/' + subid + '/func/' + subid + '_task-REST1_acq-PA_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz'
bold_rest2_ap = HCPDpath + '/' + subid + '/func/' + subid + '_task-REST2_acq-AP_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz'
bold_rest2_pa = HCPDpath + '/' + subid + '/func/' + subid + '_task-REST2_acq-PA_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz'

print('bold_rest1_ap', bold_rest1_ap)

BOLDdata_1 = smooth_img(bold_rest1_ap, fwhm=0)
nib.Nifti1Image(image.index_img(BOLDdata_1, 1).get_data(), BOLDdata_1.affine, BOLDdata_1.header).to_filename(HCPDpath + '/' + subid + '/func/'+subid+'_task-REST1_acq-AP_space-MNI152NLin2009cAsym_boldref.nii.gz')

BOLDdata_2 = smooth_img(bold_rest1_pa, fwhm=0)
nib.Nifti1Image(image.index_img(BOLDdata_2, 1).get_data(), BOLDdata_2.affine, BOLDdata_2.header).to_filename(HCPDpath + '/' + subid + '/func/'+subid+'_task-REST1_acq-PA_space-MNI152NLin2009cAsym_boldref.nii.gz')

BOLDdata_3 = smooth_img(bold_rest1_ap, fwhm=0)
nib.Nifti1Image(image.index_img(BOLDdata_3, 1).get_data(), BOLDdata_3.affine, BOLDdata_3.header).to_filename(HCPDpath + '/' + subid + '/func/'+subid+'_task-REST2_acq-AP_space-MNI152NLin2009cAsym_boldref.nii.gz')

BOLDdata_4 = smooth_img(bold_rest1_ap, fwhm=0)
nib.Nifti1Image(image.index_img(BOLDdata_4, 1).get_data(), BOLDdata_4.affine, BOLDdata_4.header).to_filename(HCPDpath + '/' + subid + '/func/'+subid+'_task-REST2_acq-PA_space-MNI152NLin2009cAsym_boldref.nii.gz')
print('Done!')