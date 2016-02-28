import numpy as np
from sklearn.cross_validation import KFold
from sklearn import metrics

class Validator:
    def __init__(self, X, y):
        self.X = X
        self.y = y

    def performance(self, classifier):
        fold_indices = KFold(len(self.y), n_folds=5, shuffle=True)
        
        y_pred = self.y.copy()
        clf = classifier()

        for train_index, test_index in fold_indices:
            clf.fit(self.X[train_index], self.y[train_index])
            y_pred[test_index] = clf.predict(self.X[test_index])

        print("Performance for %s" % clf)
        print("accuracy: %.3f" % np.mean(self.y == y_pred))
        print("Classification report")        
        print(metrics.classification_report(self.y, y_pred))
        print("Confusion matrix")
        print(metrics.confusion_matrix(self.y, y_pred))


