import pandas as pd
import numpy as np

class Reader:
	def __init__(self, file_name):
		self.file_name = file_name

	def read(self):
		data_frame = pd.read_csv(self.file_name)
		columns = data_frame.columns.tolist()

		to_show = columns[:6] + columns[-6:]
		print("\nSample data:")
		print(data_frame[to_show].head(6))

		#print("Column names:")
		#print(col_names)
