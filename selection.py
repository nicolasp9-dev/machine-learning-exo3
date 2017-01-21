from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2, mutual_info_classif, f_classif
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.feature_selection import SelectFromModel

#
# Function that reduce the number of features of a dataset using one of the five choosed techniques 
# and based on a purcentage of reduction (0.8 : 80% of original number of features will be conserve)
#

def features_selection(X, y, technique) :
	
	if technique == 'univariate':
        	return univariant_feature_selection(X,y,'KBest','chi2', .6)
	if technique == 'lvariance':
		return lvariance_feature_selection(X,y)
	if technique == 'tree_based':
		return tree_based_feature_selection(X,y)


def univariant_feature_selection(X,y,method,score_function, percentage) :
	k = int(X[0].size * percentage)

	if method == 'KBest':
		if score_function == 'chi2':
		    return SelectKBest(chi2, k=k).fit_transform(X, y)
		elif score_function == 'mutual_info_classif':
		    return SelectKBest(mutual_info_classif, k=k).fit_transform(X, y)
		elif score_function == 'f_classif':
		    return SelectKBest(f_classif, k=k).fit_transform(X, y)

def lvariance_feature_selection(X,y) :
	clf = ExtraTreesClassifier()
	clf = clf.fit(X, y)
	model = SelectFromModel(clf, prefit=True)
	return model.transform(X)


def tree_based_feature_selection(X,y) :


	return 
