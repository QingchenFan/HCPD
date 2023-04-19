import pandas as pd
import numpy as np
from xcp_abcd.utils import write_save
def readjson(jsonfile):
    import json
    with open(jsonfile) as f:
        data = json.load(f)
    return data
from xcp_abcd.interfaces import regression
from xcp_abcd.interfaces import filtering
from xcp_abcd.interfaces.confound import ConfoundMatrix
import os
from tqdm import trange
from nibabel import cifti2
from nipype.interfaces.workbench import CiftiSmooth
from templateflow.api import get as get_template
from xcp_abcd.utils import utils

indep_sub = pd.read_csv(os.path.join('/GPFS/cuizaixu_lab_permanent/Public_Data/HCP_ALL_Family/processed_data/xcpabcd/',
                                     'HCPSingleFuncParcel_n339_SubjectsIDs.csv'), header=0)['Var1']
target_path_or = '/GPFS/cuizaixu_lab_permanent/Public_Data/HCP_ALL_Family/processing/fmriprep_rest1/'
run_number=1
sigma_lx = utils.fwhm2sigma(6)
for (subname, j) in zip(indep_sub, trange(len(indep_sub))):
    subname_real = 'sub-'+str(subname)
    if run_number < 2:
        target_path = os.path.join(target_path_or, subname_real)
        datafile=target_path+'/func/'+subname_real+'_task-REST1_acq-LR_space-fsLR_den-91k_bold.dtseries.nii'
        new_path = '/GPFS/cuizaixu_lab_permanent/Public_Data/HCP_ALL_Family/processing/new_process/'+subname_real
        os.makedirs(new_path)
        os.chdir(new_path)
        conf = ConfoundMatrix()
        conf.inputs.in_file = datafile
        conf.inputs.params = "36P"
        conf.inputs.head_radius=50
        conf.inputs.TR = 0.72
        conf.run()
        filt = filtering.FilteringData()
        filt.inputs.in_file = datafile
        filt.inputs.tr = 0.72
        filt.inputs.lowpass = 0.08
        filt.inputs.highpass = 0.01
        filt.inputs.filter_order = 2
        filt.run()
        reg = regression.ciftidespike()
        reg.inputs.in_file = filt._results['filt_file']
        reg.inputs.tr = 0.72
        reg.run()
        reg_regresion = regression.regress()
        reg_regresion.inputs.in_file = reg._results['des_file']
        reg_regresion.inputs.confounds = conf._results['confound_file']
        reg_regresion.inputs.tr = 0.72
        reg_regresion.run()
        smooth = CiftiSmooth()
        smooth.inputs.in_file = reg_regresion._results['res_file']
        smooth.inputs.sigma_surf = sigma_lx
        smooth.inputs.sigma_vol=sigma_lx 
        smooth.inputs.direction ='COLUMN'
        smooth.inputs.right_surf=str(get_template("fsLR", hemi='R',suffix='sphere',density='32k')[0]) 
        smooth.inputs.left_surf=str(get_template("fsLR", hemi='L',suffix='sphere',density='32k')[0])
        smooth.run()
        run_number+=1
        print(subname)