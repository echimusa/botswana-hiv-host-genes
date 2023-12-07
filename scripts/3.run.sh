#!/bin/bash
#PBS -N ANNOT
#PBS -q serial
#PBS -P CBBI1039
#PBS -l select=1:ncpus=12
#PBS -l walltime=48:00:00

disease=BREAST
. /mnt/lustre/users/cboyd/${disease}/config.txt

ANC=San

ANNOVAR_ANNOT=${annovar}
humandb=${ANNOVAR_ANNOT}humandb/
ANN=${ANNOVAR_ANNOT}

data1=${ANNOT}${ANC}.vcf
out2=${ANNOT}${ANC}

if [ ! -f ${data}${ANC} ];then
    grep ${ANC} ${data}SANGER_${disease}.pedind | cut -f1,2 > ${data}${ANC} 						# Extract 2 first columns of all inviduals from an Ethnic
fi

if [ ! -f "${ANNOT}${ANC}.vcf" ];then
${plink} --bfile ${data}SANGER_${disease} --keep ${data}${ANC} --make-bed --out ${data}${ANC} --threads 8 	# Extract data for individual for a specific Ethnic
${plink} --bfile ${data}${ANC} --freq --out ${MAP}${ANC} --threads 8						# Write MAF output for each Ethnic to MAP folder
${plink} --bfile  ${data}${ANC} --recode vcf --out  ${ANNOT}${ANC} --threads 8 					# Write VCF file foreach Ethnic to ANNOT folder

perl ${ANN}table_annovar.pl ${data1} ${humandb} -buildver hg19 -out ${out2} -remove -protocol refGene,exac03,avsnp147,dbnsfp30a,1000g2014oct_all,1000g2014oct_afr,1000g2014oct_eas,1000g2014oct_eur,ljb26_all -operation g,f,f,f,f,f,f,f,f -nastring . -vcfinput


rm ${ANNOT}${ANC}.hg19_multianno.txt ${ANNOT}*.log ${ANNOT}*.nosex ${ANNOT}*.avinput

elif [ -f "${ANNOT}${ANC}.vcf" ];then
	if [ ! -f "${ANNOT}${ANC}.hg19_multianno.vcf" ];then
	    echo 'EMILE ALL IS GREAT .....!'
	    perl ${ANN}table_annovar.pl ${data1} ${humandb} -buildver hg19 -out ${out2} -remove -protocol refGene,exac03,avsnp147,dbnsfp30a,1000g2014oct_all,1000g2014oct_afr,1000g2014oct_eas,1000g2014oct_eur,ljb26_all -operation g,f,f,f,f,f,f,f,f -nastring . -vcfinput

            #rm ${ANNOT}${ANC}.hg19_multianno.txt ${ANNOT}*.log ${ANNOT}*.nosex ${ANNOT}*.avinput
	else
		data1=${ANNOT}${ANC}.vcf;out2=${ANNOT}${ANC}
		echo "DONE@@@@@@@@@@@@@@"
               # rm ${ANNOT}${ANC}.hg19_multianno.txt ${ANNOT}*.log ${ANNOT}*.nosex ${ANNOT}*.avinput
        fi

fi
