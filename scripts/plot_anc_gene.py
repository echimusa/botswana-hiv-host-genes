import fileinput
import pylab,sys,os
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
disease="CSL"
import matplotlib.ticker as ticker
#CUT = int(sys.argv[2])

rows = []

import math as mt

A1 = ["African_American","African_Caribbean","Latin_American"]
B = ["Chimp","Denisova","Neandertal","Pygmy","San","KhoeSan","Mongol"]
C =["Afro_Arabs","Austroasiatic","Afro_Asiatic_Cushitic","Afro_Asiatic_Egyptic","Afro_Asiatic_Omotic","Afro_Asiatic_Semitic"]
D = ["European_center","European_North","European_South","European_USA","Indo_European"]
E = ["Mandinka","Niger_Kordofanian","Nilo_Saharan","Bantu_East","BantuSan","Bantu_South"]
F = ["Maghreb","South_Africa_Coloured", "East_Asian","UK_Indian","USA_Indian"]


#A = E + D+ B+ A1 + F + C

A = ["Mandinka","Niger_Kordofanian","Nilo_Saharan","Bantu_East","BantuSan","Bantu_South","European_center","European_North","European_South","European_USA","Indo_European","Chimp","Denisova","Neandertal","Pygmy","San","KhoeSan","Mongol","African_American","African_Caribbean","Latin_American","Maghreb","South_Africa_Coloured", "East_Asian","UK_Indian","USA_Indian","Afro_Arabs","Austroasiatic","Afro_Asiatic_Cushitic","Afro_Asiatic_Egyptic","Afro_Asiatic_Omotic","Afro_Asiatic_Semitic"]

AFR = E
EUR = D
CHIP = B
ASN = A1
IND = F
AFRO = C
 
SNP = []
LOWS = {}

for i in range(len(A)):
	rows.append([])

if len(sys.argv[1:]) == 3:
	sub_gene = []
	if os.path.isfile(sys.argv[3]):
		for line in fileinput.input(sys.argv[3]):
			data = line.split()
			sub_gene.append(data[0])
	else:
		if ',' in sys.argv[3]:
			sub_gene = sys.argv[3].split(',')
		elif ';' in sys.argv[3]:
			sub_gene = sys.argv[3].split(';')
		else:
			sub_gene = sys.argv[3].split()

	for line in fileinput.input(sys.argv[1]):
		data = line.split()
		if fileinput.lineno() > 1:
			if data[0] in sub_gene:
				LOWS[data[0]] = [float(data[1])]+data[1:]
				SNP.append(data[0])
		else:
			B = data[1:]
else:	

	for line in fileinput.input(sys.argv[1]):
		data=line.split()
		if fileinput.lineno()>1:
			SNP.append(data[0]) 	
			LOWS[data[0]] = [float(data[1])]+data[1:]
	else:
		B = data[1:]
pos = range(2,len(LOWS)+2)
pos = np.array(pos)+2.5
pos = list(pos)

L = LOWS.values()
L = sorted(L, key = lambda x: (x[0]))	

for des in L:
	T = des[1:]
	for j in range(len(A)):
		rows[j].append(float(T[j])) #;rows[].append(float(des[3]))


#print(rows)
B = [d.strip('"').strip('"') for d in B]
#B = [ d.strip(disease+"_") for d in B]
####B = [ d[len(disease)+1:] for d in B]
symbols =["*",".","<","+","x","d","1","4","s"] 

#['p','H','D','o','^','v','<','>','s','+','x','D','d','1','2','3','4','h','H','p','o','^','v','<','>','s','1']#'-','--','-.',':','.',',',
#lps = [k+'-' for k in [',','.','o','^','v','<','>','s','+','x','D','d','1','2','3','4','h','H','p']]

colors= ['k','g','r','b','m','y','k','c','b','g','r','c','m','xy','k','w','b','g','r','c','m','y','k',"b"]

#pylab.legend(loc=9, bbox_to_anchor=(0.5, -0.1), ncol=2)

fig=plt.figure(2,dpi=150)
ax = fig.add_subplot(111) #plt.subplot(111)
fig.subplots_adjust(bottom=0.2)
fig.set_size_inches(17,11)
###ax.margins(x=0)
#ax.set_xlabel("SNPs")
ax.set_ylabel("Log2 Gene-specific in SNPs Frequencies")
s=9.9871
#import numpy as np
#print(B)

