#!/bin/bash
#SBATCH --job-name=fanqingchen
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=2
#SBATCH --mem-per-cpu 8G
#SBATCH -p q_fat_c
#SBATCH -q high_c
#SBATCH -o /home/cuizaixu_lab/fanqingchen/DATA_C/Project/HCPD/code/HCPD/Step2_dataprocess/Log/xcpd_log/job.%j.out
#SBATCH -e /home/cuizaixu_lab/fanqingchen/DATA_C/Project/HCPD/code/HCPD/Step2_dataprocess/Log/xcpd_log/job.%j.error.txt
echo $1
module load fsl
module load afni
module load connectome-workbench
module load ants

python /home/cuizaixu_lab/fanqingchen/DATA_C/Project/HCPD/code/HCPD/Step2_dataprocess/xcpd_HCPDII.py $1
