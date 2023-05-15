import os
import zipfile
from shutil import copy
import sys

subid = sys.argv[1]
id = subid[4:10]

print('-id-', id)
sourcepath = '/ibmgpfs/cuizaixu_lab/Public_Data/HCP_ALL_Family/rawdata/dMRI/'+id+'_3T_Structural_preproc.zip'

targetpath = '/ibmgpfs/cuizaixu_lab/fanqingchen/data/HCP/T1w'

copy(sourcepath, targetpath)

newpath = '/ibmgpfs/cuizaixu_lab/fanqingchen/data/HCP/T1w/'+id+'_3T_Structural_preproc.zip'
filepath = '/ibmgpfs/cuizaixu_lab/fanqingchen/data/HCP/T1w/'+id+'_3T_Structural_preproc'
with zipfile.ZipFile(newpath, 'r') as fzip:
    #文件全部加压缩到destpath目录
    fzip.extractall(filepath)

os.remove(newpath)



