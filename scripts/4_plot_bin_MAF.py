
import fileinput
import sys,os
import matplotlib.pyplot as plt
from matplotlib import cm

file1=sys.argv[1]
rows = {}

A = ["African_American","African_Caribbean","Afro_Arabs","Afro_Asiatic_Cushitic","Afro_Asiatic_Egyptic"]

B = ["Afro_Asiatic_Omotic","Afro_Asiatic_Semitic","Nilo_Saharan","Austroasiatic"]
C = ["Bantu_East","BantuSan","Bantu_South","Niger_Kordofanian","Mandinka"]

D =["Chimp","Denisova","Pygmy", "San","KhoeSan","Mongol","East_Asian"]
E = ["UK_Indian","USA_Indian", "European_center","European_North","European_South","European_USA"]

F = ["Indo_European","Latin_American","Maghreb","Neandertal","South_Africa_Coloured"]

PHENO = A + B + C + D + E + F

for line in fileinput.input(file1):
	data=line.split()
	if fileinput.lineno()>1:
		if data[0] in PHENO:
			rows[data[0]] = [float(j) for j in data[1:]]
	else:
		anc_av=[]
		header=data[1:]

print("\nNumber of Phenotype:",len(rows.keys()),len(A))

pos=[0.005, 0.1,0.25,0.50,0.75,1.0]

symbols = ["k","r","b","m","g","c","y"]
fig=plt.figure(2,dpi=150)

ax = fig.add_subplot(111) #plt.subplot(111)
ax.set_xlabel("Minor Allele Frequency Bin")
ax.set_ylabel("Proportion of MAF")
i  = 0;PHE=[]
a=0;b=0;c=0;d=0;e=0

for p in PHENO:
	PHE.append(p)
	phe = rows[p]
	if p in A:
		px = A.index(p); col = symbols[px]
                ax.plot(pos,phe,linestyle='--',marker='x', color='r',linewidth=2)
	elif p in B:
		px = B.index(p); col = symbols[px]
        	ax.plot(pos,phe,linestyle='--', marker='*', color='k',linewidth=2)
	elif p in C:
		px = C.index(p); col = symbols[px]
                ax.plot(pos,phe,linestyle='--', marker='+', color='b',linewidth=2)

	elif p in D:
                px = D.index(p); col = symbols[px]
                ax.plot(pos,phe,linestyle='--', marker='<', color='g',linewidth=2)
        elif p in E:
                px = E.index(p); col = symbols[px]
                ax.plot(pos,phe,linestyle='--', marker='>', color='m',linewidth=2)
	elif p in F:
		px = F.index(p); col = symbols[px]
		ax.plot(pos,phe,linestyle='--', marker='>', color='c',linewidth=2)
	else:
		print(p)	

plt.xticks([0.005, 0.1,0.25,0.50,0.75,1.0],['0-0.05', '>0.05-0.1', '>0.1-0.2', '>0.2-0.3', '>0.3-0.4', '>0.4-0.5'])

plt.grid(True)
plt.tick_params(labelsize=8)

box = ax.get_position()
ax.set_position([box.x0, box.y0 + box.height * 0.4,box.width, box.height * 0.7])
ax.legend(("African American","African Caribbean","Afro Arabs","Cushitic","Egyptic","Omotic","Semitic","Nilo-Saharan","Austroasiatic","Bantu East","BantuSan","Bantu South","Niger Kordofanian","Mandinka","Chimp","Denisova","Pygmy", "San","KhoeSan","Mongol","East Asian","UK Indian","USA Indian", "European center","European North","European South","European USA","Indo-European","Latin American","Maghreb","Neandertal","South Africa Coloured"),loc='upper center', bbox_to_anchor=(0.5, -0.09),fancybox=True, shadow=True, ncol=4,fontsize='x-small',labelspacing=0.1,columnspacing=0.2)
fig.savefig(sys.argv[2])
