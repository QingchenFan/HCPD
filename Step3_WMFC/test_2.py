import nibabel as nib
import numpy as np
# path = '/Users/fan/Documents/Data/HCPData/HCPDtest/newdata/sub-HCD0001305_task-rest_space-MNI152NLin2009cAsym_desc-residual_smooth_WMbold.nii.gz'
#
# data = nib.load(path)
# print(data)
# tem = data.get_data()
# print(tem.shape)
#
# path2 = '/Users/fan/Documents/Data/HCPData/HCPDtest/sub-HCD0001305_task-rest_space-MNI152NLin2009cAsym_desc-residual_smooth_bold.nii.gz'
#
# data2 = nib.load(path2)
# print(data2)
# tem2 = data2.get_data()
# print(tem2.shape)
from nilearn.image import resample_to_img

path3 = '/Users/fan/Documents/Data/HCPData/JHU_ICBM/rICBM_DTI_81_WMPM_FMRIB58.nii.gz'
wmatlas = nib.load(path3)
#print(wmatlas)

# path4 = '/Users/fan/Documents/Notes/datalearn/lianxi/bids/derivatives/xcp_abcd/sub-001/func/sub-001_task-rest_space-MNI152NLin2009cAsym_desc-residual_smooth_bold.nii.gz'
# data4 = nib.load(path4)
# print(data4)
# print('----------------')
# path5 = '/Users/fan/Documents/Notes/datalearn/lianxi/code/Reslice_aal.nii'
# data5 = nib.load(path5)
# print(data5.get_data()[22][11])

# path6 = '/Users/fan/Documents/Data/HCPData/JHU_ICBM/rICBM_DTI_81_WMPM_FMRIB58.nii.gz'
# path7 = '/Users/fan/Documents/Data/HCPData/HCPDtest/newdata/sub-HCD0001305_task-rest_space-MNI152NLin2009cAsym_desc-residual_smooth_WMbold.nii.gz'
# path6data = nib.load(path6)
# outdata = resample_to_img(source_img=path6, target_img=path7)
# print(outdata)
# nib.Nifti1Image(outdata.get_data(), outdata.affine, outdata.header).to_filename('/Users/fan/Documents/Data/HCPData/HCPDtest/newdata/rICBM_DTI_81_WMPM_FMRIB58_resample.nii.gz')

JHU_ICBMPath = '/Users/fan/Documents/Data/HCPData/HCPDtest/newdata/rICBM_DTI_81_WMPM_FMRIB58_resample.nii.gz'
JHU_ICBMData = nib.load(JHU_ICBMPath)
JHU_ICBMParr = JHU_ICBMData.get_data()
JHU_ICBMParr = np.reshape(JHU_ICBMParr, (1, 97*115*97))
print(JHU_ICBMParr.shape)
WMBoldpath = '/Users/fan/Documents/Data/HCPData/HCPDtest/newdata/sub-HCD0001305_task-rest_space-MNI152NLin2009cAsym_desc-residual_smooth_WMbold.nii.gz'
WMBoldData = nib.load(WMBoldpath).get_data()
WMBoldData = WMBoldData.transpose(3, 0, 1, 2)
print(WMBoldData.shape)
WMBoldParr = np.reshape(WMBoldData, (478, 1082035))
print(WMBoldParr.shape)

