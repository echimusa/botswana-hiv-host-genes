#!/bin/bash
#PBS -N SPLIT
#PBS -q serial
#PBS -P CBBI1039
#PBS -l select=1:ncpus=3
#PBS -l walltime=48:00:00


disease=BREAST
. /mnt/lustre/users/cboyd/${disease}/config.txt


#python ${script}4_Generate_prop_bin_MAF.py ${data}List_Ethnics.txt ${MAP}  


if [ -f ${MAP}FRQ_BINs.prop.txt ];then
	python ${script}4_plot_bin_MAF.py ${MAP}FRQ_BINs.prop.txt ${MAP}FRQ_BINs.${disease}.png 
else
	echo 'The program aborted as the file ${MAP}FRQ_BINs.prop.txt does exit!'
fi

