import pandas as pd

#IMPORTING THE RAW CSV FILE
import csv as csv
import os
cwd = os.getcwd()
raw_data = pd.read_csv(os.path.join(cwd,'train.csv'))

###MAPPING FUNCTIONS
#Weekday conversion to numerical values
def weekday_num(input_val):
	dict = {'Friday':5,'Monday':1,'Tuesday':2,'Wednesday':3,'Thursday':4,'Saturday':6,'Sunday':7}
	return dict[input_val]

def weekday_weekend(input_val):
	dict = {'Friday':'Weekday','Monday':'Weekday','Tuesday':'Weekday','Wednesday':'Weekday','Thursday':'Weekday','Saturday':'Weekend','Sunday':'Weekend'}
	return dict[input_val]

###IMPLEMENTATION OF ENGINEERED FEATURES
raw_data['Weekday_num'] = raw_data['Weekday'].map(weekday_num)
raw_data['Weekend_Weekday'] = raw_data['Weekday'].map(weekday_weekend)




#Check for missing values
print 'Number of rows in the data are - ', len(raw_data)
print 'Number of non-null values by columns in the raw data :'
print raw_data.count()

#Replace of missing columns with word missing
raw_data = (raw_data['FinelineNumber']).fillna(0)
raw_data = raw_data.fillna('missing')

#check for missing values again after filling the missing values
print 'Number of rows in the data are - ', len(raw_data)
print 'Number of non-null values by columns in the raw data :'
print raw_data.count()

# ###WRITE THE MODIFIED FILE TO CSV
# raw_data.to_csv('modified_input_data.csv',sep = ',')
