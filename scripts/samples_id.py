import fileinput,os,sys

file1 = sys.argv[1]

fin = open(sys.argv[2],"wt")
rows ={}

for line in fileinput.input(file1):
	data = line.split()
	rows[data[5]] = []

lows =[ ]

for line in fileinput.input(file1):
	data = line.split()
	rows[data[5]].append(1)
print"\n",rows.keys()
step = 1
for des in rows:
	fin.write(des+"\t"+str(step)+"\n")
	step = step + 1
fin.close()
