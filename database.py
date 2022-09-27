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
#-----------------------------------------------------------
conn = pyodbc.connect(Driver="{SQL Server Native Client 11.0};",Server="LAPTOP-9VKLPUUE\SQLEXPRESS;",Datebase="CWB;",UID="sinotech;",PWD="sinotech;" )
cursor = conn.cursor()
# cursor.execute("DELETE FROM 氣象")

#----------------------------------------------------------
# DATE1 = input("請輸入起始日期(yyyy-mm-dd): ")               #@@@@@@@@@@@@@@@@@@@@@
# DATE2 = input("請輸入結束日期(yyyy-mm-dd): ")               #@@@@@@@@@@@@@@@@@@@@@
#-----------------------------------------------------------
# ID=input("請輸入站點(C1R120): ")
# DATE1 = input("請輸入起始日期(yyyy-mm-dd): ")
# DATE2 = input("請輸入結束日期(yyyy-mm-dd): ")
#----------------------------------------------------------
def job():
    conn = pyodbc.connect(Driver="{SQL Server Native Client 11.0};",Server="LAPTOP-9VKLPUUE\SQLEXPRESS;",Datebase="CWB;",UID="sinotech;",PWD="sinotech;" )
    cursor = conn.cursor()
    # cursor.execute("DELETE FROM 氣象")
    DATE1=time.strftime('%Y-%m-%d', time.localtime()) #@@@@@@@@@@@@@@@@@@@@@
    DATE2=time.strftime('%Y-%m-%d', time.localtime()) #@@@@@@@@@@@@@@@@@@@2@

    M1=DATE1.split('-')[1]
    D1=DATE1.split('-')[2]

    Y=DATE1.split('-')[0]

    # M2=DATE2.split('-')[1]   #@@@@@@@@@@@@@@@@@@@@@
    # D2=DATE2.split('-')[2]   #@@@@@@@@@@@@@@@@@@@@@
 
#------------------------------------------------------------
    df = pd.read_excel(r'C:\Users\Tosha.E.T\Desktop\Sinotech\811\站點編號(爬蟲用).xlsx')
    for i in range(len(df)):
        ID=df['站點編號'][i]
        M=[]
        D=[]
    
#-------------------------------------------網址時間---------   #@@@@@@@@@@@@@@@@@@@@@

#         if int(M2)-int(M1)>1:
#             for i in range(31-int(D1)+1):
#                 M.append(int(M1))
#             for i in range(int(D1),32):
#                 D.append(i)

#             for i in range(int(M1)+1,int(M2)):
#                 for j in range(1,32):
#                     M.append(i)
#             for i in range(int(M1),int(M2)-1):
#                 for j in range(1,32):
#                     D.append(j)
            
#             for i in range(int(D2)):
#                 M.append(int(M2))
#             for i in range(1,int(D2)+1):
#                 D.append(i)        
# ########################################        
#         elif int(M2)-int(M1)==1:
#             for i in range(31-int(D1)+1):
#                 M.append(int(M1))
#             for i in range(int(D1),32):
#                 D.append(i)
    
#             for i in range(int(D2)):
#                 M.append(int(M2))
#             for i in range(1,int(D2)+1):
#                 D.append(i)
# ########################################
#         else:
#             for i in range(int(D2)-int(D1)+1):
#                 M.append(int(M1))
#             for i in range(int(D1),int(D2)+1):
#                 D.append(i)

# #--------------------------------------------------------------

#         for i in range(len(M)):
#             Yy=Y
#             if M[i]<10:
#                 Mm='0{}'.format(M[i])
#             else:
#                 Mm=str(M[i])
    
