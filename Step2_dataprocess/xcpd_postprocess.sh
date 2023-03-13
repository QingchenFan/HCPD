#!/bin/bash
#SBATCH --job-name=fanqingchen
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=6
#SBATCH --mem-per-cpu 8G
#SBATCH -p q_fat_c
#SBATCH -q high_c
#SBATCH -o /home/cuizaixu_lab/fanqingchen/DATA_C/Code/HCPDCode/Step2_dataprocess/Log/xcpdLog/job.%j.out
#SBATCH -e /home/cuizaixu_lab/fanqingchen/DATA_C/Code/HCPDCode/Step2_dataprocess/Log/xcpdLog/job.%j.error.txt
##### END OF JOB DEFINITION  #####

echo ""
echo "Running fmriprep on participant: sub-HCD$1"
echo ""
module load singularity_xcp_abcd/0.0.4
singularity run -B /home/cuizaixu_lab/fanqingchen/DATA_C/data/HCPD/HCPD_BIDS/derivatives/fmriprep/sub-HCD$1/fmriprep/:/data \
 -B /home/cuizaixu_lab/fanqingchen/DATA_C/data/HCPD/HCPD_xcpd/derivatives/:/out \
 -B /home/cuizaixu_lab/fanqingchen/.cache:/home/xcp_abcd/.cache \
 /home/cuizaixu_lab/wuguowei/DATA_C/aconda_envirment/xcp_abcd.sif \
 /data /out participant -w /out --participant_label HCD$1  \
 -p 24P --despike --lower-bpf 0.01 --upper-bpf 0.1

