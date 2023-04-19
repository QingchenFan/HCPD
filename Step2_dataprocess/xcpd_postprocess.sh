#!/bin/bash
#SBATCH --job-name=fanqingchen
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=6
#SBATCH --mem-per-cpu 8G
#SBATCH -p q_fat_c
#SBATCH -q high_c
#SBATCH -o /home/cuizaixu_lab/fanqingchen/DATA_C/Project/HCPD/code/HCPD/Step2_dataprocess/Log/xcpd_log/job.%j.out
#SBATCH -e /home/cuizaixu_lab/fanqingchen/DATA_C/Project/HCPD/code/HCPD/Step2_dataprocess/Log/xcpd_log/job.%j.error.txt

echo ""
echo "Running fmriprep on participant: sub-HCD$1"
echo ""
module load singularity_xcp_abcd/0.0.4
singularity run -B /home/cuizaixu_lab/fanqingchen/DATA_C/data/HCPD/fmriprep_rest_no_MSM/sub-HCD$1:/data \
 -B /home/cuizaixu_lab/fanqingchen/DATA_C/data/HCPD/HCPD_xcpd/:/out \
 -B /home/cuizaixu_lab/fanqingchen/.cache:/home/xcp_abcd/.cache \
 /home/cuizaixu_lab/fanqingchen/DATA_C/app/singularity/XCPD/xcpd.sif \
 /data /out participant -w /out --participant_label HCD$1  \
 -p 24P --despike --lower-bpf 0.01 --upper-bpf 0.1 --smoothing 6

