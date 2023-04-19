# coding: utf-8
import pandas as pd
import numpy as np
from xcp_abcd.utils import write_save

from xcp_abcd.interfaces import regression
from xcp_abcd.interfaces.confound import ConfoundMatrix
import os
import xcp_abcd.utils as utils
from bids import BIDSLayout

def readjson(jsonfile):
    import json
    with open(jsonfile) as f:
        data = json.load(f)
    return data


MSC = '/GPFS/cuizaixu_lab_permanent/Public_Data/MSC_data/processed_data/all_fmriprep/fmriprep/sub-MSC10'
for ses in np.arange(1,11):
    if ses<10:
        data_file = os.path.join(MSC+'/ses-func0'+str(ses))
        motor_file = os.path.join(data_file,'func/sub-MSC10_ses-func0'+ str(ses) +'_task-memoryfaces_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz')
        new_name = os.path.join(data_file,'func/sub-MSC10_ses-func0'+ str(ses) +'_task-rest_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz')
    else:
        data_file = os.path.join(MSC+'/ses-func0'+str(1))
        motor_file = os.path.join(data_file,'func/sub-MSC10_ses-func0'+ str(1) +'_task-memoryfaces_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz')
        new_name = os.path.join(MSC+'/ses-func10/func/sub-MSC10_ses-func'+ str(ses) +'_task-rest_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz')   
    cmd = 'cp '+ motor_file +' '+new_name
    os.system(cmd)


layout = BIDSLayout(str(MSC), validate=False, derivatives=False)
layout,subj_data= utils.collect_data(bids_dir=MSC,participant_label=['MSC10'],task=None,bids_validate=False)

task = "rest"
participant_label = "MSC10"
queries = {
        'regfile': {'datatype': 'anat','suffix':'xfm'},
        'boldfile': {'datatype':'func','suffix': 'bold'},
        't1w': {'datatype':'anat','suffix':'T1w'},
        'seg': {'datatype':'anat','suffix':'dseg'},
        'pial': { 'datatype': 'anat','suffix':'pial'},
        'wm': {'datatype': 'anat','suffix':'smoothwm'},
        'midthickness':{'datatype': 'anat','suffix':'midthickness'},
        'inflated':{'datatype': 'anat','suffix':'inflated'}
    }

bids_filters = {}
for acq, entities in bids_filters.items():
    queries[acq].update(entities)

if task:
    #queries["preproc_bold"]["task"] = task
    queries['boldfile']["task"] = task

subj_data = {
    dtype: sorted(
        layout.get(
            return_type="file",
            subject=participant_label,
            extension=["nii", "nii.gz","dtseries.nii","h5",'gii'],
            **query,
        )
    )
    for dtype, query in queries.items()
}


subject_data = utils.bids.select_cifti_bold(subj_data)

data_dir = '/GPFS/cuizaixu_lab_permanent/wuguowei/deratives/fmriprep/'
for sub in np.arange(10):
    if sub < 9:
        sub_name = 'sub-MSC0'+str(sub+1)
    else:
        sub_name = 'sub-MSC'+str(sub+1)
    for ses in np.arange(10):
        if ses < 9:
            ses_name = 'ses-func0'+str(ses+1)
        else:
            ses_name = 'ses-func'+str(ses+1)
        datafile=data_dir+sub_name+'/'+ses_name+'/func/'+sub_name+'_'+ses_name+'_task-rest_space-MNI152NLin6Asym_res-2_desc-preproc_bold.nii.gz'

        maskfile=data_dir+sub_name+'/'+ses_name+'/func/'+sub_name+'_'+ses_name+'_task-rest_space-MNI152NLin6Asym_res-2_desc-brain_mask.nii.gz'
        conf = ConfoundMatrix()
        conf.inputs.in_file = datafile
        conf.inputs.params = "24P"
        conf.inputs.head_radius=50
        conf.inputs.TR = 2.2
        conf.run()
        reg = regression.regress()
        reg.inputs.in_file = datafile
        reg.inputs.confounds = conf._results['confound_file']
        reg.inputs.tr = 2.2
        reg.inputs.mask = maskfile
        reg.run()
        print(ses_name)

maskfile

data_dir = '/GPFS/cuizaixu_lab_permanent/wuguowei/MSC_detrend/sub-MSC01/'
for ses in np.arange(10):
    if ses < 9:
        ses_name = 'ses-func0'+str(ses+1)
    else:
        ses_name = 'ses-func'+str(ses+1)
    datafile=data_dir+ses_name+'/sub-MSC01_'+ses_name+'_task-rest_space-MNI152NLin6Asym_desc-preproc_bold.nii.gz'
    
    maskfile=data_dir+ses_name+'/sub-MSC01_'+ses_name+'_task-rest_space-MNI152NLin6Asym_desc-brain_mask.nii.gz'
    conf = ConfoundMatrix()
    conf.inputs.in_file = datafile
    conf.inputs.params = "24P"
    conf.inputs.head_radius=50
    conf.inputs.TR = 2.2
    conf.run()
    reg = regression.regress()
    reg.inputs.in_file = datafile
    reg.inputs.confounds = conf._results['confound_file']
    reg.inputs.tr = 2.2
    reg.inputs.mask = maskfile
    reg.run()
    print(ses_name)


# # HCP-7T

data_dir = '/GPFS/cuizaixu_lab_permanent/Public_Data/HCP/7T_derivative/fmriprep/'
data_list = os.listdir(data_dir)
runs = ['_run-1','_run-2']
direction = ['AP','PA']
for subname in data_list:
    for run in runs:
        for direct in direction: 
            datafile= os.path.join(data_dir,subname,'func',subname+'_task-REST_acq-'+direct+run+'_space-MNI152NLin6Asym_res-2_desc-preproc_bold.nii.gz')
            maskfile= os.path.join(data_dir,subname,'func',subname+'_task-REST_acq-'+direct+run+'_space-MNI152NLin6Asym_res-2_desc-brain_mask.nii.gz')
            if os.path.exists(datafile):
                conf = ConfoundMatrix()
                conf.inputs.in_file = datafile
                conf.inputs.params = "24P"
                conf.inputs.head_radius=50
                conf.inputs.TR = 0.72
                conf.run()
                reg = regression.regress()
                reg.inputs.in_file = datafile
                reg.inputs.confounds = conf._results['confound_file']
                reg.inputs.tr = 0.72
                reg.inputs.mask = maskfile
                reg.run()
                print(subname+run)


# In[9]:


os.path.exists(datafile)

conf = ConfoundMatrix()
        conf.inputs.in_file = datafile
        conf.inputs.params = "24P"
        conf.inputs.head_radius=50
        conf.inputs.TR = 2.2
        conf.run()
        reg = regression.regress()
        reg.inputs.in_file = datafile
        reg.inputs.confounds = conf._results['confound_file']
        reg.inputs.tr = 2.2
        reg.inputs.mask = maskfile
        reg.run()
        print(ses_name)

