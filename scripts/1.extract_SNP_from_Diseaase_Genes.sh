#!/bin/sh
#PBS -N BREAST
#PBS -q serial
#PBS -P CBBI1039
#PBS -l select=1:ncpus=3
#PBS -l walltime=48:00:00

disease=BREAST

. /mnt/lustre/users/cboyd/${disease}/config.txt

python ${script}1_pos_map_db38.py ${data}${disease} ${dbsnp}dbsnp_138.hg19.vcf.gz \
${dbsnp}All_20180418.vcf.gz \
${data}${disease}.SNP_Gene.txt
cut -f3 ${data}${disease}.SNP_Gene.txt > ${data}SNP.txt

${plink} --bfile ${data1}SANGER_DRAKE --extract ${data}SNP.txt --make-bed --out ${data}SANGER_${disease}




