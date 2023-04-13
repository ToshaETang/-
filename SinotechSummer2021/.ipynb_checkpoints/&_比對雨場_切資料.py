#!/usr/bin/env python
# coding: utf-8

# In[428]:


import pandas as pd
import numpy as np
import os
import os.path
from os import listdir
from os.path import isfile, isdir, join
import datetime
import time
import matplotlib.pyplot as plt
import plotly.express as px
import statsmodels
from pandas.plotting import register_matplotlib_converters  
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.seasonal import STL
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import openpyxl
import pytz
from datetime import datetime
from datetime import timedelta
import stl
from dateutil.parser import parse
from dateutil.parser import parse
from dateutil.tz import tzutc
import pytz
from tzlocal import get_localzone
import xlrd

#---------------------------------------去掉紅色警告-------------
from sklearn import metrics
import warnings
warnings.filterwarnings("ignore")


# In[429]:


################################################################
name = "新化林場"      #檔案名稱
Number = 6            #要抓幾場降雨
################################################################


# In[430]:


df = pd.read_excel(r'C:\Users\Tosha.E.T\Desktop\Sinotech\708\{}_分析資料.xlsx'.format(name))    #雨場切割

s_t = []                                      #降雨開始時間
e_t = []                                      #降雨結束時間
t=0
List = []
for i in range(len(df)):
    List.append(i)
for i in range(len(df)):
    for j in range(i+1,len(df)):
        if df.總降雨量[i]<df.總降雨量[j]:
            t=df.總降雨量[i]
            df.總降雨量[i]=df.總降雨量[j]
            df.總降雨量[j]=t
            m=List[i]
            List[i]=List[j]
            List[j]=m

for i in range(Number):
    s_t.append(df.S_time[List[i]])
    e_t.append(df.E_time[List[i]])        
for i in range(len(s_t)):
    s_t[i] = pd.to_datetime(s_t[i])
    e_t[i] = pd.to_datetime(e_t[i])
    
for i in range(len(s_t)):
    s_t[i] = s_t[i].replace(tzinfo=None)
    e_t[i] = e_t[i].replace(tzinfo=None)

for i in range(len(s_t)):   
    print(i+1," ", s_t[i],"~", e_t[i])


# In[431]:


df2 = pd.read_excel(r'C:\Users\Tosha.E.T\Desktop\Sinotech\708\{}_H.xlsx'.format(name))
# df2.head()


# In[432]:


s_t_2 = []
e_t_2 = []
n = []
k = []
for i in range(len(s_t)):
    for j in range(len(df2)):
        if (str(df2.datetime[j])[0:16]) == (str(s_t[i])[0:16]):
            s_t_2.append(str(df2.datetime[j])[0:16])
            n.append(j)
        if (str(df2.datetime[j])[0:16]) == (str(e_t[i])[0:16]):
            e_t_2.append(str(df2.datetime[j])[0:16])
            k.append(j)


# In[433]:


result_A= []  #datetime
result_B= []  #原始資料
result_C= []  #水位1
result_D= []  #蓄水體積
result_E= []  #百分比
result_F= []  #出流原始資料
result_G= []  #水位2
result_H= []  #流量
result_I= []  #氣象站
result_J= []  #我們自己的

for i in range(len(n)):
    for j in range(n[i]-6,k[i]+1+12):
        result_A.append(df2.datetime[j])
        result_B.append(df2.原始資料[j]/6)               #林先生說要除6
        result_C.append(df2.水位1[j]/6)
        result_D.append(df2.蓄水體積[j]/6)
        result_E.append(df2.百分比[j]/6)
        result_F.append(df2.出流原始資料[j]/6)
        result_G.append(df2.水位2[j]/6)
        result_H.append(df2.流量[j]/6)
        result_I.append(df2.氣象站[j])
        result_J.append(df2.我們自己的[j])
    result_A.append("")
    result_B.append("")             
    result_C.append("")
    result_D.append("")
    result_E.append("")
    result_F.append("")
    result_G.append("")
    result_H.append("")
    result_I.append("")
    result_J.append("")
        
d = {
    "datetime":result_A,
    "原始資料":result_B,
    "水位1":result_C,
    "蓄水體積":result_D,
    "百分比":result_E,
    "出流原始資料":result_F,
    "水位2":result_G,
    "流量":result_H,
    "氣象站":result_I,
    "我們自己的":result_J
    }

Index = []
result = pd.DataFrame(d)
for i in range(1,len(result_A)+1):
    Index.append(str(i))   
result.index = Index 
result.columes = ["datetime","原始資料","水位1","蓄水體積","百分比","出流原始資料","水位2","流量","氣象站","我們自己的"]
print(result)

result.to_excel(r'C:\Users\Tosha.E.T\Desktop\Sinotech\708\result_{}.xlsx'.format(name))
print("---------------------------------------")
print("result_{}.xlsx".format(name),"已儲存")

