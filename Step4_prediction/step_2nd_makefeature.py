import pandas as pd
from shutil import copy
import scipy.io as scio
import numpy as np

def upper_tri_indexing(matirx):
    m = matirx.shape[0]
    r, c = np.triu_indices(m, 1)
    return matirx[r, c]


def copydata(sourpath, targetpath,filename):
    filename = '/Users/fan/Documents/Data/HCPData/behavior/flanker/flanker01_lable.csv'

    label = pd.read_csv(filename)

    #label = list()
    for i in label['src_subject_id']:
        FCpath = '/Users/fan/Documents/Data/HCPData/HCPDFC/wmFC/sub-'+i+'_FC.mat'
        targetpath = '/Users/fan/Documents/Data/HCPData/HCPD_Flanker_FC/'
        print(FCpath)
        copy(FCpath, targetpath)
label = pd.read_csv('/Users/fan/Documents/Data/HCPData/behavior/flanker/flanker01_lable.csv')
label['src_subject_id']
files_data = []
for i in label['src_subject_id']:
    data = scio.loadmat('/Users/fan/Documents/Data/HCPData/HCPDFC/wmFC/sub-'+i+ '_FC.mat')['data']
    print(data)
    print(data.shape)
    img_data_reshape = upper_tri_indexing(data)
    files_data.append(img_data_reshape)

x_data = np.asarray(files_data)
print(x_data.shape)
scio.savemat('./HCPDMori68FC.mat', {'data': x_data})
np.savetxt('./HCPDMori68FC.txt', x_data)














