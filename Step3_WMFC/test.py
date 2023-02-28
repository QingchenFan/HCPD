import nibabel as nib
import numpy as np
from scipy.io import savemat
# path = '/Users/fan/Documents/Data/HCPData/HCPDtest/sub-HCD0021614_task-rest_space-MNI152NLin2009cAsym_desc-residual_smooth_bold.nii.gz'
# data = nib.load(path)
# datanp = data.get_data()
# # print(datanp.shape)
# # print(datanp[:, :, :, 0].shape)
# matrix1 = datanp[:, :, :, 50]
#
# import nibabel as nib
# from nilearn import image
# from nilearn.image import smooth_img
# result_img=smooth_img(path, fwhm=0)  # 存储图像，smooth_img 返回一个NiftiImage对象
# print(result_img.shape[3])
# # print('result_img\n', result_img)
# # print('显示原始图像的尺寸\n', result_img.shape)  # 显示原始图像的尺寸
# first_rsn = image.index_img(result_img, 50)  # 显示一个时间点为50时的三维数据
# # print(type(first_rsn.get_data()))
# #savemat('sub-HCD0021614_func_schaefer.mat', {'data': first_rsn.get_data()})
# #print('显示三维图像的尺寸\n', first_rsn.get_data())  # 显示三维图像的尺寸
# matrix2 = first_rsn.get_data()

import nibabel as nib
import os
import numpy as np
from nilearn import image
from nilearn.image import smooth_img

subid = ['sub-HCD0001305', 'sub-HCD0008117', 'sub-HCD0021614']
reslist = []
for i in subid:
    print('被试：', i, '开始...')
    wmdatapath = '/Users/fan/Documents/Data/HCPData/HCPDtest/'+i+'_space-MNI152NLin2009cAsym_label-resampleWM_probseg.nii.gz'
    wmdata = nib.load(wmdatapath)
    wmmask = wmdata.get_data()
    wmmask[wmmask >= 0.6] = 1.0
    wmmask[wmmask < 0.6] = 0.0
    nib.Nifti1Image(wmmask, wmdata.affine, wmdata.header).to_filename('/Users/fan/Documents/Data/HCPData/HCPDtest/newdata/'+i+'_wmmask.nii.gz')
    print('WM mask done!')
    BOLDdatapath = '/Users/fan/Documents/Data/HCPData/HCPDtest/'+i+'_task-rest_space-MNI152NLin2009cAsym_desc-residual_smooth_bold.nii.gz'
    BOLDdata = smooth_img(BOLDdatapath, fwhm=0)
    for j in range(0, BOLDdata.shape[3]):
        res = wmmask * image.index_img(BOLDdata, j).get_data()
        reslist.append(res)
    wmBold = np.array(reslist).transpose(1, 2, 3, 0)
    print('wmBold-', wmBold.shape)
    nib.Nifti1Image(wmBold, BOLDdata.affine, BOLDdata.header).to_filename('/Users/fan/Documents/Data/HCPData/HCPDtest/newdata/'+i+'_task-rest_space-MNI152NLin2009cAsym_desc-residual_smooth_WMbold.nii.gz')








