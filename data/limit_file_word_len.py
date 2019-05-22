 # -*- coding: utf-8 -*-
'''
1:plot a statistic map
2:give a max and a min value, generate src and tgt
'''
import matplotlib.pyplot as plt
import collections
import numpy as np
import time
room = ['test','train','valid']
def plot_distribution(genera_static,f_name):
    
	x = []
	y = []

	for k,v in genera_static:
		print(k,v)
		
		x.append(k)
		y.append(len(v))
	print(x)
	z = np.zeros(max(x)-min(x)+1)
	index = [m - min(x) for m in x]
	z[index]=y
	plt.title(f_name)
	plt.bar(range(min(x),max(x)+1),z)
	plt.show()

	
def prun_file(static,max_len=100,min_len=0):
	
	
	for f_name in room:
		content = static[f_name].items()
		
		f_wen = open(f_name+'.de-en.en_diff_prun','w',encoding='utf-8')
		f_ren = open(f_name+'.de-en.en_diff','r',encoding='utf-8')
		f_rde = open(f_name+'.de-en.de','r',encoding='utf-8')
		f_wde = open(f_name+'.de-en.de_diff_prun','w',encoding='utf-8')

		line_en = f_ren.readline().strip('\n')
		line_de = f_rde.readline().strip('\n')
		while line_en!='':
			if (int(line_en)<max_len and int(line_en)>min_len):
				f_wen.write(line_en+'\n')
				f_wde.write(line_de+'\n')
			line_en = f_ren.readline().strip('\n')
			line_de = f_rde.readline().strip('\n')

		f_wen.close()
		f_ren.close()
		f_ren.close()
		f_wde.close()

def main():
    
    
	static = {'train':collections.defaultdict(list),'test':collections.defaultdict(list),'valid':collections.defaultdict(list)}
	sorteddict = {'train':list,'test':list,'valid':list}
	linenum = 0
	for f_name in room:
		f = open(f_name+'.de-en.en_diff_prun','r')
		line = f.readline().strip('\n')
		
		while line!='':
			linenum+=1
			static[f_name][int(line)].append(linenum)
			try:
				line = f.readline().strip('\n')
				
		
			except:
				print('except')
				continue
			
		f.close()
		sorteddict[f_name]=sorted(static[f_name].items())

	genera_static = collections.defaultdict(list)
	for f_name in room:
		for k,v in sorteddict[f_name]:
			genera_static[k].append(v)
	plot_distribution(sorteddict['train'],'train')
	plot_distribution(sorteddict['valid'],'valid')
	plot_distribution(sorteddict['test'],'test')

	#prun_file(static,20,-15)







	

    

	
if __name__=='__main__':
	main()
	    
