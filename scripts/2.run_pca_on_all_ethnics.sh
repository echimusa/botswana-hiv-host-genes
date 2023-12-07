#!/bin/sh
#PBS -N pca
#PBS -q serial
#PBS -P CBBI1039
#PBS -l select=1:ncpus=12
#PBS -l walltime=48:00:00

disease=BREAST

. /mnt/lustre/users/cboyd/${disease}/config.txt


#${plink} --bfile ${data}SANGER_${disease} --indep-pairwise 1000 50 0.15 --out ${data}indepSNP

#${plink} --bfile ${data}SANGER_${disease} --extract ${data}indepSNP.prune.in --genome --min 0.2 --out ${data}pihat_min0.2

#${plink2} --make-bed --out ${data}SANGER_${disease}.2 --bfile ${data}SANGER_${disease} --maf 0.05 --autosome --snps-only just-acgt --max-alleles 2 --rm-dup exclude-all

${plink} --bfile ${data}SANGER_${disease} --hwe 0.00001 --maf 0.05 --recode12 --out ${data}SANGER_${disease}


python ${soft}samples_id.py ${data}SANGER_${disease}.pedind ${PCA}SANGER_${disease}
python ${soft}gen_param.py ${data} SANGER_${disease} ${PCA}


## PLOTTING PCA using R script


if [  -f ${PCA}SANGER_${disease}.evec ];then
	#if [ -f ${PCA}SANGER_${disease}.fst ]; then
	Rscript ${script}2_plot_smartpca.R ${PCA}SANGER_${disease}.eval ${PCA}SANGER_${disease}.evec ${PCA}SANGER_${disease}.pdf	
	#fi
fi

