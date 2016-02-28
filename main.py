from reader import Reader

def main():
    [X,Y] = read_churn_data()
    

def read_churn_data():
	reader = Reader()
	return reader.read_data("data.csv")


if __name__ == "__main__":
    main()