##symbols = ["k","r","b","m","g","c","y"]
xs = np.array([5.79843965218024 for i in xrange(len(pos))])
i  = 0;PHE=[]
#ax.plot(pos,xs,'r',linewidth=2)
TMP = []
for phe in rows:
	idx = rows.index(phe)
	p = B[idx]
	#phe.sort()
	phe = np.asarray(phe)+1.0
	pos = np.asarray(pos)
	#print([phe,len(pos),p])
	#raw_input("Stop")
	TMP.append(p)
	if p in AFR:
		px = AFR.index(p); col = 'g'+symbols[px]
		ax.plot(pos,phe,col,ls=('dashed'),lw=3)
	elif p in EUR:
		px = EUR.index(p); col = 'b'+symbols[px]
		ax.plot(pos,phe,col,linewidth=3)
	elif p in CHIP:
		px = CHIP.index(p); col = 'r'+symbols[px]
		ax.plot(pos,phe,col,linewidth=3)
	elif p in AFRO:
		px = AFRO.index(p); col = 'm'+symbols[px]
		ax.plot(pos,phe,col,linewidth=3)
	elif p in ASN:
		px = ASN.index(p); col = 'c'+symbols[px]
		ax.plot(pos,phe,col,linewidth=3)
	elif p in IND:
		px = IND.index(p); col = 'k'+symbols[px]
		ax.plot(pos,phe,col,linewidth=3)
	else:
		pass #print(p)
	i = i +1

##print(TMP)
##raw_input("E")
y=rows[-1]
plt.xticks(pos,SNP,rotation=45)
#ax.set_yscale('log')

ax.set_yscale('log', basey=2)

#ax.set_ylim(min(phe),max(rows[-1]))
#ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda y, pos: '{0:g}'.format(y-1)))
#ax.yaxis.set_major_locator(ticker.FixedLocator(rows[0]))
#ax.yaxis.set_major_locator(ticker.MultipleLocator(0.5))
plt.grid(True)
plt.tick_params(labelsize=12)
#plt.margins(0.01)
box = ax.get_position()
ax.set_position([box.x0, box.y0 + box.height * 0.5,box.width, box.height * 0.8])

##ax.legend(("African-American","African-Caribbean","Afro-Asiatic","Afro-Asiatic Cushitic","Afro-Asiatic Omotic","Afro-Asiatic Semitic","East Asian","European North","European South","European USA","European center","KhoeSan","Latin American","Niger-Congo Bantu South","Niger Congo Bantu","Niger Congo Volta Niger","Niger Congo West","South Asian","UK Indian","USA Indian"),loc='upper center',bbox_to_anchor=(0.5, -0.19),fancybox=True, shadow=True, ncol=4,fontsize='x-small',labelspacing=0.1,columnspacing=0.2)

#ax.legend(('Afro-Asiatic Omotic', 'African-Caribbean', 'European South', 'Afro-Asiatic Semitic', 'Niger Congo West', 'European North', 'African-American','Afro-Asiatic', 'European USA', 'East Asian', 'Afro-Asiatic Cushitic', 'Latin American','Niger Congo Volta Niger', 'Niger-Congo Bantu South', 'Niger Congo Bantu', 'UK Indian', 'European center', 'Khoe-San', 'South Asian', 'USA Indian'),loc='upper center',bbox_to_anchor=(0.5, -0.19),fancybox=True, shadow=True, ncol=4,fontsize='x-small',labelspacing=0.1,columnspacing=0.2)

###ax.legend(("Mandinka","Niger_Kordofanian","Nilo_Saharan","Bantu_East","BantuSan","Bantu_South","European_center","European_North","European_South","European_USA","Indo_European","Chimp","Denisova","Neandertal","Pygmy","San","KhoeSan","Mongol","African_American","African_Caribbean","Latin_American","Maghreb","South_Africa_Coloured", "East_Asian","UK_Indian","USA_Indian","Afro_Arabs","Austroasiatic","Afro_Asiatic_Cushitic","Afro_Asiatic_Egyptic","Afro_Asiatic_Omotic","Afro_Asiatic_Semitic"),loc='upper center',bbox_to_anchor=(0.5, -0.19),fancybox=True, shadow=True, ncol=6,fontsize='large',labelspacing=0.1,columnspacing=0.2)


ax.legend(("Mandinka","Niger Kordofanian","Nilo Saharan","Bantu East","Bantu-San","Bantu South","European Center","European North","European South","European USA","Indo European","Chimp","Denisova","Neandertal","Pygmy","San","KhoeSan","Mongol","African American","African Caribbean","Latin American","Maghrebi","South Africa Coloured", "East Asian","UK Indian","USA Indian","Afro-Arabs","Austroasiatic","Afro-Asiatic Cushitic","Afro-Asiatic Egyptic","Afro-Asiatic Omotic","Afro-Asiatic Semitic"),loc='upper center', bbox_to_anchor=(0.5, -0.14),fancybox=True, shadow=True, ncol=6,fontsize='large',labelspacing=0.1,columnspacing=0.2)

#ax.legend(("African-American","African-Caribbean","Afro-Asiatic","Afro-Asiatic Cushitic","Afro-Asiatic Omotic","Afro-Asiatic Semitic","East Asian","European North","European South","European USA","European center","KhoeSan","Latin American","Niger-Congo Bantu South","Niger Congo Bantu","Niger Congo Volta Niger","Niger Congo West","South Asian","UK Indian","USA Indian"),loc='upper center', bbox_to_anchor=(0.5, -0.19),fancybox=True, shadow=True, ncol=4,fontsize='x-small',labelspacing=0.1,columnspacing=0.2)
#rcParams["legend.columnspacing"] = 1.0

fig.savefig(sys.argv[2])
