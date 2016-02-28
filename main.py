from reader import Reader

def main():
    print ("Hello World")
    read_churn_data()

def read_churn_data():
	reader = Reader("data.csv")
	reader.read()

if __name__ == "__main__":
    main()