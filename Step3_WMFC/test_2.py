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
def maskresample(sourcepath, targetpath, savepath, resamplefilename):
    print('--in--')
    sourcepath = '/Users/fan/Documents/Data/HCPData/JHU_ICBM/rICBM_DTI_81_WMPM_60p_FMRIB58.nii.gz'
    targetpath = '/Users/fan/Documents/Data/HCPData/HCPDtest/newdata/sub-HCD0021614_task-rest_space-MNI152NLin6Asym_desc-residual_smooth_WMbold.nii.gz'
    outdata = resample_to_img(source_img=sourcepath, target_img=targetpath, interpolation='nearest')
    nib.Nifti1Image(outdata.get_data(), outdata.affine, outdata.header).to_filename('/Users/fan/Documents/Data/HCPData/JHU_ICBM/rICBM_DTI_81_WMPM_60p_FMRIB58_resample.nii.gz')
    newAtlaspath = '/Users/fan/Documents/Data/HCPData/JHU_ICBM/rICBM_DTI_81_WMPM_60p_FMRIB58_resample.nii.gz'
    atlasdata = nib.load(newAtlaspath).get_data()
    print(np.max(atlasdata))


JHU_ICBMPath = '/Users/fan/Documents/Data/HCPData/JHU_ICBM/rICBM_DTI_81_WMPM_60p_FMRIB58_resample.nii.gz'
JHU_ICBMData = nib.load(JHU_ICBMPath)
JHU_ICBMParr = JHU_ICBMData.get_data()
JHU_ICBMParr = np.reshape(JHU_ICBMParr, (1, 91*109*91))
print(np.max(JHU_ICBMParr))
print(np.min(JHU_ICBMParr))
print(JHU_ICBMParr.shape)

WMBoldpath = '/Users/fan/Documents/Data/HCPData/HCPDtest/newdata/sub-HCD0001305_task-rest_space-MNI152NLin6Asym_desc-residual_smooth_WMbold.nii.gz'
WMBoldData = nib.load(WMBoldpath).get_data()
WMBoldData = WMBoldData.transpose(3, 0, 1, 2)
print(WMBoldData.shape)
WMBoldParr = np.reshape(WMBoldData, (478, 91*109*91))
print(WMBoldParr.shape)
for i in range(1, 68):
    index = np.where(JHU_ICBMParr == i)
    print(index[1])
    roi = WMBoldParr[:, index[1]]
    totalvoxel = roi.shape[1]
    for j in range(0, roi.shape[1]):
       if ~np.any(roi[:, j]):
           totalvoxel = totalvoxel - 1


