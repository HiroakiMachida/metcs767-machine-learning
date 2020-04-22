#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 07:33:23 2020

@author: hiroakimachida
"""
import os
import csv

topix17 = ["AUTT","COMR","TRNS","ELPL","FOOD","MCHR","RETI","STLN","ELCA","ENRE","PHMS","REAL","CONM","FUND","FINA","RAWM"]

def generate_data(topix17, year):
    for i, etf in enumerate(topix17):
        with open('data/original_data', mode='r') as read_file:
            with open('data/'+year+'/original_data.'+etf, mode='w') as write_file:
                with open('data/'+year+'/original_data.'+etf+'.date', mode='w') as write_file2:
                    csv_reader = csv.reader(read_file)
                    csv_writer = csv.writer(write_file)
                    csv_writer2 = csv.writer(write_file2)
                    for row in csv_reader:
                        if year+"0101"<=row[0] and row[0]<=year+"1231" and row[i+1]:
                            sub_row1 = [1] if float(row[i+1]) > 0 else [0]
                            sub_row2 = []
                            for e in row[len(topix17)+1:]:
                                sub_row2.append(str(e))
                            csv_writer.writerow(sub_row1+sub_row2)
                            csv_writer2.writerow([row[0]])


def generate_data_set(topix17):
    for i in range(2000,2022): #2000 to 2021
        yyyy = str(i)
        print("generating data set "+yyyy)
        data_dir = 'data/'+yyyy
        if not os.path.isdir(data_dir):
            os.mkdir(data_dir)
        generate_data(topix17, yyyy)

generate_data_set(topix17)
                




