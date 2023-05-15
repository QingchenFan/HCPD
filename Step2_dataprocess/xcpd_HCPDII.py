from xcp_abcd import workflow
from bids import BIDSLayout
import sys
def fmri_surface_post_process(subname):
    # fmri_prep_dir = '/ibmgpfs/cuizaixu_lab/fanqingchen/data/HCPD/fmriprep_rest_no_MSM/sub-' + subname
    # work_dir = '/ibmgpfs/cuizaixu_lab/fanqingchen/data/HCPD/HCPD_xcpd'
    # output_dir = '/ibmgpfs/cuizaixu_lab/fanqingchen/data/HCPD/HCPD_xcpd'
    fmri_prep_dir = '/home/cuizaixu_lab/fanqingchen/DATA_C/data/HCP/fmriprep_REST1_NMSM/sub-' + subname
    work_dir = '/ibmgpfs/cuizaixu_lab/fanqingchen/data/HCP/HCP_xcpd'
    output_dir = '/ibmgpfs/cuizaixu_lab/fanqingchen/data/HCP/HCP_xcpd'
    layout = BIDSLayout(str(fmri_prep_dir), validate=False, derivatives=True)
    lower_bpf = 0.01
    upper_bpf = 0.1
    contigvol = 5
    bpf_order = 2
    cifti = False
    task_id = 'REST1'
    brain_template='MNI152NLin2009cAsym'
    motion_filter_order = 4
    motion_filter_type = 'fif'
    band_stop_min = 0
    band_stop_max = 0
    smoothing = 6
    head_radius = 50
    subject_list = [subname]
    params = '24P'
    custom_conf = None
    omp_nthreads = 3
    dummytime = 0
    fd_thresh = 0.3
    despike = True

    cifti_process_wf = workflow.base.init_xcpabcd_wf(layout, lower_bpf, upper_bpf, contigvol, despike, bpf_order, motion_filter_order,
                                                     motion_filter_type, band_stop_min, band_stop_max, fmri_prep_dir, omp_nthreads,
                                                     cifti, task_id, head_radius, params, brain_template, subject_list, smoothing,
                                                     custom_conf, output_dir, work_dir, dummytime, fd_thresh, name='xcpabcd_wf')
    cifti_process_wf.run()



fmri_surface_post_process(sys.argv[1])  # sys.argv[1]
