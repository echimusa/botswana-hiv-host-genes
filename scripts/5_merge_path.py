import fileinput,os,sys,gzip
rows = {}
IND = []

disease=sys.argv[1]	# disease 
path2=sys.argv[2]	# Path to pathogenic proportion per Ethnic 


for path, subdirs, files in os.walk(path2+"PATH/"):
	for filename in files:
		IDX = files.index(filename)
		if "PATH" in filename:
			suffix ="_".join(filename.split(".")[:-2])
			IND.append(suffix)
			f = os.path.join(path, filename)
			for line in fileinput.input(f):
				data = line.split()
				if fileinput.lineno()>1:
					if data[0] in rows:
						T = rows[data[0]]; T.append(data[-1]);rows[data[0]]=T
					else:
						rows[data[0]]= [data[2],data[-1]]
fin = open(path2+disease+"_PATH.txt","wt")
fin.write("\t".join(["Gene","#SNPs"]+IND)+"\n")

F = []
for line in fileinput.input(sys.argv[3]):
	data = line.split()
	F.append(data[0])

for des in rows:
	if len(rows[des])== len(F)+1:			# Compare to total number of expected Ethnic groups
		fin.write("\t".join([des]+rows[des])+"\n")
	else:
		print(rows[des]);print([len(F),len(rows[des])])
		print("Missing pathogenic proportion from some Ethnic group !!.. Exiting..")
		os.system("rm "+ path+disease+"_PATH.txt")
		sys.exit(1)

fin.close()
