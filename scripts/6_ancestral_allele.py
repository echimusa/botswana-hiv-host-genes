import fileinput,os,sys,gzip

### Receiving input ###
print(sys.argv[1:])
pheno=sys.argv[1]  # phenotype suffix
path=sys.argv[2] # path to signinificant SNPS per pheno
out=sys.argv[3] # Output folder Sig SNPs annotated based ancestral/derived allele
evan=sys.argv[4]
MAF=sys.argv[5]
SNP = {}

for line in fileinput.input(sys.argv[-1]):
	data = line.split()
	SNP[data[0]] = data[0]
						
SIG_SNP = {}

for line in fileinput.input(evan): # Ancestral allele compilation from Evan
        data = line.split()
        if fileinput.lineno() > 1:
                if data[0] in SNP:
			SIG_SNP[data[0]] = [data[2]+data[3]]


#print("writing to"+out+"SIG_SNP_ANNOT."+pheno)

fin = open(out+"SIG_SNP_ANNOT."+pheno,"wt")

fin.write(" ".join(["SNP","A1/A2","REF/Minor","MAF"])+"\n")

for line in fileinput.input(MAF): # Ancestral allele compilation from Evan
        data = line.split()
	if fileinput.lineno()>1:
		if data[1] in SNP: 
			if data[1] in SIG_SNP:
				G = SIG_SNP[data[1]]
				G  = G + [data[2]+data[3],data[4]]
				SIG_SNP[data[1]] = G
		#elif data[1] in SNP:
		#	SIG_SNP[data[1]] = ["--",data[3]+data[4],data[5]]

#for snp in SNP:
#        if snp in SIG_SNP:
#                pass
#        else:
#               print("Missing %s"%snp) # SIG_SNP[snp] = ["--","--","--"]

SNP = {}
for snp in SIG_SNP:
	fin.write(" ".join([snp]+SIG_SNP[snp])+"\n")
fin.close()
SIG_SNP ={}
