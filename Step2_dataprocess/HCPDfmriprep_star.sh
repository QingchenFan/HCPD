#!/bin/bash
#SBATCH --job-name=fanqingchen
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=3
#SBATCH --mem-per-cpu 8G
#SBATCH -p q_cn
#SBATCH -o /home/cuizaixu_lab/fanqingchen/DATA_C/Res/fmriprep/job.%j.out
#SBATCH -e /home/cuizaixu_lab/fanqingchen/DATA_C/Res/fmriprep/job.%j.error.txt

#for file in $(ls /ibmgpfs/cuizaixu_lab/fanqingchen/data/HCP/fmriprep_REST1_NMSM); do
#	echo "${file: 4: 10}";
#	sbatch HCPDfmriprepT1w.sh ${file: 4: 10}
#done

# 漏网之鱼
#my_array=('sub-HCD1196553' 'sub-HCD1723651' 'sub-HCD1609148' 'sub-HCD1656359' 'sub-HCD1514945' 'sub-HCD1215632' 'sub-HCD1543851' 'sub-HCD1168245' 'sub-HCD1496767' 'sub-HCD1633751' 'sub-HCD1756060' 'sub-HCD1610436' 'sub-HCD1685164' 'sub-HCD1502635' 'sub-HCD1681257' 'sub-HCD1237844' 'sub-HCD1131222' 'sub-HCD1701338' 'sub-HCD1162334' 'sub-HCD1156036' 'sub-HCD1197757' 'sub-HCD1565356' 'sub-HCD1647863' 'sub-HCD1686267' 'sub-HCD1493761' 'sub-HCD1411632' 'sub-HCD1363546' 'sub-HCD1504437' 'sub-HCD1757062' 'sub-HCD1223934' 'sub-HCD1435646' 'sub-HCD1578365'  'sub-HCD1612844' 'sub-HCD1410933' 'sub-HCD1646154' 'sub-HCD1239343' 'sub-HCD1262136' 'sub-HCD1664762' 'sub-HCD1518448' 'sub-HCD1205326' 'sub-HCD1534244' 'sub-HCD1490048' 'sub-HCD1594767' 'sub-HCD1231832' 'sub-HCD1411935' 'sub-HCD1400728' 'sub-HCD1433743' 'sub-HCD1571351' 'sub-HCD1658969' 'sub-HCD1612238' 'sub-HCD1663053' 'sub-HCD1491252' 'sub-HCD1187653' 'sub-HCD1756262' 'sub-HCD1714852' 'sub-HCD1227740' 'sub-HCD1643855' 'sub-HCD1396662' 'sub-HCD1522338' 'sub-HCD1129235' 'sub-HCD1111822' 'sub-HCD1590860' 'sub-HCD1409342')
my_array=('sub-171734' 'sub-822244' 'sub-159845' 'sub-150423' 'sub-117728' 'sub-145531' 'sub-165234' 'sub-239136' 'sub-142424' 'sub-552544' 'sub-734247' 'sub-171128' 'sub-107220' 'sub-201717' 'sub-114924' 'sub-953764' 'sub-623137' 'sub-121315' 'sub-190132' 'sub-109325' 'sub-209531' 'sub-113417' 'sub-613235' 'sub-221218' 'sub-662551' 'sub-121820' 'sub-186949' 'sub-128329' 'sub-689470' 'sub-129533' 'sub-169141')
for fruit in "${my_array[@]}"
do
  echo "${fruit: 4: 9}"
  sbatch HCPDfmriprepT1w.sh ${fruit: 4: 9}
done

#for file in $(ls /home/cuizaixu_lab/fanqingchen/DATA/data/HCPD/HCPD_BIDS); do
#	echo "${file: 7: 13}";
#	sbatch HCPDfmriprep.sh ${file: 7: 13}
#done
