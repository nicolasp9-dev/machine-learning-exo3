from sklearn import neighbors
from sklearn.model_selection import train_test_split



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
	score.append(clf.score(x_test, y_test))
	print score[0]

	# Second ML Algorythm

	# Third ML Algorithm

	#score.append((score[O]+score[1]+score[2])/3)
	return score
