#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 12:13:15 2020

@author: hiroakimachida
"""
import csv
import xgboost as xgb

topix17 = ["AUTT","COMR","TRNS","ELPL","FOOD","MCHR","RETI","STLN","ELCA","ENRE","PHMS","REAL","CONM","FUND","FINA","RAWM"]

"""
Train XGBoost and predict
input: training data file and prediction input data file
output: prediction result file
"""
def predict(train_year, sector):
    # read in data
    predict_year = str(int(train_year)+1)
    dtrain = xgb.DMatrix(f"data/{train_year}/original_data.{sector}")
    dtest = xgb.DMatrix(f"data/{predict_year}/original_data.{sector}")
    # specify parameters via map
    param = {'max_depth':2, 'eta':1, 'objective':'reg:squarederror' }
    num_round = 2
    bst = xgb.train(param, dtrain, num_round)
    # make prediction
    preds = bst.predict(dtest)

    # store the prediction result to a csv file
    with open('data/'+predict_year+'/original_data.'+sector+'.date', mode='r') as read_file:
        with open('data/'+predict_year+'/original_data.'+sector+'.predict', mode='w') as write_file:
            csv_reader = csv.reader(read_file)
            csv_writer = csv.writer(write_file)
            for i,row in enumerate(csv_reader):
                csv_writer.writerow([row[0]]+[str(preds[i])])
    
    print(train_year, sector)
#    xgb.plot_importance(bst)
    return preds

"""
Execute training and predicting for all years and sectors
"""
def predict_all():
    for i in range(2008,2019): #2008 to 2019
        for sec in topix17:
            print("processing:",str(i),sec)
            predict(str(i), sec)

predict_all()