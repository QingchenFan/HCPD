from shutil import copy
import os
import glob
import json
dataPath = '/ibmgpfs/cuizaixu_lab/fanqingchen/data/HCP/fmriprep_REST1_NMSM'
dataName = os.listdir(dataPath)
#dataName = ['sub-100206', 'sub-100307']
for i in dataName:
    tname = i[4:10]
    t1wfile = '/ibmgpfs/cuizaixu_lab/fanqingchen/data/HCP/T1w/'+tname+'_3T_Structural_preproc/'+tname+'/MNINonLinear/T1w.nii.gz'
    targetpath = '/ibmgpfs/cuizaixu_lab/fanqingchen/data/HCP/fmriprep_REST1_NMSM/'+i+'/anat/'+i+'_T1w.nii.gz'
    if not os.path.exists(t1wfile):
        print('not subID-', i)
        continue
    copy(t1wfile, targetpath)
    jsonStruc = {'SkullStripped': 'false',
                 'Project': 'HCP'}
    box = json.dumps(jsonStruc, indent=1)
    jsonpath = '/ibmgpfs/cuizaixu_lab/fanqingchen/data/HCP/fmriprep_REST1_NMSM/'+i+'/anat/'+i+'_T1w.json'
    with open(jsonpath, 'w', newline='\n') as f:
        f.write(box)