import fileinput,os,sys

fi=open(sys.argv[2],"wt")
ANC=sys.argv[3]
rows = []

M=["Gene.refGene","ExAC_ALL","ExAC_AFR","ExAC_AMR","ExAC_EAS","ExAC_FIN","ExAC_NFE","ExAC_OTH","ExAC_SAS"]  #,"InterVar_automated"]


GENE = {}
#Likely_pathogenic Likely_benign

Gene = sys.argv[4]   # List of disease-specific genes

for line in fileinput.input(Gene):
	data =line.split()
	GENE[data[0]] = [0.0,0.0,0.0]

for line in fileinput.input(sys.argv[1]):		# Annotated VCF file
	data = line.split()
	if line.startswith("#"):
		pass
	else:
		DES = data[7].split(";")
		B=DES[5].split("=")
		tmp = []
		for m in M:
			for du in DES:
				if du.startswith(m):
					g = du.split("=")
					if len(g)>1:
						tmp.append(g[1])
					else:
						tmp.append(g[0])
		N = tmp[2:].count("."); L  = len(tmp[2:])
		if tmp[0] in GENE:
			T = GENE[tmp[0]]; T[1] = T[1]+1; GENE[tmp[0]] = T
			if N ==0 or N != L:
				T = GENE[tmp[0]]; T[0] = T[0] +1; GENE[tmp[0]] = T
		else:
			if "\\x3b" in tmp[0]:
				Z = tmp[0].split("\\x3b")
				for g in Z:
					if g in GENE:
						T = GENE[g]; T[1] = T[1]+1; GENE[g] = T
						if N ==0 or N != L :
							T = GENE[g]; T[0] = T[0] +1; GENE[g] = T
fi.writelines("GENE"+"\t"+"#Polymorphisms_Pathogenicn"+"\t"+"#SNPs"+"\t"+"%SNPs_with_P"+"\n")
print("OK")
#Likely_pathogenic, Benign, Pathogenic
for gene in GENE:
	if float(GENE[gene][1]) in [0.0, 0,"0.0","0"]:
		fi.write("\t".join([gene,str(GENE[gene][0]),str(GENE[gene][1]),str(0.0) ])+"\n")
	else:
        	fi.write("\t".join([gene,str(GENE[gene][0]),str(GENE[gene][1]),str(round(100*(float(GENE[gene][0])/float(GENE[gene][1])),3)) ])+"\n")
fi.close()

print("End")

