#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 15:16:39 2020

@author: hiroakimachida
"""

from sklearn.linear_model import LogisticRegression
import csv


"""

X, y = load_iris(return_X_y=True)
print("y")
print(y)
print("X")
print(X)
clf = LogisticRegression(penalty='l2', max_iter=100000).fit(X, y)

res = clf.predict(X[:3, :])
print("predict")
print("X[:2, :]")
print(X[:3, :].shape)
print(X[:3, :])
print("Result")
print(res)

res = clf.predict_proba(X[:3, :])
print("predict_proba")
print(res)
#clf.score(X, y)
"""

topix17 = ["AUTT","COMR","TRNS","ELPL","FOOD","MCHR","RETI","STLN","ELCA","ENRE","PHMS","REAL","CONM","FUND","FINA","RAWM"]
import numpy as np


def predict(train_year, sector):
    # read in data
    predict_year = str(int(train_year)+1)
    y = []
    X = []
    with open(f"data/{train_year}/original_data.{sector}", mode='r') as read_file:
        csv_reader = csv.reader(read_file)
        for row in csv_reader:
            y.append(row[0])
            X.append(np.array(row[1:]).astype(np.float))
    clf = LogisticRegression(penalty='l1', solver='liblinear').fit(X, y)

    # prediction
    X = []
    Y = []
    with open(f"data/{predict_year}/original_data.{sector}", mode='r') as read_file:
        csv_reader = csv.reader(read_file)
        for row in csv_reader:
            X.append(np.array(row[1:]).astype(np.float))
            Y.append(row[0])

    preds = clf.predict_proba(X)

    # store the prediction result to a csv file
    with open('data/'+predict_year+'/original_data.'+sector+'.date', mode='r') as read_file:
        with open('data/'+predict_year+'/original_data.'+sector+'.predict', mode='w') as write_file:
            csv_reader = csv.reader(read_file)
            csv_writer = csv.writer(write_file)
            for i,row in enumerate(csv_reader):
                csv_writer.writerow([row[0]]+[str(preds[i][1])])

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