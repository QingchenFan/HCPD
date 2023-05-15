import os
from shutil import copy
import sys
import nibabel as nib
from nilearn.image import smooth_img
from nilearn import image
#
datapath = '/home/cuizaixu_lab/fanqingchen/DATA_C/data/HCP/fmriprep_REST1_NMSM'
dataName = os.listdir(datapath)
print(dataName)
nomask = []
dataName=['sub-462139', 'sub-351938', 'sub-995174', 'sub-171734', 'sub-822244', 'sub-159845', 'sub-150423', 'sub-117728', 'sub-693461', 'sub-145531', 'sub-165234', 'sub-239136', 'sub-142424', 'sub-160931', 'sub-552544', 'sub-734247', 'sub-171128', 'sub-107220', 'sub-201717', 'sub-114924', 'sub-248238', 'sub-953764', 'sub-623137', 'sub-121315', 'sub-150019', 'sub-190132', 'sub-109325', 'sub-209531', 'sub-113417', 'sub-613235', 'sub-221218', 'sub-662551', 'sub-121820', 'sub-186949', 'sub-128329', 'sub-689470', 'sub-173233', 'sub-578158', 'sub-129533', 'sub-569965', 'sub-169141']
for i in dataName:
    print('--', i, '--')
    sourcedatapath = '/home/cuizaixu_lab/fanqingchen/DATA_C/data/HCP/fmriprep_REST1_NMSM/derivatives/fmriprep/'+i+'/fmriprep/'+i+'/anat/'+i+'_space-MNI152NLin6Asym_res-2_desc-brain_mask.nii.gz'

    anattargetdatapath = '/home/cuizaixu_lab/fanqingchen/DATA_C/data/HCP/fmriprep_REST1_NMSM/'+i+'/anat/'+i+'_desc-brain_mask.nii.gz'

    LRfundatapath = '/home/cuizaixu_lab/fanqingchen/DATA_C/data/HCP/fmriprep_REST1_NMSM/'+i+'/func/'+i+'_task-REST1_acq-LR_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz'
    RLfundatapath = '/home/cuizaixu_lab/fanqingchen/DATA_C/data/HCP/fmriprep_REST1_NMSM/'+i+'/func/'+i+'_task-REST1_acq-RL_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz'

    LRrefdatapath = '/home/cuizaixu_lab/fanqingchen/DATA_C/data/HCP/fmriprep_REST1_NMSM/'+i+'/func/'+i+'_task-REST1_acq-LR_space-MNI152NLin2009cAsym_boldref.nii.gz'
    RLrefdatapath = '/home/cuizaixu_lab/fanqingchen/DATA_C/data/HCP/fmriprep_REST1_NMSM/'+i+'/func/'+i+'_task-REST1_acq-RL_space-MNI152NLin2009cAsym_boldref.nii.gz'

    if not os.path.exists(LRrefdatapath) or os.path.exists(RLrefdatapath):
        bold_LR = '/home/cuizaixu_lab/fanqingchen/DATA_C/data/HCP/fmriprep_REST1_NMSM/'+i+'/func/'+i+'_task-REST1_acq-LR_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz'
        if not os.path.exists(bold_LR):
            print('no exit LRbold-', i)
            continue
        BOLDdata_LR = smooth_img(bold_LR, fwhm=0)
        nib.Nifti1Image(image.index_img(BOLDdata_LR, 1).get_data(), BOLDdata_LR.affine, BOLDdata_LR.header).to_filename('/home/cuizaixu_lab/fanqingchen/DATA_C/data/HCP/fmriprep_REST1_NMSM/'+i+'/func/'+i+'_task-REST1_acq-LR_space-MNI152NLin2009cAsym_boldref.nii.gz')

        bold_RL = '/home/cuizaixu_lab/fanqingchen/DATA_C/data/HCP/fmriprep_REST1_NMSM/' + i + '/func/' + i + '_task-REST1_acq-RL_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz'
        if not os.path.exists(bold_RL):
            print('no exit RLbold-', i)
            continue
        BOLDdata_RL = smooth_img(bold_RL, fwhm=0)
        nib.Nifti1Image(image.index_img(BOLDdata_RL, 1).get_data(), BOLDdata_RL.affine, BOLDdata_RL.header).to_filename(
            '/home/cuizaixu_lab/fanqingchen/DATA_C/data/HCP/fmriprep_REST1_NMSM/' + i + '/func/' + i + '_task-REST1_acq-RL_space-MNI152NLin2009cAsym_boldref.nii.gz')

    if os.path.exists(anattargetdatapath) or os.path.exists(LRfundatapath) or os.path.exists(RLfundatapath):
        print('exit ant-', i)
        continue
    if not os.path.exists(sourcedatapath):
        print('no source mask-', i)
        nomask.append(i)
        continue
    copy(sourcedatapath, anattargetdatapath)
    copy(sourcedatapath, LRfundatapath)
    copy(sourcedatapath, RLfundatapath)
    print('--', i, '--done')
print('-nomask-', nomask)
# check
lwzy = []
lwzy_2 = []

datapath = '/home/cuizaixu_lab/fanqingchen/DATA_C/data/HCP/fmriprep_REST1_NMSM'
dataName = os.listdir(datapath)
print('--len--', len(dataName))
for i in dataName:
    LRrefdatapath = '/home/cuizaixu_lab/fanqingchen/DATA_C/data/HCP/fmriprep_REST1_NMSM/' + i + '/func/' + i + '_task-REST1_acq-LR_space-MNI152NLin2009cAsym_boldref.nii.gz'
    anattargetdatapath = '/home/cuizaixu_lab/fanqingchen/DATA_C/data/HCP/fmriprep_REST1_NMSM/' + i + '/anat/' + i + '_desc-brain_mask.nii.gz'
    if not os.path.exists(LRrefdatapath):
        #print('refno exit:', i)
        lwzy.append(i)
    if not os.path.exists(LRrefdatapath):
        #print('maskno exit:', i)
        lwzy_2.append(i)

print(lwzy)
print('--len--',len(lwzy))

print(lwzy_2)
print('--len--',len(lwzy_2))
