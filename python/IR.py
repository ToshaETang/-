#python IR.py
import numpy as np 
import pandas as pd
import csv

with open('data.csv', newline='') as csvfile:
    rows = csv.reader(csvfile,delimiter=',')
    for i in rows:
        print(i)