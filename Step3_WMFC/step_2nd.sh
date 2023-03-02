#!/bin/bash
#SBATCH --job-name=whitematterFC
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=2
#SBATCH --mem-per-cpu=20G
#SBATCH -p q_cn
#SBATCH -o /home/cuizaixu_lab/fanqingchen/DATA_C/Code/HCPDCode/Step3_WMFC/log/job.%j.out
#SBATCH -e /home/cuizaixu_lab/fanqingchen/DATA_C/Code/HCPDCode/Step3_WMFC/log/job.%j.error.txt

python /home/cuizaixu_lab/fanqingchen/DATA_C/Code/HCPDCode/Step3_WMFC/step_2nd_getwmbold.py