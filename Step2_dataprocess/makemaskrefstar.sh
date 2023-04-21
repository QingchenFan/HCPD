#!/bin/bash
#SBATCH --job-name=fanqingchen
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=2
#SBATCH --mem-per-cpu 8G
#SBATCH -p q_cn
#SBATCH -o /home/cuizaixu_lab/fanqingchen/DATA_C/Project/HCPD/code/HCPD/Step2_dataprocess/Log/xcpd_log/job.%j.out
#SBATCH -e /home/cuizaixu_lab/fanqingchen/DATA_C/Project/HCPD/code/HCPD/Step2_dataprocess/Log/xcpd_log/job.%j.error.txt

#my_array=('sub-HCD2239247' 'sub-HCD2804151' 'sub-HCD1880465' 'sub-HCD1854767' 'sub-HCD1871969' 'sub-HCD2203933' 'sub-HCD1880162' 'sub-HCD2240030' 'sub-HCD1783366' 'sub-HCD2828569' 'sub-HCD1847972' 'sub-HCD2795479' 'sub-HCD1765970' 'sub-HCD2810954' 'sub-HCD2884377' 'sub-HCD2229547' 'sub-HCD2797584' 'sub-HCD2820351' 'sub-HCD1778474' 'sub-HCD2807460' 'sub-HCD1852056' 'sub-HCD2811552' 'sub-HCD2903759' 'sub-HCD2855875' 'sub-HCD2236140' 'sub-HCD2207840' 'sub-HCD2220428' 'sub-HCD1863465' 'sub-HCD2884175' 'sub-HCD1796577' 'sub-HCD1845160' 'sub-HCD2174649' 'sub-HCD2254243' 'sub-HCD2832863' 'sub-HCD2863975' 'sub-HCD2860262' 'sub-HCD2901654' 'sub-HCD2879788' 'dataset_description.json' 'sub-HCD2264549' 'sub-HCD1886275' 'sub-HCD2801852' 'sub-HCD2833461' 'sub-HCD1794977' 'sub-HCD2164242' 'sub-HCD1791163' 'sub-HCD2256651' 'sub-HCD2211932' 'sub-HCD1801140' 'sub-HCD1855365' 'sub-HCD2856170' 'sub-HCD2163644' 'sub-HCD1856468' 'sub-HCD2897184' 'sub-HCD1762661' 'sub-HCD1787677' 'sub-HCD1785572' 'sub-HCD2864270' 'sub-HCD1870159' 'sub-HCD2878382' 'sub-HCD1778070' 'sub-HCD1872971' 'sub-HCD1881164' 'sub-HCD2181848' 'sub-HCD1886477' 'sub-HCD2812352')
#for fruit in "${my_array[@]}"
#do
#  echo "$fruit"
#  sbatch makemaskref.sh $fruit
#done

#--HCPD--
#for file in $(ls /home/cuizaixu_lab/fanqingchen/DATA_C/data/HCPD/fmriprep_rest_no_MSM); do
#	echo $file;
#  sbatch makemaskref.sh $file
#done

#--HCP--
for file in $(ls /home/cuizaixu_lab/fanqingchen/DATA_C/data/HCP/fmriprep_REST1_NMSM); do
	echo $file;
  sbatch makemaskref.sh $file
done