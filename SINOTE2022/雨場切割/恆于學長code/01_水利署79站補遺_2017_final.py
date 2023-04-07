#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import os
import os.path
import plotly 
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import datetime


# In[6]:


file_list = []
file_new_name = []
def getfilepath(filepath):
    for root,dirs,files in os.walk(filepath): 
# root 為檔案路徑位置
# dirs 為list，為該文件夾中所有目錄名字
# files 為list，為該文件夾中所有文件
        for name in files:
            if ("歷史降雨事件參數" in name):
                os.remove(os.path.join(root, name))
        for filepath in files:
#            print(os.path.join(root,filepath))
            file_list.append(os.path.join(root,filepath))
            a = os.path.split(filepath)
            b = a[1]
            b = b[0:-4]
            file_new_name.append(b)
    return file_list,file_new_name


# In[ ]:





# In[7]:


getfilepath(r"D:\NTNU_SUMMER\SOP_雨場切割\雨場資料_V2\01_水利署79站補遺_2017_final")


# In[ ]:





# In[8]:


result = pd.DataFrame()
result_rain = []
for file in range(len(file_list)):
    filepath = file_list[file]
    df1 = pd.read_csv(filepath)
    df1 = df1.drop(columns = 'HQT')                #拿掉每日雨量
    df = np.split(df1,[1,4],axis = 1)              #切開DataFrame，然後分開存
    df_no = df[0]
    df_date = df[1]
    df_date.columns = ['year','month','day']       #轉成datetime格式的方法之一
    df_date = pd.to_datetime(df_date)
    df_rain = df[2]
#     df_rain.index = df_date
    test = df_rain.values.ravel()                  #資料轉成array，然後轉成一維
    L = []
    L_rain = [0]
    r_start = 0
    r_end = 0
    L_end = 0
    L_max = 0
    L_sum = 0

    while any(x > 4 for x in test):               #判斷剩餘的list還有沒有大於4的數值
        for i in range(len(test)):                #找到第一個大於4的位置，往後全部存成一個新的list
            if test[i] >= 4:
                first = i
                break

        LL = test[first:]
        #print(LL)
        #print(L)
        
        if sum(LL) <= sum(L):                      #若取到最後一筆資料，避免進入無限迴圈
            break
        L = []

        for j in range(len(LL)):
            if LL[j] >= 4:
                L.append(LL[j])
                if L_max < LL[j]:
                    L_max = LL[j]
            else:
                ii = LL[ j + 1: j + 6]
                if all(jj < 4 for jj in ii):       #判斷是否連續6筆資料都小於門檻值
                    L_end = L_end + first + j
                    test = test[(first + j) : ]
                    break
                else:
                    L.append(LL[j])                #如果取到最到一筆資料，結束有Bug

        if L_sum < sum(L):
            L_sum = sum(L)
            L_rain = L
            r_end = L_end-1    
            r_start = L_end-len(L_rain)
#     print(filepath)
#     print(L_rain)
    d = {'index':file,'ID':file_new_name[file],'站號':df_no.values[0],'S_date':df_date[0],'E_date':df_date[len(df_date)-1],'降雨延時':len(L_rain),'最大降雨量':L_max,
         '總降雨量':L_sum,'S_rain':r_start,'E_rain':r_end}
    df_test = pd.DataFrame(data = d)
    result = pd.concat([result,df_test],axis =0)
    result_rain.append(L_rain)
    
print("Done")


# In[9]:


df_L_rain = pd.DataFrame(np.array([result_rain]))    #同一個list存進單格
df_L_rain = df_L_rain.T                              #行列互換
df_L_rain = df_L_rain.reset_index()
rain_all = pd.merge(result,df_L_rain,on='index')
rain_all.columns = ['index','事件ID','測站站號','起始日期','結束日期','降雨延時','最大降雨量','總降雨量','降雨延時開始','降雨延時結束','rain_detail']
rain_all = rain_all.set_index('index')

rain_all.to_excel(r"D:\NTNU_SUMMER\SOP_雨場切割\雨場資料_V2\降雨延時_統計.xls")

print("Done")


# In[10]:


for i in range(len(rain_all.rain_detail)):
    j = rain_all.降雨延時[i]
    #排除不符合降雨延時定義的資料
    if j > 1:
        #取出事件始末時間
        start = datetime.datetime.strptime(str(rain_all.起始日期[i]),"%Y-%m-%d %H:%M:%S")
        end = datetime.datetime.strptime(str(rain_all.結束日期[i]),"%Y-%m-%d %H:%M:%S")
        #分別抓出從start到end的每一時間段(天)
        date_generated = [start + datetime.timedelta(days = x) for x in range(0, (end-start).days)]
        date_generated.append(end + datetime.timedelta())
        
        #指存取事件始末時間的年月日，不存時分秒
        date_all = []
        for date in date_generated:
            qq = (date.strftime("%Y-%m-%d"))
            date_all.append(str(qq))

        #用降雨延時開始的時間計算是在該事件的第幾天
        kk = int(rain_all.降雨延時開始[i])/24
        kk = int(kk)
        ttl = range(120)
        #X軸Y軸長度
        rain_width = ttl[rain_all.降雨延時開始[i] : (rain_all.降雨延時結束[i]+1)]
        rain_height = rain_all.rain_detail[i]
        #累積雨量
        rain_total = []
        total = 0
        for k in range(len(rain_width)):
            q = rain_height[k]
            total += q
            rain_total.append(total)

        # Create figure with secondary y-axis
        fig = make_subplots(specs=[[{"secondary_y": True}]])

        # 加入資料，Y軸在左(secondary_y=False)
        fig.add_trace(
            go.Bar(y = rain_height, name="降雨強度"),
            secondary_y= False
        )
        #設定左側Y軸顯示的資訊
        fig.update_yaxes(secondary_y = False,title = "降雨強度(mm//hr)",
                         titlefont=dict(family="Microsoft JhengHei",size=14,color="black"))
        #加入資料，Y軸在右(secondary_y=True)
        fig.add_trace(
            go.Scatter(y=rain_total, name="累積降雨量"),
            secondary_y= True
        )
        #設定右側Y軸顯示的資訊
        fig.update_yaxes(ticks = 'outside',showgrid = False,secondary_y=True,title = '累積雨量(mm)',
                        titlefont=dict(family="Microsoft JhengHei",size=14,color="black"))
        fig.update_layout(
            #設定輸出的圖的標題
            title=go.layout.Title(
                text="降雨延時自 {0}:{1}點 開始".format(date_all[kk],ttl[rain_all.降雨延時開始[i]]),
                xref="paper",
                x=0,
                font=dict(
                    family="Microsoft JhengHei",
                    size=12,
                    color="black")
            ),
            #設定輸出的圖的圖例
            legend=go.layout.Legend(
                x=0,
                y=1,
                traceorder="normal",
                font=dict(
                    family="sans-serif",
                    size=12,
                    color="black"
                ),
                bgcolor="rgba(0,0,0,0)",
                bordercolor="rgba(0,0,0,0)",
            ),
            #設定X軸顯示的資訊
            xaxis=go.layout.XAxis(title='降雨延時(hr)',titlefont=dict(family="Microsoft JhengHei",size=14,color="black"))
        )
        
        #fig.show()
        #輸出圖檔為jpeg檔
        fig.write_image(r"D:\NTNU_SUMMER\SOP_雨場切割\雨場資料_V2\result\{}.jpeg".format(rain_all.事件ID[i]))
print("Done")


# In[ ]:




