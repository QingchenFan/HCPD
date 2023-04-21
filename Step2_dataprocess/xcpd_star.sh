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

for file in $(ls /ibmgpfs/cuizaixu_lab/Public_Data/HCP_ALL_Family/processed_data/rest_fmriprep_no_MSM/fmriprep_REST1_NMSM); do
	echo "${file: 4: 9}";
	sbatch xcpdpy.sh ${file: 4: 9}
done

#for file in $(ls /home/cuizaixu_lab/fanqingchen/DATA_C/data/HCPD/fmriprep_rest_no_MSM); do
#	echo "${file: 4: 13}";
#	sbatch xcpdpy.sh ${file: 4: 13}
#done