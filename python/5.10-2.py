# python 5.10-2.py
import pandas as pd
import os
from os import listdir
import arcpy

data_path=r"C:\Users\Tosha.E.T\Aland\arcpy_data\ols_table"

for i in listdir(data_path):
    if i.endswith(".csv"):
        os.rename(os.path.join(data_path,i), i[0:i.index('csv')]+'.dbf' )                              #路徑(絕對)(現在是相對) 名字


import pandas as pd
import os
from os import listdir
import arcpy
data_path=r"C:\Users\Tosha.E.T\Documents\ArcGIS\Projects\5.10\arcpy_data\ols_table"
for i in listdir(data_path):
    if i.endswith(".dbf"):
        input_data_path=os.path.join(data_path,i)
        output_data=os.path.join(data_path,i[0:i.index('.dbf')]+'.csv')
        arcpy.conversion.TableToTable(input_data_path,
                                      data_path, 
                                      output_data)