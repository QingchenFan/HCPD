import nibabel as nib
import glob
from nilearn.image import resample_to_img
import numpy as np

wmpath = '/home/cuizaixu_lab/fanqingchen/DATA_C/data/HCPD/wmmask/*WM_probseg.nii.gz'
datapath = sorted(glob.glob(wmpath))

tem = np.zeros((241, 286, 241))
for i in datapath:
    data = nib.load(i).get_data()
    tem = tem + data
    resdata = tem/len(datapath)

subwmpath = '/home/cuizaixu_lab/fanqingchen/DATA_C/data/HCPD/wmmask/sub-HCD0001305_space-MNI152NLin2009cAsym_label-WM_probseg.nii.gz'

subdata = nib.load(subwmpath)
nib.Nifti1Image(resdata, subdata.affine, subdata.header).to_filename('./gruopwmmask.nii.gz')

sourcedata = './gruopwmmask.nii.gz'
targetdata = './sub-HCD0001305_task-rest_space-MNI152NLin2009cAsym_desc-residual_smooth_bold.nii.gz'
outdata = resample_to_img(source_img=sourcedata, target_img=targetdata)


nib.Nifti1Image(outdata.get_data(), outdata.affine, outdata.header).to_filename('./resamplegruopwmmask.nii.gz')
