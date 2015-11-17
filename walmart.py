import pandas as pd
import numpy as np
import csv as csv
import os

cwd = os.getcwd()
raw_data = pd.read_csv(os.path.join(cwd,'train.csv'))

def understand_data(input_list):
	for choice in input_list:
		if choice==1:
			print raw_data.head(10)
			print pd.unique(raw_data.TripType)
		elif choice ==2:
			share_of_trip_type = pd.DataFrame(raw_data.groupby(['TripType'],axis= 0)['Upc'].count()*100/len(raw_data))
			print share_of_trip_type
		elif choice==3:
			(pd.DataFrame(pd.unique(raw_data.TripType))).to_csv('Unique_trip_types.csv',sep = ',',index = False)
			share_of_trip_type.to_csv('TripType_percentage_share.csv',sep = ',')
		elif choice ==4:
			


understand_data([1])

