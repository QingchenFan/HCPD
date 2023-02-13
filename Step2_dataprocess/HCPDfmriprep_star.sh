#!/bin/bash
#SBATCH --job-name=fanqingchen
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=2
#SBATCH --mem-per-cpu 2000
#SBATCH -p q_cn
#SBATCH -o /home/cuizaixu_lab/fanqingchen/DATA/Res/fmriprep/other/job.%j.out
#SBATCH -e /home/cuizaixu_lab/fanqingchen/DATA/Res/fmriprep/other/job.%j.error.txt

for file in $(ls /home/cuizaixu_lab/fanqingchen/DATA/data/HCPD/HCPD_BIDS); do
	echo "${file: 7: 13}";
	sbatch HCPDfmriprep.sh ${file: 7: 13}
done
