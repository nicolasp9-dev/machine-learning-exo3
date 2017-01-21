#!/usr/bin/python


# Seyed Saeid Masoumzadeh, Nicolas Peslerbe
# Exercise 3 implementation


# Needed libraries
# Scipy
# Arff :  easy_install liac-arff

from ml_algorythms import data_test_and_validation
from selection import features_selection

import sys, getopt
import arff, numpy as np
import loading as load

# Main function

def main(argv):
   	datasetfile = load.options(argv)
	data  = load.file(datasetfile)
	x = data[:,:len(data[0])-1]
	x = x.astype(np.float)
	y = data[:,len(data[0])-1]	
	x_new = features_selection(x, y, 'univariate')
	score = data_test_and_validation(x_new, y)

if __name__ == "__main__":
   	main(sys.argv[1:])
