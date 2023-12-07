#!/bin/bash
#PBS -N admix
#PBS -q seriallong
#PBS -P CBBI0818
#PBS -l select=1:ncpus=12
#PBS -l walltime=144:00:00
module add chpc/gnu/parallel-20160422

cd /mnt/lustre/groups/CBBI0818/PRISKA/POP_GEN/PCA/

IFS=" "
SUB_JOBS=""

for K in 3 4 5 6 7
do
        SUB_JOBS="${SUB_JOBS}
${K}"
done
echo ${SUB_JOBS}
echo "${SUB_JOBS}" | parallel --tmpdir /mnt/lustre/groups/CBBI0818/PRISKA/TMP/ -j 10 -u --sshloginfile ${PBS_NODEFILE} --col-sep ' ' '. /mnt/lustre/groups/CBBI0818/PRISKA/config.txt;K={1}; . /mnt/lustre/groups/CBBI0818/PRISKA/POP_GEN/PCA/admixture.sh'
