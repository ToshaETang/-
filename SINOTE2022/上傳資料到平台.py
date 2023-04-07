import pandas as pd
import numpy as np
import json
import requests
from pandas.io.json import json_normalize
import datetime
from datetime import timedelta
import time
from tzlocal import get_localzone
import warnings
warnings.filterwarnings('ignore')
#--------------------------------------------
print("645") 
df_ID = pd.read_csv(r"..\設備編號.csv")

# L = []
# N = []
# E = []

# F1 = []
# F2 = []
# F3 = []
# F4 = []
# F5 = []
# F6 = []
# F7 = []

# for i in range (len(df_ID['ID'])):
#     print(df_ID['ID'][i]) 
#     df = request("{}".format(df_ID['ID'][i]))    
#     df['time']=pd.DataFrame(df['time'])    
#     df['time'] = pd.to_datetime(pd.Series(df['time']))   
#     TT = (df['time'][99] + timedelta(hours=8)).strftime("%Y-%m-%d %H:%M:%S")
#     N.append(df_ID['ID'][i])  #編號
#     L.append(TT)  #時間
#     E.append(str(df['entry_id'][99]).split(" "))
#     F1.append(str(df['field1'][99]).split(" "))
#     F2.append(str(df['field2'][99]).split(" "))
#     F3.append(str(df['field3'][99]).split(" "))
#     F4.append(str(df['field4'][99]).split(" "))
#     F5.append(str(df['field5'][99]).split(" "))
#     F6.append(str(df['field6'][99]).split(" "))
#     F7.append(str(df['field7'][99]).split(" "))
#     print("------------------------------")

    
    
# result = pd.DataFrame()
# for i in range (len(N)):
#     d = {"設備":N[i],
#         "Time":L[i],
#         "entry_id":E[i],
#         "field1":F1[i],
#         "field2":F2[i],
#         "field3":F3[i],
#         "field4":F4[i],
#         "field5":F5[i],
#         "field6":F6[i],
#         "field7":F7[i],
#         }    

#     df_test = pd.DataFrame(data = d, index=[0])
#     result = pd.concat([result, df_test],axis =0)

# result.to_csv(r'C:\TET\SINOTE2022\TRY_水位濁度.csv', index=False,encoding='utf_8_sig')
print(df_ID)   
