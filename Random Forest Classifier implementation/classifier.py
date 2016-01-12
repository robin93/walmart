import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv as csv
import os
from sklearn.ensemble import RandomForestClassifier

cwd = os.getcwd()
train_data = pd.read_csv(os.path.join(cwd,'classifier_input_train_data.csv'))
test_data = pd.read_csv(os.path.join(cwd,'classifier_input_test_data.csv'))

print train_data.count()
print test_data.count()


clf = RandomForestClassifier(n_estimators= 500, max_depth = 60)

print np.shape(train_data)

test_features = test_data.columns[1:77]
#print 'unique triptype in train data\n',np.sort(pd.unique(train_data.TripType))

# features = train_data.columns[3:71]
print 'training.....'
clf.fit(train_data[test_features],train_data['TripType'])

#test_features = test_data.columns[1:80]
print test_features
# # #print test_data
print 'predicting...'
headers = ['TripType_3','TripType_4','TripType_5','TripType_6','TripType_7','TripType_8','TripType_9','TripType_12','TripType_14','TripType_15','TripType_18','TripType_19','TripType_20','TripType_21','TripType_22','TripType_23','TripType_24','TripType_25','TripType_26','TripType_27','TripType_28','TripType_29','TripType_30','TripType_31','TripType_32','TripType_33','TripType_34','TripType_35','TripType_36','TripType_37','TripType_38','TripType_39','TripType_40','TripType_41','TripType_42','TripType_43','TripType_44','TripType_999']
pred = clf.predict_proba(test_data[test_features])
# print pred
# (pd.DataFrame(pred)).to_csv('pred.csv',sep=',')
prediction = pd.DataFrame(pred,columns = headers)
# prediction = pd.DataFrame(clf.predict_proba(test_data[test_features]),columns = headers)
print 'done predicting...'
print prediction

final_output = pd.concat([pd.DataFrame(test_data['VisitNumber']),prediction],axis =1)

# # print final_output
# # #
final_output.to_csv('prediction_output_addfeatures_500_depth60.csv',sep=',',index = False)
