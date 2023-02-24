#!/bin/bash
#SBATCH --job-name=fanqingchen
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem-per-cpu 8G
#SBATCH -p q_cn
#SBATCH -o /home/cuizaixu_lab/fanqingchen/DATA/Res/fmriprep/job.%j.out
#SBATCH -e /home/cuizaixu_lab/fanqingchen/DATA/Res/fmriprep/job.%j.error.txt
module load singularity/3.7.0


#!/bin/bash
#User inputs:
bids_root_dir=/home/cuizaixu_lab/fanqingchen/DATA/data/HCPD/HCPD_BIDS
bids_root_dir_output_wd4singularity=/home/cuizaixu_lab/fanqingchen/DATA/data/HCPD_tep_wk

mkdir $bids_root_dir_output_wd4singularity
subj=$1
nthreads=40

mkdir $bids_root_dir/derivatives
mkdir $bids_root_dir_output_wd4singularity/derivatives
#Run fmriprep
echo ""
echo "Running fmriprep on participant: sub-HCD$subj"
echo ""
#Make fmriprep directory and participant directory in derivatives folder
if [ ! -d $bids_root_dir/derivatives/fmriprep ]; then
    mkdir $bids_root_dir/derivatives/fmriprep
fi

if [ ! -d $bids_root_dir/derivatives/fmriprep/sub-HCD${subj} ]; then
    mkdir $bids_root_dir/derivatives/fmriprep/sub-HCD${subj}
fi
if [ ! -d $bids_root_dir_output_wd4singularity/derivatives/fmriprep ]; then
    mkdir $bids_root_dir_output_wd4singularity/derivatives/fmriprep
fi

if [ ! -d $bids_root_dir_output_wd4singularity/derivatives/fmriprep/sub-HCD${subj} ]; then
    mkdir $bids_root_dir_output_wd4singularity/derivatives/fmriprep/sub-HCD${subj}
fi

#Run fmriprep
export SINGULARITYENV_TEMPLATEFLOW_HOME=/home/cuizaixu_lab/fanqingchen/DATA/templateflow                             #将templateflow加载到singularity_fmriprep
#修改python环境
unset PYTHONPATH; singularity run --cleanenv -B $bids_root_dir_output_wd4singularity/derivatives/fmriprep/sub-HCD${subj}:/wd \
    -B $bids_root_dir:/inputbids \
    -B $bids_root_dir/derivatives/fmriprep/sub-HCD${subj}:/output \
    -B /GPFS/cuizaixu_lab_temp/wuguowei/code:/freesurfer_license \
    /usr/nzx-cluster/apps/fmriprep/singularity/fmriprep-20.2.1.simg \
    /inputbids /output participant \
    --participant_label HCD${subj} \
    -w /wd \
    --nthreads $nthreads \
    --omp-nthreads $nthreads \
    --mem-mb 160000 \
    --fs-license-file /freesurfer_license/license.txt \
    --output-spaces T1w MNI152NLin6Asym MNI152NLin2009cAsym  \
    --return-all-components \
    --notrack --verbose \
    --skip-bids-validation --debug all --stop-on-first-crash --use-syn-sdc --resource-monitor --cifti-output 91k
