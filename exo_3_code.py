#!/usr/bin/python


# Seyed Saeid Masoumzadeh, Nicolas Peslerbe
# Exercise 3 implementation


# Needed libraries
# Scipy
# Arff :  easy_install liac-arff

from ml_algorythms import data_test_and_validation
from selection import features_selection
from sklearn import preprocessing

import sys, getopt
import arff, numpy as np
import loading as load

# Main function


def main(argv):
	
	# Loading dataset
   	datasetfile = load.options(argv)
	data  = load.file(datasetfile)
	x = data[:,:len(data[0])-1]
	x = x.astype(np.float)
	y = data[:,len(data[0])-1]

	# Preprocessing x part of dataset
	min_max_scaler = preprocessing.MinMaxScaler()
	x = min_max_scaler.fit_transform(x)	
	
	print "No selection"	
	score = data_test_and_validation(x, y)

	print "l1 0.8"	
	x_new = features_selection(x, y, 'l1', .8)
	score = data_test_and_validation(x_new, y)

	print "Univariate 0.6"	
	x_new = features_selection(x, y, 'univariate', .6)
	score = data_test_and_validation(x_new, y)

	print "Univariate 0.4"	
	x_new = features_selection(x, y, 'univariate', .4)
	score = data_test_and_validation(x_new, y)

	print "Univariate 0.2"	
	x_new = features_selection(x, y, 'univariate', .2)
	score = data_test_and_validation(x_new, y)

	print "Tree based 0.8"
	x_new = features_selection(x, y, 'tree_based', .8)
	score = data_test_and_validation(x_new, y)
	
	print "Tree based 0.6"
	x_new = features_selection(x, y, 'tree_based', .6)
	score = data_test_and_validation(x_new, y)

	print "Tree based 0.4"
	x_new = features_selection(x, y, 'tree_based', .4)
	score = data_test_and_validation(x_new, y)

	print "Tree based 0.2"
	x_new = features_selection(x, y, 'tree_based', .2)
	score = data_test_and_validation(x_new, y)

if __name__ == "__main__":
    main(sys.argv[1:])
