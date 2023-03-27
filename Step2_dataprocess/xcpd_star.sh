#!/bin/bash
#SBATCH --job-name=fanqingchen
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=2
#SBATCH --mem-per-cpu 2000
#SBATCH -p q_cn
#SBATCH -o /home/cuizaixu_lab/fanqingchen/DATA_C/Res/fmriprep/other/job.%j.out
#SBATCH -e /home/cuizaixu_lab/fanqingchen/DATA_C/Res/fmriprep/other/job.%j.error.txt

for file in $(ls /home/cuizaixu_lab/fanqingchen/DATA_C/data/HCPD/fmriprep_rest_no_MSM); do
	echo "${file: 7: 13}";
	#sbatch xcpd_postprocess.sh ${file: 7: 13}
done