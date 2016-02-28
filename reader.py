import pandas as pd
import numpy as np

class Reader:
	def __init__(self):
		pass

	def read_data(self, file_name):
		"""Reads the data from the given file, drops a few columns and rescales
		"""

		data_frame = pd.read_csv(file_name)
		Y = np.where(data_frame['Churn?'] == 'True.', 1, 0)

		irrelevant_columns = [
			'State',   		#doesn't sound relevant
			'Phone',		#doesn't sound relevant
			'VMail Message',#doesn't sound relevant
			'Day Mins',		#for simplicity, ditch Mins and Calls and keep Day Charge only
			'Day Calls',	#for simplicity, ditch Mins and Calls and keep Day Charge only
			'Eve Mins',		#for simplicity, ditch Mins and Calls and keep Eve Charge only
			'Eve Calls',	#for simplicity, ditch Mins and Calls and keep Eve Charge only
			'Night Mins',	#for simplicity, ditch Mins and Calls and keep Night Charge only
			'Night Calls',	#for simplicity, ditch Mins and Calls and keep Night Charge only
			'Intl Mins',	#for simplicity, ditch Mins and Calls and keep Intl Charge only
			'Intl Calls',	#for simplicity, ditch Mins and Calls and keep Intl Charge only
			'Churn?'		#target variable, already recorded as "Y"
		]
		yesno_columns = ["Int'l Plan", "VMail Plan"]

		data_frame = data_frame.drop(irrelevant_columns, axis=1)
		data_frame[yesno_columns] = data_frame[yesno_columns] == "yes"

		X = data_frame.as_matrix().astype(np.float)
		return X, Y
