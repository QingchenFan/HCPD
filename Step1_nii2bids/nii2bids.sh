#!/bin/bash
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=2
#SBATCH --mem-per-cpu 2000
#SBATCH -p q_cn
#SBATCH -o /home/cuizaixu_lab/fanqingchen/DATA/Res/HCP_Res/server_note/step1_log/job.%j.out
#SBATCH -e /home/cuizaixu_lab/fanqingchen/DATA/Res/HCP_Res/server_note/step1_log/job.%j.error.txt

python /home/cuizaixu_lab/fanqingchen/DATA/Code/HCPDCode/Step1_nii2bids/nii2bids.py