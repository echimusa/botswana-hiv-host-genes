import fileinput,sys,os,gzip

fin = open(sys.argv[4],"wt")

rows = {}
GENE = {}
for line in fileinput.input(sys.argv[1]): # 1 column file list of disease genes 
        data = line.split()
	GENE[data[0]] =data[0]	

fin.write("\t".join(["CHR","POS","SNP","GENE"])+"\n")
for line in gzip.open(sys.argv[2]): # dbsnp hg19 file
	data = line.split()
	if data[0].startswith("#"):
		pass
	else:
		gene="NA"
		F= data[7].split(";")
		for des in F:
			if des.startswith("GENEINFO"):
				gene = des.split("=")[1].split(":")[0]
		if gene in GENE:
			fin.write("\t".join([data[0],data[1],data[2],gene])+"\n")
			rows[data[2]] = data[2]

for line in gzip.open(sys.argv[3]): # dbsnp hg38 file:
        data = line.split()
        if data[0].startswith("#"):
                pass
        else:
                gene="NA"
                F= data[7].split(";")
                for des in F:
                        if des.startswith("GENEINFO"):
                                gene = des.split("=")[1].split(":")[0]
                if gene in GENE:
			if data[2] in rows:
				pass
			else:
				fin.write("\t".join([data[0],data[1],data[2],gene])+"\n")
				rows[data[2]] = data[2]
fin.close()
