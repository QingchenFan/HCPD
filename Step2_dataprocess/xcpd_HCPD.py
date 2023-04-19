#from xcp_d import workflows
from bids import BIDSLayout
import sys
from nilearn.image import smooth_img
from nilearn import image
import nibabel as nib
from niworkflows.func.util import init_bold_reference_wf

BOLDdatapath = '/Users/fan/Desktop/sub-HCD0031617_task-REST2_acq-PA_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz'
BOLDdata = smooth_img(BOLDdatapath, fwhm=0)
data = image.index_img(BOLDdata, 1).get_data()
nib.Nifti1Image(data, BOLDdata.affine, BOLDdata.header).to_filename(
    './sub-HCD0031617_task-REST2_acq-PA_space-MNI152NLin2009cAsym_boldref.nii.gz')

exit()
def fmri_surface_post_process(subname):
    fmri_prep_dir = '/home/cuizaixu_lab/fanqingchen/DATA_C/data/HCPD/fmriprep_rest_no_MSM/sub-HCD'+subname
    work_dir = '/home/cuizaixu_lab/fanqingchen/DATA_C/data/HCPD/HCPD_xcpd/out'
    output_dir = '/home/cuizaixu_lab/fanqingchen/DATA_C/data/HCPD/HCPD_xcpd/work'
    layout = BIDSLayout(str(fmri_prep_dir), validate=False, derivatives=False)
    lower_bpf = 0.01
    upper_bpf = 0.08
    contigvol = 5
    bpf_order = 2
    cifti = True
    task_id = None
    brain_template='MNI152NLin2009cAsym'
    motion_filter_order = 4
    motion_filter_type = 'fif'
    band_stop_min = 0
    band_stop_max = 0
    smoothing = 6
    head_radius = 50
    subject_list = [subname]
    params = '24P'
    custom_conf = []
    omp_nthreads = 3
    dummytime = 0
    fd_thresh = 0.3
    despike = True
    num_cifti = 2
    analysis_level = 'participant'
    bids_filters = None
    bandpass_filter = None
    cifti_process_wf = workflows.base.init_xcpd_wf(fmri_dir=fmri_prep_dir, layout=layout, output_dir=output_dir, low_pass=lower_bpf, high_pass=upper_bpf, despike=despike, bpf_order=bpf_order,
                                                   motion_filter_order=motion_filter_order, motion_filter_type=motion_filter_type, band_stop_min=band_stop_min, band_stop_max=band_stop_max,
                                                    omp_nthreads=omp_nthreads, cifti=cifti, task_id=task_id, head_radius=head_radius, params=params,
                                                   subject_list=subject_list, smoothing=smoothing, custom_confounds_folder=custom_conf, work_dir=work_dir,
                                                   dummy_scans=dummytime, fd_thresh=fd_thresh, analysis_level=analysis_level, bids_filters=bids_filters,
                                                   bandpass_filter=bandpass_filter, name='xcpd_wf')
    cifti_process_wf.run()
fmri_surface_post_process(sys.argv[1])
