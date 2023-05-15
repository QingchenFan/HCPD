#!/bin/bash
#SBATCH --job-name=HCPXCPD
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=2
#SBATCH --mem-per-cpu 8G
#SBATCH -p q_cn
#SBATCH -o /home/cuizaixu_lab/fanqingchen/DATA_C/Project/HCPD/code/HCPD/Step2_dataprocess/HCPLog/xcpd_log/job.%j.out
#SBATCH -e /home/cuizaixu_lab/fanqingchen/DATA_C/Project/HCPD/code/HCPD/Step2_dataprocess/HCPLog/xcpd_log/job.%j.error.txt

# HCP
#for file in $(ls /home/cuizaixu_lab/fanqingchen/DATA_C/data/HCP/fmriprep_REST1_NMSM); do
#	echo "${file: 4: 9}";
#	sbatch xcpdpy.sh ${file: 4: 9}
#done

# 漏网之鱼
my_array=('sub-597869' 'sub-579867' 'sub-995174' 'sub-587664' 'sub-585256' 'sub-599671' 'sub-316633' 'sub-316835' 'sub-318637' 'sub-611938' 'sub-310621' 'sub-599065' 'sub-616645' 'sub-604537' 'sub-735148' 'sub-731140' 'sub-598568' 'sub-580044' 'sub-729557' 'sub-581349')
for fruit in "${my_array[@]}"
do
  echo "$fruit"
  sbatch xcpdpy.sh ${fruit: 4: 9}
done
# HCPD
#for file in $(ls /home/cuizaixu_lab/fanqingchen/DATA_C/data/HCPD/fmriprep_rest_no_MSM); do
#	echo "${file: 4: 13}";
#	sbatch xcpdpy.sh ${file: 4: 13}
#done