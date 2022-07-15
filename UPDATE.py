#------------------------------------------------
import pandas as pd
import numpy as np
import json
import requests
from pandas.io.json import json_normalize
import datetime
from datetime import timedelta
import time
from tzlocal import get_localzone
import pymssql
import pyodbc

import re
import os
from bs4 import BeautifulSoup
import schedule 
import warnings
warnings.filterwarnings('ignore')
#-----------------------------------------------------------------------
def request(device_post_api):
    url = "https://api.thingspeak.com/channels/{}/feeds.json".format(device_post_api)
    data = requests.get(url)
    data_json = json.dumps(data.json())
    info = json.loads(data_json)
    info_val = info["feeds"]
    info_lat_lon = info["channel"]
    df = json_normalize(info_val)    
    df = df.rename({'created_at': 'time'}, axis=1)
    return (df.tail(1))

#########################################
def UpdatePQ(ID, PWD,PQ, DT, VALUES):
    url1 = r'http://59.120.114.172:8080/APP_SWCB_IFEM/api/User/GetToken'
    dt1 = {"API_USER_ID": "{}".format(ID), "API_USER_PWD": "{}".format(PWD)}
    r1 = requests.post(url1, data =dt1)
    jr1 = json.loads(r1.text)    
    T = jr1["Token"]   
    url3 = 'http://59.120.114.172:8080/APP_SWCB_IFEM/api/Stations/UpdateStationSensorPQ'
    dt3 = {
        "Token":"{}".format(T),
        "Data":
        [
            {"PQguid": "{}".format(PQ),
             "DateTime":"{}".format(DT),
             "VALUES": "{}".format(VALUES)
            }
        ]
    } 
    r3 = requests.post(url3, json = dt3) 
    print(r3.text)
#-----------------------------------------------------------------------

df_ID = pd.read_excel(r"大表.xlsx")
dfid = df_ID['設備編號'].drop_duplicates()
df = dfid
conn = pyodbc.connect(Driver="{SQL Server Native Client 11.0};",Server="LAPTOP-9VKLPUUE\SQLEXPRESS;",Datebase="UPDATE;",UID="sinotech;",PWD="sinotech;" )
print("連接上資料庫!!!")

L = []
N = []
E = []
F1 = []
F2 = []
F3 = []
F4 = []
F5 = []
F6 = []
F7 = []

print("---水位濁度表開始更新---")
for i in range (len(df_ID['設備編號'])):
    try:
        df = request("{}".format(dfid[i]))
    except:
        continue   
    print(dfid[i]) 
    df['time']=pd.DataFrame(df['time'])    
    df['time'] = pd.to_datetime(pd.Series(df['time']))   
    TT = (df['time'].iloc[-1] + timedelta(hours=8)).strftime("%Y-%m-%d %H:%M:%S")
    N.append(dfid[i])  #編號
    L.append(TT)  #時間
    E.append(str(df['entry_id'].iloc[-1]).split(" "))
    F1.append(str(df['field1'].iloc[-1]).split(" "))
    F2.append(str(df['field2'].iloc[-1]).split(" "))
    F3.append(str(df['field3'].iloc[-1]).split(" "))
    F4.append(str(df['field4'].iloc[-1]).split(" "))
    F5.append(str(df['field5'].iloc[-1]).split(" "))
    F6.append(str(df['field6'].iloc[-1]).split(" "))
    F7.append(str(df['field7'].iloc[-1]).split(" "))

dt = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
result = pd.DataFrame()
for i in range (len(N)):
    d = {"設備":N[i],
        "Time":L[i],
        "entry_id":E[i],
        "field1":F1[i],
        "field2":F2[i],
        "field3":F3[i],
        "field4":F4[i],
        "field5":F5[i],
        "field6":F6[i],
        "field7":F7[i],
        }
    qq1 = str(N[i])
    qq2 = str(L[i])
    qq3 = (E[i])
    qq3 = int(qq3[0])
    qq4 = (F1[i])
    qq4 = float(qq4[0])
    qq5 = (F2[i])
    qq5 = float(qq5[0])
    qq6 = (F3[i])
    qq6 = float(qq6[0])
    qq7 = (F4[i])
    qq7 = float(qq7[0])
    qq8 = (F5[i])
    qq8 = float(qq8[0])
    qq9 = (F6[i])
    qq9 = float(qq9[0])
    qq10 = (F7[i])
    qq10 = float(qq10[0])
        
    df_test = pd.DataFrame(data = d, index=[0])
    result = pd.concat([result, df_test],axis =0)

    try:
        cursor = conn.execute("insert into originaldd (設備,Time,entry_id,field1,field2,field3,field4,field5,field6,field7,upload_time) values(?,?,?,?,?,?,?,?,?,?,?)",(qq1,qq2,qq3,qq4,qq5,qq6,qq7,qq8,qq9,qq10,dt))
        conn.commit()
        Z = True
    except:
        Z = False
        pass

