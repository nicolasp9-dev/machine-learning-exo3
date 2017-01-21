import sys, getopt
import arff, numpy as np

#
# Load .ARFF file into a numpy table
#
# Input parameter : 
#	dataset = (Mandatory) file name as String
# Return value : numpy array
#

def file(datasetfile):
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

def options(argv) :
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

