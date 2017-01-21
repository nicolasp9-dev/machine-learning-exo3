#!/usr/bin/python


# Seyed Saeid Masoumzadeh, Nicolas Peslerbe
# Exercise 3 implementation


# Needed libraries
# Scipy
# Arff :  easy_install liac-arff

from ml_algorythms import data_test_and_validation
from selection import features_selection
from sklearn import preprocessing

import csv
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
	
	score= []
	score.append(['technique','percentage','knn score','nn score','SVM Score','average score','total number of features', 'current number of features'])
	for technique in ['univariate', 'tree_based', 'l1'] :
		for percentage in np.arange(0.1,1.05,0.1) :
			score_prov = []
			score_prov.append(technique)
			score_prov.append(percentage)
			x_new = features_selection(x, y, technique, percentage)
			score_prov = score_prov+data_test_and_validation(x_new, y)
			score_prov.append(int(x[0].size))
			score_prov.append(int(x[0].size * percentage))	
			score.append(score_prov)
	

	with open(datasetfile+".csv", "wb") as f:
	    writer = csv.writer(f)
	    writer.writerows(score)

if __name__ == "__main__":
    main(sys.argv[1:])
