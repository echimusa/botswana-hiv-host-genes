#!/bin/bash
#PBS -N SPLIT
#PBS -q serial
#PBS -P CBBI1039
#PBS -l select=1:ncpus=3
#PBS -l walltime=48:00:00


disease=BREAST
. /mnt/lustre/users/cboyd/${disease}/config.txt




python ${script}5_merge_path.py ${disease} ${ANNOT} ${data}List_Ethnics.txt

#if [ -f "${ANNOT}${disease}_PATH.txt" ];then
#	# Add list of gene separated by , or space or ; or in 1-column file as last parameter other it will use all genes
	#python ${script}5_plot_ethnics_path.py ${ANNOT}${disease}_PATH.txt ${ANNOT}${disease}_PATH.png  
	python ${script}plot_anc_gene.py ${ANNOT}BREAST_PATH.txt ${ANNOT}BREAST_PATH.png ${MAP}top_genes_consistent.txt
#fi
