#!/bin/bash
#PBS -N SPLIT
#PBS -q serial
#PBS -P CBBI1039
#PBS -l select=1:ncpus=3
#PBS -l walltime=48:00:00


disease=BREAST
. /mnt/lustre/users/cboyd/${disease}/config.txt



###${data}${disease}.SNP_Gene.txt

#python ${script}4_frq_to_gene_reduce.py ${MAP} ${data}List_Ethnics.txt ${MAP}${disease}.gene.frq ${data}${disease} ${data}${disease}.SNP_Gene.txt 

if [ -f "${MAP}${disease}.gene.frq" ];then
	# Add list of gene separated by , or space or ; or in 1-column file as last parameter other it will use all genes
	python ${script}plot_anc_gene.py ${MAP}${disease}.gene.frq ${MAP}${disease}.gene_frq.png ${MAP}top_genes_consistent.txt
fi
