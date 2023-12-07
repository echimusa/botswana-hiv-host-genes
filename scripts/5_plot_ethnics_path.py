import fileinput
import pylab,sys,os
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np

import matplotlib.ticker as ticker

rows = []

import math as mt


AFRO = ["African_American","African_Caribbean","Afro_Arabs","Afro_Asiatic_Cushitic","Afro_Asiatic_Egyptic"]
ASN = ["Afro_Asiatic_Omotic","Afro_Asiatic_Semitic","Nilo_Saharan","Austroasiatic"]
AFR = ["Bantu_East","BantuSan","Bantu_South","Niger_Kordofanian","Mandinka"]
CHIP =["Chimp","Denisova","Pygmy", "San","KhoeSan","Mongol","East_Asian"]
EUR = ["UK_Indian","USA_Indian", "European_center","European_North","European_South","European_USA"]
IND = ["Indo_European","Latin_American","Maghreb","Neandertal","South_Africa_Coloured"]


SNP = [];LOWS = {}
if len(sys.argv[1:])==3:
	sub_gene = []
	if os.path.isfile(sys.argv[3]):
		for lin in fileinput.input(sys.argv[3]):
			data = line.split()
			sub_gene.append(data[0])
	else:
		if ',' in sys.argv[3]:
			sub_gene = sys.argv[3].split(',')
		elif ';' in sys.argv[3]:
			sub_gene = sys.argv[3].split(';')
		else:
			sub_gene = sys.argv[3].split()

A = AFRO+ASN+CHIP+AFR+EUR+IND
	
for i in range(len(AFRO+ASN+CHIP+AFR+EUR+IND)):
	rows.append([])


for line in fileinput.input(sys.argv[1]):  # Merged pathogenic proportion for all Ethnics
	data=line.split()
	if fileinput.lineno()>1:
		SNP.append(data[0].strip('"').strip('"'))
		if len(sys.argv[1:])==3:
			if data[0] in sub_gene:
				LOWS[data[0]] = [float(data[2])]+data[2:]
		else:
			LOWS[data[0]] = [float(data[2])]+data[2:]
	else:
		B = data[2:]
pos = range(2,len(LOWS)+2)
pos = np.array(pos)+2.5
pos = list(pos)

L = LOWS.values()
L = sorted(L, key = lambda x: (x[0]))	

for des in L:
	T = des[1:]
	for j in range(len(A)):
		rows[j].append(float(T[j])) #;rows[].append(float(des[3]))


B = [d.strip('"').strip('"') for d in B]
symbols =["*",".","<","+","x","d","1","4","s"] 

#['p','H','D','o','^','v','<','>','s','+','x','D','d','1','2','3','4','h','H','p','o','^','v','<','>','s','1']#'-','--','-.',':','.',',',
#lps = [k+'-' for k in [',','.','o','^','v','<','>','s','+','x','D','d','1','2','3','4','h','H','p']]

colors= ['k','g','r','b','m','y','k','c','b','g','r','c','m','xy','k','w','b','g','r','c','m','y','k',"b"]


fig=plt.figure(2,dpi=150)
ax = fig.add_subplot(111) #plt.subplot(111)
fig.subplots_adjust(bottom=0.1)
fig.set_size_inches(17,11)
#ax.margins(x=2)
#ax.set_xlabel("SNPs")
ax.set_ylabel("log2 % Pathogenic SNPs within Gene")
s=9.9871

xs = np.array([5.79843965218024 for i in xrange(len(pos))])
i  = 0;PHE=[]

for phe in rows:
	idx = rows.index(phe)
	p = B[idx]
	#phe.sort()
	phe = np.asarray(phe) +1.0
	pos = np.asarray(pos)

	if p in AFR:
		px = AFR.index(p); col = 'g'+symbols[px]
		ax.plot(pos,phe,col,linewidth=3)
	elif p in EUR:
		px = EUR.index(p); col = 'b'+symbols[px]
		ax.plot(pos,phe,col,linewidth=3)
	elif p in ASN:
		px = ASN.index(p); col = 'r'+symbols[px]
		ax.plot(pos,phe,col,linewidth=3)
	elif p in AFRO:
		px = AFRO.index(p); col = 'm'+symbols[px]
		ax.plot(pos,phe,col,linewidth=3)
	elif p in IND:
		px = IND.index(p); col = 'k'+symbols[px]
		ax.plot(pos,phe,col,linewidth=3)
	elif p in CHIP:
		px = CHIP.index(p); col = 'c'+symbols[px]
		ax.plot(pos,phe,col,linewidth=3)
	else:
		print(p)
	i = i +1

y=rows[-1]
plt.xticks(pos,SNP,rotation=45)
ax.set_yscale('log', basey=2)

#ax.yaxis.set_major_locator(ticker.FixedLocator(rows[0]))
#ax.yaxis.set_major_locator(ticker.MultipleLocator(0.5))
plt.grid(True)
plt.tick_params(labelsize=12)
#plt.margins(1.09)
box = ax.get_position()

ax.set_position([box.x0, box.y0 + box.height * 0.5,box.width, box.height * 0.8])

ax.legend(("African American","African Caribbean","Afro Arabs","Cushitic","Egyptic","Omotic","Semitic","Nilo-Saharan","Austroasiatic","Bantu East","BantuSan","Bantu South","Niger Kordofanian","Mandinka","Chimp","Denisova","Pygmy", "San","KhoeSan","Mongol","East Asian","UK Indian","USA Indian", "European center","European North","European South","European USA","Indo-European","Latin American","Maghreb","Neandertal","South Africa Coloured"),loc='upper center', bbox_to_anchor=(0.5, -0.09),fancybox=True, shadow=True, ncol=4,fontsize='x-small',labelspacing=0.1,columnspacing=0.2)


fig.savefig(sys.argv[2])
