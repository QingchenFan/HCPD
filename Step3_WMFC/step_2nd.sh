#!/bin/bash
#SBATCH --job-name=whitematterFC
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=2
#SBATCH --mem-per-cpu=20G
#SBATCH -p q_fat_c
#SBATCH -o /ibmgpfs/cuizaixu_lab/fanqingchen/Project/HCPD/code/HCPD/Step3_WMFC/log/job.%j.out
#SBATCH -e /ibmgpfs/cuizaixu_lab/fanqingchen/Project/HCPD/code/HCPD/Step3_WMFC/log/job.%j.error.txt

python /home/cuizaixu_lab/fanqingchen/DATA_C/Project/HCPD/code/HCPD/Step3_WMFC/step_2nd_getwmbold_new.py