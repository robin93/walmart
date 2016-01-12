import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv as csv
import os
from sklearn.ensemble import RandomForestClassifier

cwd = os.getcwd()
train_data = pd.read_csv(os.path.join(cwd,'Visit_department_scancount_sum.csv'))
test_data = pd.read_csv(os.path.join(cwd,'Visit_department_scancount_sum_test.csv'))

print test_data
print train_data

clf = RandomForestClassifier(n_estimators=50, max_depth = None, max_features = 10)


print np.shape(train_data)

test_features = test_data.columns[1:72]
# features = train_data.columns[3:71]
print 'training.....'
clf.fit(train_data[test_features],train_data['TripType'])
#
test_features = test_data.columns[1:72]
print test_features
# # #print test_data
print 'predicting...'
headers = ['TripType_3','TripType_4','TripType_5','TripType_6','TripType_7','TripType_8','TripType_9','TripType_12','TripType_14','TripType_15','TripType_18','TripType_19','TripType_20','TripType_21','TripType_22','TripType_23','TripType_24','TripType_25','TripType_26','TripType_27','TripType_28','TripType_29','TripType_30','TripType_31','TripType_32','TripType_33','TripType_34','TripType_35','TripType_36','TripType_37','TripType_38','TripType_39','TripType_40','TripType_41','TripType_42','TripType_43','TripType_44','TripType_999']
prediction1 = pd.DataFrame(clf.predict_proba(test_data[test_features]),columns = headers)

prediction2 = pd.read_csv(os.path.join(cwd,'bayes_output.csv'))
#prediction = pd.DataFrame(clf.predict_log_proba(test_data[test_features]),columns = headers)
# print 'done predicting...'
prediction = prediction1 + prediction2
print prediction

final_output = pd.concat([pd.DataFrame(test_data['VisitNumber']),prediction],axis =1)

# print final_output
# #
final_output.to_csv('randForest and bayes ensemble.csv',sep=',',index = False)
