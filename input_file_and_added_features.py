import pandas as pd

#IMPORTING THE RAW CSV FILE
import csv as csv
import os
cwd = os.getcwd()
raw_data = pd.read_csv(os.path.join(cwd,'train.csv'))

###MAPPING FUNCTIONS
#Weekday conversion to numerical values
def weekday_num(input_val):
	if input_val == 'Friday':
		return 5
	elif input_val == 'Monday':
		return 1
	elif input_val == 'Tuesday':
		return 2
	elif input_val == 'Wednesday':
		return 3
	elif input_val == 'Thursday':
		return 4
	elif input_val == 'Friday':
		return 5

###IMPLEMENTATION OF ENGINEERED FEATURES
raw_data['Weekday_num'] = raw_data['Weekday'].map(weekday_num)


###WRITE THE MODIFIED FILE TO CSV
raw_data.to_csv('modified_input_data.csv',sep = ',')
