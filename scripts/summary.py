#! /usr/bin/python
# summary.py -- display some quick summary statistics

import sys, csv
import numpy as np
from collections import Counter
from matplotlib import pyplot as plt

USAGE = 'USAGE: python summary.py datafile'
DATA = '/home/gabe/projects/ideology/data/rawdata.csv'

def main():
	if len(sys.argv) != 2: print USAGE; exit()
	f = open(sys.argv[1])
	data = np.array([row for row in csv.reader(f)])

	print '%dx%d table loaded' % (data.shape[0]-1,data.shape[1])	# Minus 1 for header

	print '\nSex distribution:'
	sexes = Counter(data[1:,175])
	print '%d women and %d men' % (sexes['Women'],sexes['Men'])

	print '\nPlotting age distribution'
	plt.hist(map(int,data[1:,176]), normed=1)
	plt.title('Age distribution')
	plt.show()

	print '\nParty info:'
	for k,v in Counter(data[1:,195]).items(): print '%s:%d'%(k,v)

	print '\nState info:'
	for k,v in sorted(Counter(data[1:,9]).items(),key=lambda x: -x[1]): print '%s:%d'%(k,v)

if __name__=='__main__': main()