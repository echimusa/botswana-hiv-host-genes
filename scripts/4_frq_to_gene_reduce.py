import fileinput,sys,gzip
import numpy as np
rows = {}

path=sys.argv[1]	# Path to MAF files

FRQ = []

for line in fileinput.input(sys.argv[2]):  ### file containing list of Ethnics
	data=line.split()
	FRQ.append(data[0])


fin=open(sys.argv[3],"wt")

Gene = {};Gene1 = {}
for line in fileinput.input(sys.argv[4]):
	data = line.split()
	Gene[data[0].lower()]=[data[0]]

for line in fileinput.input(sys.argv[5]):
        data = line.split()
        if fileinput.lineno()>1:
                if data[-1].lower() in Gene:
                        tmp = Gene[data[-1].lower()] ### position
			if data[2].startswith("rs"):
                        	tmp.append(data[2])
                        	Gene[data[-1].lower()] = tmp
LOWS = {}
G = Gene.values()


for  des in G:
	T = []
	for snp in des[1:]:
		tmp = []
	
DATA = {}

for filename in FRQ:
	for line in fileinput.input(path+filename+".frq"):
		data=line.split()
		#print(filename)
		if fileinput.lineno()>1:
			if data[4] in ["NA","na","nan","---","--"]:
				pass
			else:
				snp = data[1]
				if snp in DATA:
					tp = DATA[snp];tp.append(float(data[4]))
					DATA[snp]=tp
				else:
					if snp in ["NA","na","---","."]:
						print("NA") #pass
					else:
						DATA[snp] = [float(data[4])]
DATA1 = {}

for snp in DATA:
	print([len(DATA[snp]),len(FRQ)])
	if len(DATA[snp]) ==len(FRQ):
		DATA1[snp] = DATA[snp]
DATA.clear()

for des in G:
        T = []
        for snp in des[1:]:
		if snp in DATA1:
			T.append(DATA1[snp])			
		else:
			pass #rint(snp)
	LOWS[des[0].upper()] = T



DATA1.clear();G=[]

fin.write("\t".join(["Gene"]+FRQ)+"\n")

for gene in LOWS:
	if len(LOWS[gene]) != 0:
		if len(LOWS[gene])==len(FRQ):
			L = np.mean(LOWS[gene],axis=0,dtype=np.float64)
			fin.write("\t".join([gene]+[str(round(k,3)) for k in L])+"\n")
		else:
			L = np.mean(LOWS[gene],axis=0,dtype=np.float64)
			fin.write("\t".join([gene]+[str(round(k,3)) for k in L])+"\n")
	else:
		pass
fin.close()