#             if D[i]<10:
#                 Dd='0{}'.format(D[i])
#             else:
#                 Dd=str(D[i])
        
        #     url = r'https://e-service.cwb.gov.tw/HistoryDataQuery/DayDataController.do?command=viewMain&station={0}&stname=%25E4%25B8%258A%25E5%25BE%25B7%25E6%2596%2587&datepicker={1}-{2}-{3}#'.format(ID,Y,M1,D1)          

        #     re = requests.get(url) 
        #     soup = BeautifulSoup(re.text, "html.parser")
        #     result = soup.find_all("td")
    
        #     RR = soup.find_all("head")
        #     t = str(RR).split(";")
        #     x = t[4].split("\"")
        #     y=x[1].split("-")

    
        #     st_no=(y[0])
        #     dd=(y[3]) 
        #     mm=(y[2])
        #     yy=(y[1])
    
        #     HQ01=((str(result[20]).split())[0].split(">")[1])
        #     HQ02=((str(result[37]).split())[0].split(">")[1])
        #     HQ03=((str(result[54]).split())[0].split(">")[1])
        #     HQ04=((str(result[71]).split())[0].split(">")[1])
        #     HQ05=((str(result[88]).split())[0].split(">")[1])
        #     HQ06=((str(result[105]).split())[0].split(">")[1])
        #     HQ07=((str(result[122]).split())[0].split(">")[1])
        #     HQ08=((str(result[139]).split())[0].split(">")[1])
        #     HQ09=((str(result[156]).split())[0].split(">")[1])
        #     HQ10=((str(result[173]).split())[0].split(">")[1])
        #     HQ11=((str(result[190]).split())[0].split(">")[1])
        #     HQ12=((str(result[207]).split())[0].split(">")[1])
        #     HQ13=((str(result[224]).split())[0].split(">")[1])
        #     HQ14=((str(result[241]).split())[0].split(">")[1])
        #     HQ15=((str(result[258]).split())[0].split(">")[1])
        #     HQ16=((str(result[275]).split())[0].split(">")[1])
        #     HQ17=((str(result[292]).split())[0].split(">")[1])
        #     HQ18=((str(result[309]).split())[0].split(">")[1])
        #     HQ19=((str(result[326]).split())[0].split(">")[1])
        #     HQ20=((str(result[343]).split())[0].split(">")[1])
        #     HQ21=((str(result[360]).split())[0].split(">")[1])
        #     HQ22=((str(result[377]).split())[0].split(">")[1])
        #     HQ23=((str(result[394]).split())[0].split(">")[1])
        #     HQ24=((str(result[411]).split())[0].split(">")[1])
 

        #     def insert(conn):
        #         cursor = conn.execute("insert into 氣象 (站點編號,年,月,日,HQ01,HQ02,HQ03,HQ04,HQ05,HQ06,HQ07,HQ08,HQ09,HQ10,HQ11,HQ12,HQ13,HQ14,HQ15,HQ16,HQ17,HQ18,HQ19,HQ20,HQ21,HQ22,HQ23,HQ24) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(st_no,yy,mm,dd,HQ01,HQ02,HQ03,HQ04,HQ05,HQ06,HQ07,HQ08,HQ09,HQ10,HQ11,HQ12,HQ13,HQ14,HQ15,HQ16,HQ17,HQ18,HQ19,HQ20,HQ21,HQ22,HQ23,HQ24))
        #         conn.commit()
        #     try:
        #         insert(conn)
        #     except:
        #         pass
        #     time.sleep(random.uniform(0,0.1))
        #     print("WAIT..................",i) 

        # print("done~~")
    url = r'https://e-service.cwb.gov.tw/HistoryDataQuery/DayDataController.do?command=viewMain&station={0}&stname=%25E4%25B8%258A%25E5%25BE%25B7%25E6%2596%2587&datepicker={1}-{2}-{3}#'.format(ID,2018,M1,D1)          

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
 

    def insert(conn):
        cursor = conn.execute("insert into 氣象 (站點編號,年,月,日,HQ01,HQ02,HQ03,HQ04,HQ05,HQ06,HQ07,HQ08,HQ09,HQ10,HQ11,HQ12,HQ13,HQ14,HQ15,HQ16,HQ17,HQ18,HQ19,HQ20,HQ21,HQ22,HQ23,HQ24) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(st_no,yy,mm,dd,HQ01,HQ02,HQ03,HQ04,HQ05,HQ06,HQ07,HQ08,HQ09,HQ10,HQ11,HQ12,HQ13,HQ14,HQ15,HQ16,HQ17,HQ18,HQ19,HQ20,HQ21,HQ22,HQ23,HQ24))
        conn.commit()
    try:
        insert(conn)
    except:
        pass
        # time.sleep(random.uniform(0,0.1))
    #     print("WAIT..................",i) 

    # print("done~~")


#----------------------------------------------------------------------------------------------------------------------

    def read(conn):
        cursor = conn.cursor()
        cursor.execute("Select * from 氣象")
        row =cursor.fetchall()
        print(row)
        conn.commit()


    read(conn)

schedule.every().day.at("10:30").do(job)
while True:  
    schedule.run_pending()
