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
# from nilearn.image import resample_to_img
# def maskresample(sourcepath, targetpath, savepath, resamplefilename):
#     print('--in--')
#     sourcepath = '/Users/fan/Documents/Data/HCPData/JHU_ICBM/rICBM_DTI_81_WMPM_60p_FMRIB58.nii.gz'
#     targetpath = '/Users/fan/Documents/Data/HCPData/HCPDtest/newdata/sub-HCD0021614_task-rest_space-MNI152NLin6Asym_desc-residual_smooth_WMbold.nii.gz'
#     outdata = resample_to_img(source_img=sourcepath, target_img=targetpath, interpolation='nearest')
#     nib.Nifti1Image(outdata.get_data(), outdata.affine, outdata.header).to_filename('/Users/fan/Documents/Data/HCPData/JHU_ICBM/rICBM_DTI_81_WMPM_60p_FMRIB58_resample.nii.gz')
#     newAtlaspath = '/Users/fan/Documents/Data/HCPData/JHU_ICBM/rICBM_DTI_81_WMPM_60p_FMRIB58_resample.nii.gz'
#     atlasdata = nib.load(newAtlaspath).get_data()
#     print(np.max(atlasdata))
#
#
# JHU_ICBMPath = '/Users/fan/Documents/Data/HCPData/JHU_ICBM/rICBM_DTI_81_WMPM_60p_FMRIB58_resample.nii.gz'
# JHU_ICBMData = nib.load(JHU_ICBMPath)
# JHU_ICBMParr = JHU_ICBMData.get_data()
# JHU_ICBMParr = np.reshape(JHU_ICBMParr, (1, 91*109*91))
# print(np.max(JHU_ICBMParr))
# print(np.min(JHU_ICBMParr))
# print(JHU_ICBMParr.shape)
#
# WMBoldpath = '/Users/fan/Documents/Data/HCPData/HCPDtest/newdata/sub-HCD0001305_task-rest_space-MNI152NLin6Asym_desc-residual_smooth_WMbold.nii.gz'
# WMBoldData = nib.load(WMBoldpath).get_data()
# WMBoldData = WMBoldData.transpose(3, 0, 1, 2)
# print(WMBoldData.shape)
# WMBoldParr = np.reshape(WMBoldData, (478, 91*109*91))
# print(WMBoldParr.shape)
# for i in range(1, 68):
#     index = np.where(JHU_ICBMParr == i)
#     print(index[1])
#     roi = WMBoldParr[:, index[1]]
#     totalvoxel = roi.shape[1]
#     for j in range(0, roi.shape[1]):
#        if ~np.any(roi[:, j]):
#            totalvoxel = totalvoxel - 1


# Install and load required libraries
# e.g. pip install numpy brainspace surfplot neuromaps nibabel

from surfplot import Plot
from brainspace.datasets import load_parcellation
from brainspace.mesh.mesh_io import read_surface
from neuromaps.datasets import fetch_fslr
import numpy as np

# Load the surface we want to use as the background
# Read in your own background surface {'.ply', '.vtp', '.vtk', '.fs', '.asc', '.gii'}
surfaces = read_surface('./path/to/surface/file.gii.gz')

# Or use one of the surface files included in the neuromaps package
# Here we are using the 32k FsLR (a symmetric version
# fsaverage space template with ~32k verticies in each hemisphere
surfaces = fetch_fslr()
lh, rh = surfaces['inflated']

# Next we want to load the parcellation/atlas we want to plot
# on the background surface. A parcellation is a array or surface file the same
# length (number of vertices) as the background surface, with the same value
# assigned to clusters of vertivies, representing discrete brain regions
# We can either read in a surface file in FsLR space
atlas = read_surface('./path/to/surface/atlas/file.gii.gz')

# Or use one of the surface files included in the brainspace package
atlas = load_parcellation('schaefer', 100, join=True)

# You can either plot this atlas directly, or assign new values
# to each parcel to demonstrate an statistical effect. Here we assign a
# random value between [0,1] to each unique parcel (excluding the medial wall [0])
unique = unique[1:len(atlas)]
for i in range(unique.shape[0]):
	rd = np.random.uniform(low=0.0, high=1.0, size=1).round(3)
	atlas = np.where(atlas==unique[i], rd, atlas)

# Generate plot
p = Plot(lh, rh, views=['lateral','medial'], zoom=1.2)
p.add_layer(atlas, cbar=True, cmap='inferno')
p.build()