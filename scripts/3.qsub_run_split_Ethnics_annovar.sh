#!/bin/bash
#PBS -N ANNOT
#PBS -q seriallong
#PBS -P CBBI1039
#PBS -l select=1:ncpus=12:mpiprocs=24
#PBS -l walltime=144:00:00


module add chpc/gnu/parallel-20160422

IFS=" "
SUB_JOBS=""


while read line
 do
    if [[ $line != start* ]]
       then
           ((g++))
           IFS=" "
           set -- $line
           datas=( $line )
SUB_JOBS="${SUB_JOBS}
${datas[0]}"
   fi
done</mnt/lustre/users/cboyd/BREAST/DATA/List_Ethnics.txt

echo "${SUB_JOBS}"
echo "${SUB_JOBS}" | parallel -j 6 -u --temp /mnt/lustre/users/cboyd/BREAST/TMP/ --sshloginfile ${PBS_NODEFILE} --col-sep ' ' '. /mnt/lustre/users/cboyd/BREAST/config.txt;ANC={1} . /mnt/lustre/users/cboyd/BREAST/scripts/3.run_split_Ethnics_annovar.sh'