result.to_excel(r'水位濁度.xlsx', index=False,encoding='utf_8_sig')
print("---水位濁度表已更新---")

if Z:
    print("---原始資料已上傳---")
else:    
    print("---原始資料上船失敗---")


R = 0
NN = 0
print("---大表開始更新---")   
df_B = pd.read_excel(r"大表.xlsx")
df_V = pd.read_excel(r'水位濁度.xlsx')
df_V['Time'] = pd.to_datetime(pd.Series(df_V['Time'])) 
for i in range(len(df_B['OBS_Type'])):
    if (df_B['OBS_Type'][i]=="水位"):
        for j in range(len(df_V['設備'])):
            if df_V['設備'][j] == df_B['設備編號'][i]:
                if str(df_B['entry_id'][i])==str(df_V['entry_id'][j]):
                    print(str(df_V['設備'][j]) +" 水位 沒有更新")
                    NN=NN+1
                    continue
                else:
                    df_B['value'][i] = df_V['field5'][j]
                    K = df_V['Time'][j].strftime("%Y%m%d%H%M%S")
                    df_B['time'][i] = str(K)
                    df_B['entry_id'][i] = str(df_V['entry_id'][j])
                    print(str(df_V['設備'][j]) +" 水位 已更新")
                    try:
                        df_B['true value'][i] = float(df_B['校正係數A'][i]) - (df_V['field5'][j]*float(df_B['校正係數B'][i]))     
                    except:
                        df_B['true value'][i] = 0

                    try:
                        UpdatePQ("Sinotech","Sinotech!Org@swcb","{}".format(df_B['pquid'][i]),"{}".format(df_B['time'][i]),"{}".format(df_B['true value'][i]))
                        R = R+1
                    except:
                        NN = NN+1
                        pass

                    try:
                        dt = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                        cursor = conn.execute("insert into updateV (ID,value_time,sensor_type,value,entry_id,upload_time) values(?,?,?,?,?,?)",(str(df_B['設備編號'][i]),df_B['time'][i],"W",df_B['true value'][i],df_B['entry_id'][i],dt))
                        conn.commit()
                        print(str(df_V['設備'][j])+" 水位已放入資料庫")
                    except:
                        print(str(df_V['設備'][j])+" 水位放不進去")
                        pass

            
    elif (df_B['OBS_Type'][i]=="濁度"):
        for j in range(len(df_V['設備'])):
            if df_V['設備'][j] == df_B['設備編號'][i]:
                if str(df_B['entry_id'][i])==str(df_V['entry_id'][j]):
                    print(str(df_V['設備'][j]) +" 濁度 沒有更新")
                    NN = NN+1
                    continue
                else:
                    df_B['value'][i] = df_V['field6'][j]
                    K = df_V['Time'][j].strftime("%Y%m%d%H%M%S")
                    df_B['time'][i] = str(K)
                    df_B['entry_id'][i] = str(df_V['entry_id'][j])
                    print(str(df_V['設備'][j]) +" 濁度 已更新")
                    try:
                        df_B['true value'][i] = float(df_B['校正係數A'][i])*np.log(df_V['field6'][j]) + float(df_B['校正係數B'][i])
                    except:
                        df_B['true value'][i] = 0   

                    try:
                        UpdatePQ("Sinotech","Sinotech!Org@swcb","{}".format(df_B['pquid'][i]),"{}".format(df_B['time'][i]),"{}".format(df_B['true value'][i]))
                        R = R+1
                    except:
                        NN = NN+1
                        pass  
                    try:
                        dt = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                        cursor = conn.execute("insert into updateV (ID,value_time,sensor_type,value,entry_id,upload_time) values(?,?,?,?,?,?)",(str(df_B['設備編號'][i]),df_B['time'][i],"S",df_B['true value'][i],df_B['entry_id'][i],dt))
                        conn.commit()
                        print(str(df_V['設備'][j])+" 濁度已放入資料庫")
                    except:
                        print(str(df_V['設備'][j])+" 濁度放不進去")
                        pass
                                  
DF = df_B
DF.to_excel(r'大表.xlsx', index=False,encoding='utf_8_sig')
print("---大表已更新---")



print("============================================")
print("共上傳 {} 筆資料".format(str(R)))
print("{} 筆資料不上傳".format((NN)))
print("============================================")