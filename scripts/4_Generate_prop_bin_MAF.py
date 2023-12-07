import fileinput,os,sys,gzip

### Receiving input ###



SNP = []
PHENO = {};RES={};

for line in fileinput.input(sys.argv[1]): # List of Ethnics
	data = line.split()
	RES[data[0]] = [data[0]]

path=sys.argv[2]  # Path to FRQ files	

for phe in RES:
	f = path+phe+".frq"					
	B1 = 0; B2=0 ; B3=0; B4=0;B5=0;B6=0
	T=0
	if os.path.isfile(f):
		for line in fileinput.input(f):
			data = line.split()
			if fileinput.lineno() > 1:
				T = T + 1
				if data[4] in ["NA","na","Na","---"," "]:
					pass
				else:	
					if float(0.0) <= float(data[4]) <= 0.05:			
						B1 = B1+ 1
					elif 0.05 < float(data[4]) <= 0.1:
						B2 = B2+ 1
					elif 0.1 < float(data[4]) <= 0.2:
						B3 = B3+ 1
					elif 0.2 < float(data[4]) <= 0.3:
						B4 = B4+ 1
					elif 0.30 < float(data[4]) <= 0.4:
						B5 = B5+ 1
					elif 0.4 < float(data[4]) <= 0.5:
						B6 = B6+ 1
  		Z = RES[phe];Z = Z+[str(float(B1)/T),str(float(B2)/T),str(float(B3)/T),str(float(B4)/T),str(float(B5)/T),str(float(B6)/T)];RES[phe] = Z
		#print(Z)
	else:
		print("The script aborted as the file %s does not exist"%f)
		sys.exit(1)
fin = open(path+"FRQ_BINs.prop.txt","wt")
fin.write(" ".join(["Phenotypes","(0-0.005",">0.005-0.1",">0.1-0.2",">0.2-0.3",">0.3-0.4",">0.4-0.5)"])+"\n")

for p in RES:
	fin.write(" ".join(RES[p])+"\n")
fin.close()

