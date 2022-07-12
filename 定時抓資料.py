import pyodbc
import re
import os
import requests
import pandas as pd
import time
import random
from bs4 import BeautifulSoup
import pymssql
import schedule
import datetime 
#----------------------------------------------------------
def job():
    conn = pyodbc.connect(Driver="{SQL Server Native Client 11.0};",Server="LAPTOP-9VKLPUUE\SQLEXPRESS;",Datebase="CWB;",UID="sinotech;",PWD="sinotech;" )
    cursor = conn.cursor()

    td=datetime.date.today()
    DATE1=td - datetime.timedelta(days=2)
    DATE1=DATE1.strftime('%Y-%m-%d')
 
    M1=DATE1.split('-')[1]
    D1=DATE1.split('-')[2]

    Y=DATE1.split('-')[0]
#------------------------------------------------------------
    df = pd.read_excel(r'C:\Users\Tosha.E.T\Desktop\Sinotech\811\站點編號(爬蟲用).xlsx')
    for i in range(len(df)):
        ID=df['站點編號'][i]

        N = ('{}'.format(ID))
        cursor.execute('''
                       IF NOT EXISTS(select * from dbo.sysobjects where id = object_id( 'dbo.{0}' ) and OBJECTPROPERTY(id, 'IsUserTable' )=1)
                       begin
                       CREATE TABLE {1} (站點編號 varchar(10) not null,  
                       年 int not null,
                       月 int not null,
                       日 int not null,
                       HQ01 float ,
                       HQ02 float ,
                       HQ03 float ,
                       HQ04 float ,
                       HQ05 float ,
                       HQ06 float ,
                       HQ07 float ,
                       HQ08 float ,
                       HQ09 float ,
                       HQ10 float ,
                       HQ11 float ,
                       HQ12 float ,
                       HQ13 float ,
                       HQ14 float ,
                       HQ15 float ,
                       HQ16 float ,
                       HQ17 float ,
                       HQ18 float ,
                       HQ19 float ,
                       HQ20 float ,
                       HQ21 float ,
                       HQ22 float ,
                       HQ23 float ,
                       HQ24 float)
                       end
                       '''.format(N,N))
        conn.commit()
            
        url = r'https://e-service.cwb.gov.tw/HistoryDataQuery/DayDataController.do?command=viewMain&station={0}&stname=%25E4%25B8%258A%25E5%25BE%25B7%25E6%2596%2587&datepicker={1}-{2}-{3}#'.format(ID,Y,M1,D1)       

        re = requests.get(url) 
        soup = BeautifulSoup(re.text, "html.parser")
        result = soup.find_all("td")
    
        RR = soup.find_all("head")
        t = str(RR).split(";")
        x = t[4].split("\"")
        y=x[1].split("-")

        st_no=(y[0])
        dd=(y[3]) 
        mm=(y[2])
        yy=(y[1])
    
        HQ01=((str(result[20]).split())[0].split(">")[1])
        HQ02=((str(result[37]).split())[0].split(">")[1])
        HQ03=((str(result[54]).split())[0].split(">")[1])
        HQ04=((str(result[71]).split())[0].split(">")[1])
        HQ05=((str(result[88]).split())[0].split(">")[1])
        HQ06=((str(result[105]).split())[0].split(">")[1])
        HQ07=((str(result[122]).split())[0].split(">")[1])
        HQ08=((str(result[139]).split())[0].split(">")[1])
        HQ09=((str(result[156]).split())[0].split(">")[1])
        HQ10=((str(result[173]).split())[0].split(">")[1])
        HQ11=((str(result[190]).split())[0].split(">")[1])
        HQ12=((str(result[207]).split())[0].split(">")[1])
        HQ13=((str(result[224]).split())[0].split(">")[1])
        HQ14=((str(result[241]).split())[0].split(">")[1])
        HQ15=((str(result[258]).split())[0].split(">")[1])
        HQ16=((str(result[275]).split())[0].split(">")[1])
        HQ17=((str(result[292]).split())[0].split(">")[1])
        HQ18=((str(result[309]).split())[0].split(">")[1])
        HQ19=((str(result[326]).split())[0].split(">")[1])
        HQ20=((str(result[343]).split())[0].split(">")[1])
        HQ21=((str(result[360]).split())[0].split(">")[1])
        HQ22=((str(result[377]).split())[0].split(">")[1])
        HQ23=((str(result[394]).split())[0].split(">")[1])
        HQ24=((str(result[411]).split())[0].split(">")[1])
 
        NAME=('{}'.format(ID))
        def insert(conn):
            cursor = conn.execute("insert into {0} (站點編號,年,月,日,HQ01,HQ02,HQ03,HQ04,HQ05,HQ06,HQ07,HQ08,HQ09,HQ10,HQ11,HQ12,HQ13,HQ14,HQ15,HQ16,HQ17,HQ18,HQ19,HQ20,HQ21,HQ22,HQ23,HQ24) values('{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}','{10}','{11}','{12}','{13}','{14}','{15}','{16}','{17}','{18}','{19}','{20}','{21}','{22}','{23}','{24}','{25}','{26}','{27}','{28}')".format(NAME,st_no,yy,mm,dd,HQ01,HQ02,HQ03,HQ04,HQ05,HQ06,HQ07,HQ08,HQ09,HQ10,HQ11,HQ12,HQ13,HQ14,HQ15,HQ16,HQ17,HQ18,HQ19,HQ20,HQ21,HQ22,HQ23,HQ24))
            conn.commit()
        try:
            insert(conn)
            print("!!!",ID)
            continue
        except:
            print("0",ID)
            continue
 
#----------------------------------------------------------------------------------------------------------------------

schedule.every().day.at("23:00").do(job)
while True:  
    schedule.run_pending()

#python 定時抓資料.py

