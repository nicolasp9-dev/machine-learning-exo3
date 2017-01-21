#!/usr/bin/python


# Seyed Saeid Masoumzadeh, Nicolas Peslerbe
# Exercise 3 implementation


# Needed libraries
# Scipy
# Arff :  easy_install liac-arff

import sys, getopt
import arff, numpy as np
from sklearn import neighbors

#
# Load .ARFF file into a numpy table
#
# Input parameter : 
#	dataset = (Mandatory) file name as String
# Return value : numpy array
#

def load_file(datasetfile):
	try :
		dataset = arff.load(open(datasetfile, 'rb'))
	except :
		print 'Impossible to find or load :',datasetfile
		sys.exit(4)
	data = np.array(dataset['data'])
	return data


#
# Get parameters entered into the terminal
#
# Input parameter :
#	arv = (Mandatory) input arguments for the terminal 
# Return value :
#	dataset path as string
#

def options_load(argv) :
	datasetfile = ''	
	try:
      		opts, args = getopt.getopt(argv,"hd:",["help","datasetfile="])
   	except getopt.GetoptError:
      		print 'Error'
		sys.exit(2)

	for opt, arg in opts:

	      	if opt in ("-h", "--help"):
	         	print get_help_txt()
	        	sys.exit()

	     	elif opt in ("-d", "--datasetfile"):
	         	datasetfile = arg
	if datasetfile == '' :
		print '\nMandatory arguments are missing\nPlease enter : -h or --help for help\n'
		sys.exit(3)
	return datasetfile



#
# Function that return the complete text for help
#

def get_help_txt() :
	return 	"""
Help :
-d or --datasetfile <path of dataset> : (Mandatory) Path of the dataset you want to work with
		"""

#
# Function that reduce the number of features of a dataset using one of the five choosed techniques 
# and based on a purcentage of reduction (0.8 : 80% of original number of features will be conserve)
#

def features_selection(x, y, technique, pourcentage_of_features) :
	x_new = []
	y_new = []
	

	return x_new, y_new

#
# Function that test a data set with differents learning techniques and a validation technique
# and return the 3 scores (for each techniques) and the average score.
#


def data_test_and_validation(x, y) :
	score = []

	# K-NN Algorythm
	n_neighbors = 5
	
	clf = neighbors.KNeighborsClassifier(n_neighbors, weights='distance')
    	clf.fit(x, y)
	
	
	#score.append((score[O]+score[1]+score[2])/3)
	return score


# Main function

def main(argv):
   	datasetfile = options_load(argv)
	data  = load_file(datasetfile)
	x = data[:,:len(data[0])-1]
	x = x.astype(np.float)
	y = data[:,len(data[0])-1]
	x_new, y_new = features_selection(x, y, "1", "0.8")
	score = data_test_and_validation(x, y)

if __name__ == "__main__":
   	main(sys.argv[1:])
