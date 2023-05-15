#!/bin/bash
#SBATCH --job-name=HCPfmriprep
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --mem-per-cpu 8G
#SBATCH -p q_cn
#SBATCH -o /home/cuizaixu_lab/fanqingchen/DATA_C/Res/hcpfmriprep/job.%j.out
#SBATCH -e /home/cuizaixu_lab/fanqingchen/DATA_C/Res/hcpfmriprep/job.%j.error.txt
module load singularity/3.7.0


#!/bin/bash
#User inputs:
bids_root_dir=/ibmgpfs/cuizaixu_lab/fanqingchen/data/HCP/fmriprep_REST1_NMSM
bids_root_dir_output_wd4singularity=/ibmgpfs/cuizaixu_lab/fanqingchen/data/HCP/HCP_tep_wk

mkdir $bids_root_dir_output_wd4singularity
subj=$1
nthreads=40

mkdir $bids_root_dir/derivatives
mkdir $bids_root_dir_output_wd4singularity/derivatives
#Run fmriprep
echo ""
echo "Running fmriprep on participant: sub-$subj"
echo ""
#Make fmriprep directory and participant directory in derivatives folder
if [ ! -d $bids_root_dir/derivatives/fmriprep ]; then
    mkdir $bids_root_dir/derivatives/fmriprep
fi

if [ ! -d $bids_root_dir/derivatives/fmriprep/sub-${subj} ]; then
    mkdir $bids_root_dir/derivatives/fmriprep/sub-${subj}
fi
if [ ! -d $bids_root_dir_output_wd4singularity/derivatives/fmriprep ]; then
    mkdir $bids_root_dir_output_wd4singularity/derivatives/fmriprep
fi

if [ ! -d $bids_root_dir_output_wd4singularity/derivatives/fmriprep/sub-${subj} ]; then
    mkdir $bids_root_dir_output_wd4singularity/derivatives/fmriprep/sub-${subj}
fi

#Run fmriprep
export SINGULARITYENV_TEMPLATEFLOW_HOME=/home/cuizaixu_lab/fanqingchen/DATA/templateflow
#修改python环境
unset PYTHONPATH; singularity run --cleanenv -B $bids_root_dir_output_wd4singularity/derivatives/fmriprep/sub-${subj}:/wd \
    -B $bids_root_dir:/inputbids \
    -B $bids_root_dir/derivatives/fmriprep/sub-${subj}:/output \
    -B /GPFS/cuizaixu_lab_temp/wuguowei/code:/freesurfer_license \
    /usr/nzx-cluster/apps/fmriprep/singularity/fmriprep-20.2.1.simg \
    /inputbids /output participant \
    --participant_label ${subj} \
    -w /wd \
    --nthreads $nthreads \
    --omp-nthreads $nthreads \
    --mem-mb 160000 \
    --fs-license-file /freesurfer_license/license.txt \
    --output-spaces T1w MNI152NLin6Asym:res-2 MNI152NLin2009cAsym:res-2 \
    --skip-bids-validation --anat-only

