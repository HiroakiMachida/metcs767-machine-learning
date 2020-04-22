#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 13:46:28 2020

@author: hiroakimachida
"""
import csv

topix17 = ["AUTT","COMR","TRNS","ELPL","FOOD","MCHR","RETI","STLN","ELCA","ENRE","PHMS","REAL","CONM","FUND","FINA","RAWM"]

preds = dict()
trade = dict()
prices = dict()
trade_result = dict()


for predict_year in range(2009,2020): #2008 to 2019
    for sector in topix17:
        with open('data/'+str(predict_year)+'/original_data.'+sector+'.predict', mode='r') as read_file:
            csv_reader = csv.reader(read_file)
            for row in csv_reader:
                if not row[0] in preds.keys():
                    preds[row[0]] = dict()
                preds[row[0]][sector]=row[1]    
    for date in preds:
        max = None
        for pred in preds[date]:
            if not max or abs(float(preds[date][max[0]])-0.5)<abs(float(preds[date][pred])-0.5):
                if float(preds[date][pred])-0.5 > 0:
                    max = (pred, 'BUY')
                else:
                    max = (pred, 'SELL')
        trade[date] = max            

with open('data/original_data', mode='r') as read_file:
    csv_reader = csv.reader(read_file)
    for row in csv_reader:
        if not row[0] in prices.keys():
            prices[row[0]] = dict()
        for i, sector in enumerate(topix17):
            if row[i+1]:
                prices[row[0]][sector]=float(row[i+1])

total_ret = float(1)

#trade = sorted(trade.items(), key=lambda x:str(x[0]))

for day in prices:
    if day in trade.keys():
        if trade[day][1] == 'BUY':
            print(day, trade[day][1], trade[day][0], prices[day][trade[day][0]])
            total_ret = total_ret * (1+prices[day][trade[day][0]])
            trade_result[day] = total_ret
        elif trade[day][1] == 'SELL':
            print(day, trade[day][1], trade[day][0], -prices[day][trade[day][0]])
            total_ret = total_ret * (1-prices[day][trade[day][0]])
            trade_result[day] = total_ret


with open('data/result', mode='w') as write_file:
    csv_writer = csv.writer(write_file)
    for row in trade_result:
        print(row, trade_result[row])
        csv_writer.writerow([row]+[trade_result[row]])



