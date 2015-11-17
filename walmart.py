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
			#print pd.unique(raw_data.TripType)
			print 'Count of unique product Upc', int(pd.DataFrame(pd.unique(raw_data.Upc)).count())
			print 'Count of unique product department descriptions', int(pd.DataFrame(pd.unique(raw_data.DepartmentDescription)).count())
		elif choice ==2:
			share_of_trip_type = pd.DataFrame(raw_data.groupby(['TripType'],axis= 0)['VisitNumber'].count()*100/len(raw_data))
			print share_of_trip_type
  
			products_departments = pd.DataFrame(raw_data.groupby(['DepartmentDescription'],axis= 0)['Upc'].nunique())  #http://stackoverflow.com/questions/15411158/pandas-countdistinct-equivalent

			print products_departments
		elif choice==3:
			#http://pandas.pydata.org/pandas-docs/stable/reshaping.html
			department_triptype_pivot = pd.pivot_table(raw_data, values='VisitNumber', index='DepartmentDescription', columns='TripType', aggfunc=np.size)
			print department_triptype_pivot
		elif choice==20:
			#(pd.DataFrame(pd.unique(raw_data.TripType))).to_csv('Unique_trip_types.csv',sep = ',',index = False)
			#share_of_trip_type.to_csv('TripType_percentage_share.csv',sep = ',')
			#products_departments.to_csv('Unique products per department.csv',sep = ',')
			department_triptype_pivot.to_csv('DepartmentDescription trip Type visit number frequency pivot table.csv',sep=',')



understand_data([3,20])

