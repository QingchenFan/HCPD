# coding: utf-8
import pandas as pd
import numpy as np
from xcp_abcd.utils import write_save

from xcp_abcd.interfaces import regression
from xcp_abcd.interfaces.confound import ConfoundMatrix
import os
import xcp_abcd.utils as utils
from bids import BIDSLayout

datafile = '/ibmgpfs/cuizaixu_lab/fanqingchen/data/HCPD/fmriprep_rest_no_MSM/sub-HCD0031617/func/sub-HCD0031617_task-REST2_acq-PA_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz'

maskfile = '/ibmgpfs/cuizaixu_lab/fanqingchen/data/HCPD/fmriprep_rest_no_MSM/sub-HCD0031617/func/sub-HCD0031617_task-REST2_acq-PA_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz'
conf = ConfoundMatrix()
conf.inputs.in_file = datafile
conf.inputs.params = "24P"
conf.inputs.head_radius = 50
conf.inputs.TR = 0.8
conf.run()
reg = regression.regress()
reg.inputs.in_file = datafile
reg.inputs.confounds = conf._results['confound_file']
reg.inputs.tr = 0.8
reg.inputs.mask = maskfile
reg.run()
