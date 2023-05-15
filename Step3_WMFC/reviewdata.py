import numpy as np
import nibabel as nib
from nilearn import image
from nilearn.image import smooth_img
'''
    验证reshape函数，reshape之后位置对应关系
'''
a = np.random.randint(1, 10, (3, 2, 5))
print('--a--\n', a)
b = np.reshape(a, (1, 30))
print('--b--\n', b)
print('b shape-', b.shape)

c = np.random.randint(1, 10, (5, 3, 2, 5))
print('--c--\n', c)
d = np.reshape(c, (5, 30))
print('--d--\n', d)
'''
    验证按索引取数
'''
index_1 = np.where(b==1)
index_2 = np.where(b==2)
index_3 = np.where(b==3)

print(index_1)
print(type(index_1[1]))
print('index_1-', index_1[1])

list = []
dres = d[:, index_1[1]]
dres_2 = d[:, index_2[1]]
dres_3 = d[:, index_3[1]]
print('dres-\n', dres)
print('dres2-\n', dres_2)
print('dres3-\n', dres_3)

exit()
sumdres = np.sum(dres, axis=1)
sumdres_2 = np.sum(dres_2, axis=1)
sumdres_3 = np.sum(dres_3, axis=1)

print('sumdres-', sumdres)
print('sumdres-2', sumdres_2)
print('sumdres-3', sumdres_3)

print('sumdres.shape', sumdres.shape)
averageres_1 = sumdres / sumdres.shape[0]
print('averageres_1-', averageres_1)
print('averageres_1.shape-', averageres_1.shape)


averageres_2 = sumdres_2 / sumdres_2.shape[0]
print('averageres_2-', averageres_2)
averageres_3 = sumdres_3 / sumdres_3.shape[0]
print('averageres_3-', averageres_3)

list.append(averageres_1)
list.append(averageres_2)
list.append(averageres_3)
resnp = np.array(list)
print('-resnp-\n', resnp)
resfc = np.corrcoef(resnp, rowvar=True)
print('resfc-', resfc)

'''
    判断矩阵中某一列是否全为0
'''
for i in range(0, dres.shape[1]):
    print(dres[:, i])
    iszero = ~(np.any(dres[:, i]))
    print('iszero', iszero)
exit()

'''
    python中numpy维度获取验证
'''
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

