#!/bin/bash
#SBATCH --job-name=HCPD
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=2
#SBATCH --mem-per-cpu=2G
#SBATCH -p q_fat_c
#SBATCH -o /home/cuizaixu_lab/fanqingchen/DATA_C/Project/HCPD/Log/job.%j.out
#SBATCH -e /home/cuizaixu_lab/fanqingchen/DATA_C/Project/HCPD/Log/job.%j.error.txt

python /home/cuizaixu_lab/fanqingchen/DATA_C/Project/HCPD/code/HCPD/Step4_prediction/step_3rd_prebehaviorstar.py
