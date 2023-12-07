#!/bin/bash
#PBS -N admix
#PBS -q seriallong
#PBS -P CBBI0818
#PBS -l select=1:ncpus=12
#PBS -l walltime=144:00:00
#PBS -m abe -M thmpri004@myuct.ac.za

. /mnt/lustre/groups/CBBI0818/PRISKA/config.txt

cd /mnt/lustre/groups/CBBI0818/PRISKA/POP_GEN/PCA/


K=3
### you can submit (qsub admixture.sh this by fixing a K eg. K=4 etc or comment as it is and qsub qsub_qdmixture.sh


data=/mnt/lustre/groups/CBBI0818/PRISKA/POP_GEN/PCA/

###${plink} --file ${data}MERGED_reduced --threads 8 --maf 0.05 --geno 0.10 --hwe 0.01 --recode12 --out ${data}MERGED3

##new criteria ###
#${plink} --file ${data}MERGED_reduced --threads 8 --maf 0.05 --geno 0.02 --hwe 0.0001 --recode12--out ${data}MERGED4

#${plink} --file ${data}MERGED4 --indep-pairwise 1000 50 0.15 --out ${data}indepSNP

#${plink} --file ${data}MERGED4 --extract ${data}indepSNP.prune.in --genome --min 0.2 --out ${data}pihat_min0.2
#not sure whats going on in the output file will therefore skip this step

#${plink} --file ${data}MERGED4 --extract ${data}indepSNP.prune.in --make-bed --out ${data}MERGED_pruned

#${plink} --bfile ${data}MERGED_pruned --recode --out ${data}MERGED_pruned

## best proxies ###
${plink} --bfile ${data}MERGED_pruned --keep ${data}k3_ind_fam.txt --recode --out ${data}MERGED_bprox

## run admixture ###
${data}admixture -B ${data}MERGED_bprox.ped ${K}
${data}admixture --cv ${data}MERGED_bprox.ped ${K} | tee ${data}log${K}.MERGED_bprox.out



