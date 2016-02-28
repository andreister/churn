from reader import Reader
from validator import Validator

from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier as RF
from sklearn.neighbors import KNeighborsClassifier as KNN


def main():
	[X, y] = read_churn_data()
	validator = Validator(X, y)

	print("SVM: %.3f" % validator.accuracy(SVC))
	print("RF: %.3f" % validator.accuracy(RF))
	print("KNN: %.3f" % validator.accuracy(KNN))

def read_churn_data():
	reader = Reader()
	return reader.read_data("data.csv")




if __name__ == "__main__":
    main()