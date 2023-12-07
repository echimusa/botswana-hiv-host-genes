#!/bin/sh
#PBS -N PCA_ALL
#PBS -q serial
#PBS -P CBBI0818
#PBS -l select=1:ncpus=3
#PBS -l walltime=48:00:00
#PBS -m abe -M alssha003@myuct.ac.za

. /mnt/lustre/groups/CBBI0818/PRISKA/config.txt

soft=/mnt/lustre/groups/CBBI0818/PRISKA/POP_GEN/PCA/

data=/mnt/lustre/groups/CBBI0818/PRISKA/POP_GEN/PCA/

cd ${soft}

#${plink} --bfile ${soft}MERGED2 --recode12 --out ${data}MERGED2
#cp ${soft}MERGED.pedind ${soft}MERGED2.pedind
python ${soft}samples_id.py ${soft}MERGED_reduced.pedind ${data}MERGED_reduced
python ${soft}gen_param.py MERGED_reduced


