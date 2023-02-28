import numpy as np
import nibabel as nib
from nilearn import image
from nilearn.image import smooth_img

a = np.random.randint(1, 10, (3, 2, 5))
print(a)
b = np.reshape(a, (1, 30))
print(b)

c = np.random.randint(1, 10, (4, 3, 2, 5))
print(c)
d = np.reshape(c, (4, 30))
print(d)
res = np.where(b==1)
print(type(res[0]))
print('res-', res[0])
exit()


BOLDdatapath = '/Users/fan/Documents/Data/HCPData/HCPDtest/newdata/sub-HCD0001305_task-rest_space-MNI152NLin2009cAsym_desc-residual_smooth_WMbold.nii.gz'
BOLDdata = smooth_img(BOLDdatapath, fwhm=0)

data1 = image.index_img(BOLDdata, 50).get_data()
print('data1-', data1.shape)

data = BOLDdata.get_data()
print('data-', data.shape)
data2 = data[:, :, :, 50]
print('data2-', data2.shape)

datare = data.transpose(3, 0, 1, 2)
print(datare.shape)
data3 = datare[50, :, :, :]
print(data3.shape)
print((data3==data2).all())
