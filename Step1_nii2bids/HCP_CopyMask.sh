#!/bin/bash
#SBATCH --job-name=HCP
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --mem-per-cpu 8G
#SBATCH -p q_cn
#SBATCH -o /home/cuizaixu_lab/fanqingchen/DATA_C/Project/HCPD/code/HCPD/Step1_nii2bids/Log/job.%j.out
#SBATCH -e /home/cuizaixu_lab/fanqingchen/DATA_C/Project/HCPD/code/HCPD/Step1_nii2bids/Log/job.%j.error.txt


python /home/cuizaixu_lab/fanqingchen/DATA_C/Project/HCPD/code/HCPD/Step1_nii2bids/HCP_CopyMask.py