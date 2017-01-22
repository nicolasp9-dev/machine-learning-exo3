from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2, mutual_info_classif, f_classif
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.feature_selection import SelectFromModel
from sklearn.feature_selection import VarianceThreshold
from sklearn.svm import LinearSVC
from sklearn import preprocessing


#
# Function that reduce the number of features of a dataset using one of the five choosed techniques 
# and based on a purcentage of reduction (0.8 : 80% of original number of features will be conserve)
#

def features_selection(X, y, technique, percentage) :

    if technique == 'univariate':
            return univariant_feature_selection(X,y,'KBest','chi2', percentage)
    if technique == 'lvariance':
        return lvariance_feature_selection(X,y, percentage)
    if technique == 'tree_based':
        return tree_based_feature_selection(X,y, percentage)
    if technique == 'l1':
        return l1_feature_selection(X,y, percentage)


def univariant_feature_selection(X,y,method,score_function, percentage) :
    k = int(X[0].size * percentage)
    if method == 'KBest':
        if score_function == 'chi2':
            return SelectKBest(chi2, k=k).fit_transform(X, y)
        elif score_function == 'mutual_info_classif':
            return SelectKBest(mutual_info_classif, k=k).fit_transform(X, y)
        elif score_function == 'f_classif':
            return SelectKBest(f_classif, k=k).fit_transform(X, y)


def lvariance_feature_selection(X,y, percentage) :
    X = preprocessing.scale(X)
    j=0.5
    while True :
        j+=1
        sel = VarianceThreshold(threshold=(j * (1 - j)))
        if (sel.fit_transform(X))[0].size <= percentage*X[0].size:
            break
        print(sel.fit_transform(X)[0].size)
    return sel.transform(X)


def l1_feature_selection(X,y, percentage) :
    j=percentage*X[0].size*0.002
    while True :
        j-=0.0001*percentage*X[0].size/2
        lsvc = LinearSVC(C=j, penalty="l1", dual=False).fit(X, y)
        model = SelectFromModel(lsvc, prefit=True)
        if ((model.transform(X))[0].size <= percentage*X[0].size) :
            print("Yeh")
            break
        print(model.transform(X)[0].size)
        print(percentage*X[0].size)
    return model.transform(X)


def tree_based_feature_selection(X,y, percentage) :
    clf = ExtraTreesClassifier()
    clf = clf.fit(X, y)
    j=0
    while True :
        j+=0.0001*percentage*X[0].size/3
        stra = str(j) + "*mean"
        model = SelectFromModel(clf, prefit=True, threshold=stra)
        if (model.transform(X))[0].size <= percentage*X[0].size:
            print(model.transform(X)[0].size)
            print(percentage*X[0].size)
            break
    return model.transform(X)

