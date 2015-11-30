import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv as csv
import os

cwd = os.getcwd()
data = pd.read_csv(os.path.join(cwd,'modified_input_data.csv'))

def understand_data(input_list):
	for choice in input_list:
		if choice==1:
			print data.head(10)
			#print pd.unique(data.TripType)
			#print 'Count of unique product Upc', int(pd.DataFrame(pd.unique(data.Upc)).count())
			#print 'Count of unique product department descriptions', int(pd.DataFrame(pd.unique(data.DepartmentDescription)).count())
			print pd.unique(data.Weekday)
			print pd.unique(data.Weekday_num)
		elif choice ==2:
			#share_of_trip_type = pd.DataFrame(data.groupby(['TripType'],axis= 0)['VisitNumber'].count()*100/len(data))
			#share_of_trip_type = pd.DataFrame(data.groupby(['TripType'],axis= 0)['VisitNumber'].count())
			share_of_trip_type = pd.DataFrame(data.groupby(['TripType'],axis= 0)['VisitNumber'].nunique())
			print share_of_trip_type

			# share_of_trip_type_weekday_weekend = pd.DataFrame(data.groupby(['TripType','Weekend_Weekday'],axis= 0)['VisitNumber'].nunique())
			# print share_of_trip_type_weekday_weekend



			#products_departments = pd.DataFrame(data.groupby(['DepartmentDescription'],axis= 0)['Upc'].nunique())   #1
			#products_departments = pd.DataFrame(data.groupby(['DepartmentDescription'],axis= 0)['Upc'].count())
			#print products_departments

		elif choice==3:
			# department_triptype_pivot = pd.pivot_table(data, values='VisitNumber', index='DepartmentDescription', columns='TripType', aggfunc=np.size)    #2
			# print department_triptype_pivot

			# department_finelinenum_pivot = pd.pivot_table(data, values='VisitNumber', index='FinelineNumber', columns='DepartmentDescription', aggfunc=np.size)
			# print department_finelinenum_pivot

			# department_weekday_pivot = pd.pivot_table(data, values='VisitNumber', index='DepartmentDescription', columns='Weekday', aggfunc=np.size)
			# print department_weekday_pivot

			# Weekday_trip_type_pivot = pd.pivot_table(data, values='VisitNumber', index='TripType', columns='Weekday', aggfunc=np.size)
			# print Weekday_trip_type_pivot

			share_of_trip_type_weekday_weekend = pd.pivot_table(data, values='VisitNumber',index='TripType', columns='Weekend_Weekday', aggfunc=pd.Series.nunique)
			print share_of_trip_type_weekday_weekend

		elif choice==10:
			#http://stackoverflow.com/questions/21654635/scatter-plots-in-pandas-pyplot-how-to-plot-by-category
			groups = data.groupby('TripType')
			fig, ax = plt.subplots()
			for name, group in groups:
				#print name
				#print group.DepartmentDescription
				ax.plot(group.ScanCount, group.Weekday_num, marker='o', linestyle='', ms=5, label=name)
				ax.legend()
			plt.show()


		elif choice==20:
			#(pd.DataFrame(pd.unique(data.TripType))).to_csv('Unique_trip_types.csv',sep = ',',index = False)
			#share_of_trip_type.to_csv('TripType_visitnumber_unique.csv',sep = ',')
			share_of_trip_type_weekday_weekend.to_csv('TripType_weekday_weekend_visitnumber_unique.csv',sep=',')
			#products_departments.to_csv('Unique products per department.csv',sep = ',')
			#department_triptype_pivot.to_csv('DepartmentDescription trip Type visit number frequency pivot table.csv',sep=',')
			#department_finelinenum_pivot.to_csv('DepartmentDescription finelinenumber visit number frequency pivot table.csv',sep=',')
			#department_weekday_pivot.to_csv('DepartmentDescription Weekday visit number frequency pivot table.csv',sep=',')
			#Weekday_trip_type_pivot.to_csv('TripType Weekday visit number frequency pivot table.csv',sep=',')


understand_data([3,20])




#References
#1 - http://stackoverflow.com/questions/15411158/pandas-countdistinct-equivalent
#2 - http://pandas.pydata.org/pandas-docs/stable/reshaping.html
