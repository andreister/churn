import numpy as np
from sklearn.cross_validation import KFold

class Validator:
    def __init__(self, X, y):
        self.X = X
        self.y = y

        pass

    def accuracy(self, classifier, **kwargs):
        fold_indices = KFold(len(self.y), n_folds=5, shuffle=True)
        
        y_pred = self.y.copy()
        clf = classifier(**kwargs)

        for train_index, test_index in fold_indices:
            clf.fit(self.X[train_index], self.y[train_index])
            y_pred[test_index] = clf.predict(self.X[test_index])

        #report accuracy as a mean of correct predictions
        return np.mean(self.y == y_pred)

