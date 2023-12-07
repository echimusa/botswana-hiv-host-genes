#!/bin/bash
#PBS -N SPLIT
#PBS -q serial
#PBS -P CBBI1039
#PBS -l select=1:ncpus=3
#PBS -l walltime=48:00:00

disease=BREAST
. /mnt/lustre/users/cboyd/${disease}/config.txt

anot=${ANNOT}${ANC}.hg19_multianno.vcf

soft=${script}5_special.py

if [ ! -d "${ANNOT}PATH/" ]; then
        mkdir ${ANNOT}PATH/
        chmod 777 -R ${ANNOT}PATH/
fi
python ${soft} ${anot} ${ANNOT}PATH/${ANC}.PATH.txt ${ANC} ${data}${disease}
