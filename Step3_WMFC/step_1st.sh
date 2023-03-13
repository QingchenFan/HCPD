#!/bin/bash
#SBATCH --job-name=fanqingchen
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=6
#SBATCH --mem-per-cpu 6000
#SBATCH -p q_fat_c
#SBATCH -o /home/cuizaixu_lab/fanqingchen/DATA_C/Code/HCPDCode/Step3_WMFC/log/job.%j.out
#SBATCH -e /home/cuizaixu_lab/fanqingchen/DATA_C/Code/HCPDCode/Step3_WMFC/log/job.%j.error.txt


python /home/cuizaixu_lab/fanqingchen/DATA_C/Code/HCPDCode/Step3_WMFC/step_1st_resamplewm.py
