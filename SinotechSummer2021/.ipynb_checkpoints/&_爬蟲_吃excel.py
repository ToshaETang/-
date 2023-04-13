#!/usr/bin/env python
# coding: utf-8

# In[30]:


import re
import os
import requests
import pandas as pd
import time
import random
from bs4 import BeautifulSoup
#-----------------------------------------------------------
DATE1 = input("請輸入起始日期(yyyy-mm-dd): ")
DATE2 = input("請輸入結束日期(yyyy-mm-dd): ")
#-----------------------------------------------------------
# ID=input("請輸入站點(C1R120): ")
# DATE1 = input("請輸入起始日期(yyyy-mm-dd): ")
# DATE2 = input("請輸入結束日期(yyyy-mm-dd): ")
#----------------------------------------------------------
M1=DATE1.split('-')[1]
D1=DATE1.split('-')[2]

Y=DATE1.split('-')[0]

M2=DATE2.split('-')[1]
D2=DATE2.split('-')[2]
#------------------------------------------------------------
df = pd.read_excel(r'C:\Users\Tosha.E.T\Desktop\Sinotech\811\站點編號.xlsx')
for i in range(len(df)):
    ID=df['站點編號'][i]
    M=[]
    D=[]
    
    st_no=[]
    yy=[]
    mm=[]
    dd=[]

    HQ01=[]
    HQ02=[]
    HQ03=[]
    HQ04=[]
    HQ05=[]
    HQ06=[]
    HQ07=[]
    HQ08=[]
    HQ09=[]
    HQ10=[]
    HQ11=[]
    HQ12=[]
    HQ13=[]
    HQ14=[]
    HQ15=[]
    HQ16=[]
    HQ17=[]
    HQ18=[]
    HQ19=[]
    HQ20=[]
    HQ21=[]
    HQ22=[]
    HQ23=[]
    HQ24=[]

#-------------------------------------------網址時間---------

    if int(M2)-int(M1)>1:
        for i in range(31-int(D1)+1):
            M.append(int(M1))
        for i in range(int(D1),32):
            D.append(i)

        for i in range(int(M1)+1,int(M2)):
            for j in range(1,32):
                M.append(i)
        for i in range(int(M1),int(M2)-1):
            for j in range(1,32):
                D.append(j)
            
        for i in range(int(D2)):
            M.append(int(M2))
        for i in range(1,int(D2)+1):
            D.append(i)        
########################################        
    elif int(M2)-int(M1)==1:
        for i in range(31-int(D1)+1):
            M.append(int(M1))
        for i in range(int(D1),32):
            D.append(i)
    
        for i in range(int(D2)):
            M.append(int(M2))
        for i in range(1,int(D2)+1):
            D.append(i)
########################################
    else:
        for i in range(int(D2)-int(D1)+1):
            M.append(int(M1))
        for i in range(int(D1),int(D2)+1):
            D.append(i)

#--------------------------------------------------------------

    for i in range(len(M)):
        Yy=Y
        if M[i]<10:
            Mm='0{}'.format(M[i])
        else:
            Mm=str(M[i])
    
        if D[i]<10:
            Dd='0{}'.format(D[i])
        else:
            Dd=str(D[i])
        
        url = r'https://e-service.cwb.gov.tw/HistoryDataQuery/DayDataController.do?command=viewMain&station={0}&stname=%25E4%25B8%258A%25E5%25BE%25B7%25E6%2596%2587&datepicker={1}-{2}-{3}#'.format(ID,Yy,Mm,Dd)          

        re = requests.get(url) 
        soup = BeautifulSoup(re.text, "html.parser")
        result = soup.find_all("td")
    
        RR = soup.find_all("head")
        t = str(RR).split(";")
        x = t[4].split("\"")
        y=x[1].split("-")

    
        st_no.append(y[0])
        dd.append(y[3]) 
        mm.append(y[2])
        yy.append(y[1])
    
        HQ01.append((str(result[20]).split())[0].split(">")[1])
        HQ02.append((str(result[37]).split())[0].split(">")[1])
        HQ03.append((str(result[54]).split())[0].split(">")[1])
        HQ04.append((str(result[71]).split())[0].split(">")[1])
        HQ05.append((str(result[88]).split())[0].split(">")[1])
        HQ06.append((str(result[105]).split())[0].split(">")[1])
        HQ07.append((str(result[122]).split())[0].split(">")[1])
        HQ08.append((str(result[139]).split())[0].split(">")[1])
        HQ09.append((str(result[156]).split())[0].split(">")[1])
        HQ10.append((str(result[173]).split())[0].split(">")[1])
        HQ11.append((str(result[190]).split())[0].split(">")[1])
        HQ12.append((str(result[207]).split())[0].split(">")[1])
        HQ13.append((str(result[224]).split())[0].split(">")[1])
        HQ14.append((str(result[241]).split())[0].split(">")[1])
        HQ15.append((str(result[258]).split())[0].split(">")[1])
        HQ16.append((str(result[275]).split())[0].split(">")[1])
        HQ17.append((str(result[292]).split())[0].split(">")[1])
        HQ18.append((str(result[309]).split())[0].split(">")[1])
        HQ19.append((str(result[326]).split())[0].split(">")[1])
        HQ20.append((str(result[343]).split())[0].split(">")[1])
        HQ21.append((str(result[360]).split())[0].split(">")[1])
        HQ22.append((str(result[377]).split())[0].split(">")[1])
        HQ23.append((str(result[394]).split())[0].split(">")[1])
        HQ24.append((str(result[411]).split())[0].split(">")[1])
 
        d = {
            "st_no":st_no,
            "yy":yy,
            "mm":mm,
            "dd":dd,
            "HQ01":HQ01,
            "HQ02":HQ02,
            "HQ03":HQ03,
            "HQ04":HQ04,
            "HQ05":HQ05,
            "HQ06":HQ06,
            "HQ07":HQ07,
            "HQ08":HQ08,
            "HQ09":HQ09,
            "HQ10":HQ10,
            "HQ11":HQ11,
            "HQ12":HQ12,
            "HQ13":HQ13,
            "HQ14":HQ14,
            "HQ15":HQ15,
            "HQ16":HQ16,
            "HQ17":HQ17,
            "HQ18":HQ18,
            "HQ19":HQ19,
            "HQ20":HQ20,
            "HQ21":HQ21,
            "HQ22":HQ22,
            "HQ23":HQ23,
            "HQ24":HQ24,
            }
    
        time.sleep(random.uniform(0,0.5))
        print("WAIT..................",i) 

    print("done~~")
    df_test=(pd.DataFrame(data = d))


    N = ID+"-"+y[1]
    df_test.to_csv(r'C:\Users\Tosha.E.T\Desktop\Sinotech\811\{}.csv'.format(N),index=False)     #要改存檔路徑
    print(ID, "  SAVE!!!")

print("  ")    
print("-----------------------------------------------------------------------")    
print("FINISH")

