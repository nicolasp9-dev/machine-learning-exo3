from sklearn import neighbors
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn import svm

#
# Function that test a data set with differents learning techniques and a validation technique
# and return the 3 scores (for each techniques) and the average score.
#

def data_test_and_validation(x, y) :
	score = []
	x_train, x_test, y_train, y_test  = train_test_split(x, y, test_size=.3)
	
	# K-NN Algorythm
	n_neighbors = 12
	x_train, x_test, y_train, y_test  = train_test_split(x, y, test_size=.3)
	clf = neighbors.KNeighborsClassifier(n_neighbors, weights='distance')
    	clf.fit(x_train, y_train)
	score.append(round(clf.score(x_test, y_test),3))

	# NN Algorythm
	clf2 = MLPClassifier(alpha=1)
   	clf2.fit(x_train,y_train)
    	score.append(round(clf2.score(x_test, y_test),3))

	# SVM ML Algorithm
	clf3 = svm.SVC()
	clf3.fit(x_train, y_train)
	score.append(round(clf3.score(x_test, y_test),3))  	

	score.append(round((score[0]+score[1]+score[2])/3,3))
	#print "K-nn score : %f / NN score : %f / SVM Algorythm : %f / Average : %f" % (score[0],  score[1], score[2], score[3])
	return score
