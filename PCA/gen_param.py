import fileinput,os,sys

pop = sys.argv[1]

file1 ="/mnt/lustre/groups/CBBI0818/PRISKA/POP_GEN/PCA/"+pop+".par"
p="/mnt/lustre/groups/CBBI0818/PRISKA/POP_GEN/PCA/"

fin = open(file1,"wt")
param ='''genotypename:   %s%s.ped
snpname:        %s%s.map
indivname:      %s%s.pedind
poplistname:    %s%s
evecoutname:    %s%s.evec
evaloutname:    %s%s.eval
phylipoutname:  %s%s.fst
numoutlieriter: 0
outlieroutname: %s%s.out
altnormstyle: NO
familynames: NO
missingmode: NO
nsnpldregress: 0
noxdata: YES
nomalexhet: YES'''%(p,pop,p,pop,p,pop,p,pop,p,pop,p,pop,p,pop,p,pop)
fin.write(param)
fin.close()

out="/mnt/lustre/groups/CBBI0818/PRISKA/POP_GEN/PCA/"+pop+".log"

soft="/mnt/lustre/groups/CBBI0818/PRISKA/POP_GEN/PCA/smartpca"

srun = soft+" "+"-p"+" "+file1+" "+">"+" "+out
print(srun)
os.system("cd /mnt/lustre/groups/CBBI0818/PRISKA/POP_GEN/PCA/")
os.system(srun)

#ind="python"+" "+"/mnt/lustre/groups/CBBI0818/PRISKA/POP_GEN/PCA/cut_ind.py"+" "+p+pop+".evec"+" "+p+pop+".ind"
#os.system(ind)

