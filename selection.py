from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2, mutual_info_classif, f_classif


#
# Function that reduce the number of features of a dataset using one of the five choosed techniques 
# and based on a purcentage of reduction (0.8 : 80% of original number of features will be conserve)
#

def features_selection(x, y, technique) :
	
	if technique == 'univariate':
        	x_new= univariant_feature_selection(x,y,'KBest','chi2')

	return x_new, y


def univariant_feature_selection(X,y,method,score_function ):
    if method == 'KBest':
        if score_function == 'chi2':
            return SelectKBest(chi2, k=2).fit_transform(X, y)
        elif score_function == 'mutual_info_classif':
            return SelectKBest(mutual_info_classif, k=2).fit_transform(X, y)
        elif score_function == 'f_classif':
            return SelectKBest(f_classif, k=2).fit_transform(X, y)
