import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv as csv
import os

cwd = os.getcwd()
data = pd.read_csv(os.path.join(cwd,'modified_input_data.csv'))

#print data.count()

def understand_data(input_list):
	for choice in input_list:
		if choice==1:
			# print data.head(20)
			print np.sort(pd.unique(data.TripType))
			# print 'Count of unique product Upc', int(pd.DataFrame(pd.unique(data.Upc)).count())
			# print 'Count of unique product department descriptions', int(pd.DataFrame(pd.unique(data.DepartmentDescription)).count())
			#print 'Count of visitnumber',int(pd.DataFrame(pd.unique(data.VisitNumber)).count())
			#print pd.unique(data.VisitNumber)
			# print pd.unique(data.Weekday_num)
			# list_of_departments = pd.unique(data.DepartmentDescription)

		elif choice ==2:   #group by tables
			# #share_of_trip_type = pd.DataFrame(data.groupby(['TripType'],axis= 0)['VisitNumber'].count()*100/len(data))
			# #share_of_trip_type = pd.DataFrame(data.groupby(['TripType'],axis= 0)['VisitNumber'].count())
			# share_of_trip_type = pd.DataFrame(data.groupby(['TripType'],axis= 0)['VisitNumber'].nunique())
			# print share_of_trip_type

			# share_of_trip_type_weekday_weekend = pd.DataFrame(data.groupby(['TripType','Weekend_Weekday'],axis= 0)['VisitNumber'].nunique())
			# print share_of_trip_type_weekday_weekend



			#products_departments = pd.DataFrame(data.groupby(['DepartmentDescription'],axis= 0)['Upc'].nunique())   #1
			#products_departments = pd.DataFrame(data.groupby(['DepartmentDescription'],axis= 0)['Upc'].count())
			#print products_departments

			# products_in_departments = pd.DataFrame(data.groupby(['DepartmentDescription'],axis= 0)['Upc'].nunique())   #1
			# #products_departments = pd.DataFrame(data.groupby(['DepartmentDescription'],axis= 0)['Upc'].count())
			# print products_in_departments

			# departments_per_product = pd.DataFrame(data.groupby(['Upc'],axis= 0)['DepartmentDescription'].nunique())
			# print departments_per_product.head(10)
			# #print pd.unique(departments_per_product.DepartmentDescription)

			department_per_visit= pd.DataFrame(data.groupby(['VisitNumber'],axis= 0)['DepartmentDescription'].nunique())
			# #department_per_visit = department_per_visit.rename(columns = {'0':'Number_of_department'})
			# #department_per_visit.rename(columns = {'0':'Number_of_department'},inplace= True)
			department_per_visit.columns = ['Number_of_department']
			# print department_per_visit.count()

			avg_finelinenumb_per_visit = pd.DataFrame(data.groupby(['VisitNumber'],axis= 0)['FinelineNumber'].mean())
			avg_finelinenumb_per_visit.columns = ['Avg_finelinenumber']

			# visit_num_trip_type = data[['VisitNumber','TripType']]
			# visit_num_trip_type = visit_num_trip_type.drop_duplicates()
			# visit_num_trip_type = pd.DataFrame(visit_num_trip_type)
			# print visit_num_trip_type
			# print visit_num_trip_type.count()

		elif choice==3:    #pivot tables
			# department_triptype_pivot = pd.pivot_table(data, values='VisitNumber', index='DepartmentDescription', columns='TripType', aggfunc=np.size)    #2
			# print department_triptype_pivot

			# department_finelinenum_pivot = pd.pivot_table(data, values='VisitNumber', index='FinelineNumber', columns='DepartmentDescription', aggfunc=np.size)
			# print department_finelinenum_pivot

			# department_weekday_pivot = pd.pivot_table(data, values='VisitNumber', index='DepartmentDescription', columns='Weekday', aggfunc=np.size)
			# print department_weekday_pivot

			# Weekday_trip_type_pivot = pd.pivot_table(data, values='VisitNumber', index='TripType', columns='Weekday', aggfunc=np.size)
			# print Weekday_trip_type_pivot

			# share_of_trip_type_weekday_weekend = pd.pivot_table(data, values='VisitNumber',index='TripType', columns='Weekend_Weekday', aggfunc=pd.Series.nunique)
			# print share_of_trip_type_weekday_weekend

			visit_department_distribution = pd.pivot_table(data,values='ScanCount',rows=['VisitNumber'],cols='DepartmentDescription',aggfunc=np.sum,fill_value = 0)
			# # # #visit_department_distribution = pd.pivot_table(data,values='ScanCount',rows='TripType',cols='DepartmentDescription',aggfunc=np.sum,fill_value = 0)
			# print visit_department_distribution.count()

			weekday_dist = pd.pivot_table(data,values='ScanCount',rows=['VisitNumber'],cols='Weekday',aggfunc=np.size,fill_value = 0)
			# print weekday_dist.count()



			# product_department_overlap_check = pd.pivot_table(data, values='VisitNumber',index='Upc',columns='DepartmentDescription', aggfunc=pd.Series.nunique,fill_value = 0)
			# print product_department_overlap_check

			#triptype_department_distribution_counts = pd.pivot_table(data,values='ScanCount',rows=['TripType'],cols='DepartmentDescription',aggfunc=np.size,fill_value = 0)
			#print triptype_department_distribution_counts

		elif choice==4:
			classifier_input_train_data = pd.concat([visit_department_distribution,weekday_dist,department_per_visit,avg_finelinenumb_per_visit],axis=1, join_axes=[visit_department_distribution.index])
			#classifier_input_train_data = pd.concat([classifier_input_train_data,data[['TripType']]], axis=1)
			#classifier_input_train_data['VisitNumber'] = data[['VisitNumber']]
			classifier_input_train_data['TripType'] = data[['TripType']]

			print np.sort(pd.unique(classifier_input_train_data.TripType))
			# print classifier_input_train_data.count()


		elif choice==10:
			#http://stackoverflow.com/questions/21654635/scatter-plots-in-pandas-pyplot-how-to-plot-by-category
			groups = data.groupby('TripType')
			fig, ax = plt.subplots()
			for name, group in groups:
				#print nam
				#print group.DepartmentDescription
				ax.plot(group.ScanCount, group.Weekday_num, marker='o', linestyle='', ms=5, label=name)
				ax.legend()
			plt.show()

		elif choice == 11:
			#probability calculations
			list_of_triptypes = np.sort(pd.unique(data.TripType))
			list_of_departments = pd.unique(data.DepartmentDescription)
			print list_of_triptypes
			print list_of_departments
			dep_trip_probability_cal = pd.DataFrame(columns = list_of_departments)
			sum = 0
			no_of_dept = 0
			for col_element in list_of_departments:
				number_in_department = float(len(data[(data.DepartmentDescription == col_element)]))
				total_number = float(len(data) - 1361)
				sum = sum + number_in_department
				prop_of_dept_in_total = (number_in_department/total_number)*100
				cum_prop_of_dept = (sum/total_number)*100
				no_of_tt = 0
				for row_element in list_of_triptypes:
					no_of_tt = no_of_tt + 1
					number_in_dept_tt = float(len(data[(data.DepartmentDescription == col_element)& (data.TripType == row_element)]))
					if number_in_department>0:
						probability = (number_in_dept_tt/number_in_department)*100
					else:
						probability = 0
					print 'probability',col_element,row_element,probability
					dep_trip_probability_cal.set_value(row_element,col_element,probability)
			print 'sum',sum
			print dep_trip_probability_cal

		elif choice ==12:
			top3_dept_explaining_tt = pd.DataFrame(columns = ['Highest Prob','Second highest Prob','Third highest Prob'])
			prob_data = pd.read_csv(os.path.join(cwd,'dep_triptype_probability_cal.csv'))
			for index,row in prob_data.iterrows():
				probabilities = []
				for element in row[1:np.size(row)-1]:
					probabilities.append(element)
				print probabilities
				highest = max(probabilities)
				top3_dept_explaining_tt.set_value(row[0],'Highest Prob',highest/100)
				print 'highest',highest
				probabilities.remove(highest)
				second_highest = max(probabilities)
				top3_dept_explaining_tt.set_value(row[0],'Second highest Prob',second_highest/100)
				print 'second_highest',second_highest
				probabilities.remove(second_highest)
				third_highest = max(probabilities)
				top3_dept_explaining_tt.set_value(row[0],'Third highest Prob',third_highest/100)
			print top3_dept_explaining_tt

		elif choice == 14:
			test_data = pd.read_csv(os.path.join(cwd,'test.csv'))
			test_data = test_data.fillna('missing')
			def weekday_num(input_val):
				dict = {'Friday':5,'Monday':1,'Tuesday':2,'Wednesday':3,'Thursday':4,'Saturday':6,'Sunday':7}
				return dict[input_val]
			test_data['Weekday_num'] = test_data['Weekday'].map(weekday_num)
			visit_department_distribution_test = pd.pivot_table(test_data,values='ScanCount',rows=['VisitNumber'],cols='DepartmentDescription',aggfunc=np.sum,fill_value = 0)
			print visit_department_distribution_test.count()

			weekday_dist_test = pd.pivot_table(test_data,values='ScanCount',rows=['VisitNumber'],cols='Weekday',aggfunc=np.size,fill_value = 0)
			print weekday_dist_test.count()

			department_per_visit_test= pd.DataFrame(test_data.groupby(['VisitNumber'],axis= 0)['DepartmentDescription'].nunique())
			department_per_visit_test.columns = ['Number_of_department']
			print department_per_visit_test.count()

			avg_finelinenumb_per_visit = pd.DataFrame(test_data.groupby(['VisitNumber'],axis= 0)['FinelineNumber'].mean())
			avg_finelinenumb_per_visit.columns = ['Avg_finelinenumber']

			classifier_input_test_data = pd.concat([visit_department_distribution_test,weekday_dist_test,department_per_visit_test,avg_finelinenumb_per_visit], axis=1, join_axes=[visit_department_distribution_test.index])
			print classifier_input_test_data.count()

			#visit_department_distribution_test = pd.pivot_table(test_data,values='ScanCount',rows='VisitNumber',cols='DepartmentDescription',aggfunc=len,fill_value = 0)
			#visit_department_distribution_test = pd.pivot_table(test_data,rows='VisitNumber',cols='DepartmentDescription',fill_value = 0)

			# visit_numbers = pd.unique(test_data.VisitNumber)
			# departments = pd.unique(test_data.DepartmentDescription)
			#
			# visit_department_distribution_test = pd.DataFrame(columns = departments)
			# for visit in visit_numbers:
			# 	print 'visit number is :',visit
			# 	sub_data = test_data[(test_data.VisitNumber == visit)]
			# 	for deps in departments:
			# 		if len(sub_data[(sub_data.DepartmentDescription == deps)])>0:
			# 			visit_department_distribution_test.set_value(visit,1,deps)
			# 		else:
			# 			visit_department_distribution_test.set_value(visit,0,deps)

			# all_visit_numbers = pd.unique(test_data.VisitNumber)
			# visit_numbers_in_pivot_data = pd.read_csv(os.path.join(cwd,'output_with_headers.csv'))
			# visit_numbers_in_pivot = pd.unique(visit_numbers_in_pivot_data.VisitNumber)
			# missing_visits = []
			# for entry in all_visit_numbers:
			# 	if entry not in visit_numbers_in_pivot:
			# 		missing_visits.append(entry)
			# print missing_visits


			#print visit_department_distribution_test.columns
			# print np.size(pd.unique(test_data.VisitNumber))

			#(pd.DataFrame(pd.unique(test_data.VisitNumber))).to_csv('list_of_visitnumbers_in_test.csv',sep=',')





		elif choice==20:
			#(pd.DataFrame(pd.unique(data.TripType))).to_csv('Unique_trip_types.csv',sep = ',',index = False)
			#share_of_trip_type.to_csv('TripType_visitnumber_unique.csv',sep = ',')
			#share_of_trip_type_weekday_weekend.to_csv('TripType_weekday_weekend_visitnumber_unique.csv',sep=',')
			#products_departments.to_csv('Unique products per department.csv',sep = ',')
			#department_triptype_pivot.to_csv('DepartmentDescription trip Type visit number frequency pivot table.csv',sep=',')
			#department_finelinenum_pivot.to_csv('DepartmentDescription finelinenumber visit number frequency pivot table.csv',sep=',')
			#department_weekday_pivot.to_csv('DepartmentDescription Weekday visit number frequency pivot table.csv',sep=',')
			#Weekday_trip_type_pivot.to_csv('TripType Weekday visit number frequency pivot table.csv',sep=',')
			#visit_department_distribution.to_csv('Visit_department_scancount_sum.csv',sep=',')
			#visit_department_distribution_test.to_csv('Visit_department_scancount_sum_test.csv',sep=',')
			#dep_trip_probability_cal.to_csv('dep_triptype_probability_cal.csv',sep=',')
			#pd.DataFrame(list_of_departments).to_csv('list of departments.csv',sep=',')
			#pd.DataFrame(missing_visits).to_csv('missing visit numbers.csv',sep=',')
			#top3_dept_explaining_tt.to_csv('top3 department explaining triptype.csv',sep=',')
			#triptype_department_distribution_counts.to_csv('Triptype_department_distribution_counts.csv',sep=',')
			classifier_input_train_data.to_csv('classifier_input_train_data.csv',sep=',')
			classifier_input_test_data.to_csv('classifier_input_test_data.csv',sep=',')




understand_data([1,2,3,4,14,20])




#References
#1 - http://stackoverflow.com/questions/15411158/pandas-countdistinct-equivalent
#2 - http://pandas.pydata.org/pandas-docs/stable/reshaping.html
