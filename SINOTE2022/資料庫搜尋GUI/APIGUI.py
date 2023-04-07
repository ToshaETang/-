import tkinter.ttk as ttk
import tkinter as tk
from tkinter import *
from unittest import result
import pymssql
import pyodbc
import pandas as pd
import os
import os.path
from os import listdir
from os.path import isfile, isdir, join
from tkinter import filedialog

L_ID = ["請選擇設備編號"] #站點編號
df = [] #所有資料
sensor_type = [] #格式
value = [] #數值
entry_id = []
upload_time = []
ID = []
value_time = []
N = {}
N.clear()
#-----------------------------------
dfn = pd.read_excel(r"大表.xlsx")
for i in range(len(dfn['內部編號'])):
    # N[str(i)+"_"+str(dfn['設備編號'][i])] = dfn['內部編號'][i]
    try:
        int(dfn['內部編號'][i][-1]) + int(dfn['內部編號'][i][-2])
        N[(dfn['設備編號'][i])] = dfn['內部編號'][i]
    except:
        N[(dfn['設備編號'][i])] = dfn['內部編號'][i][:-1]
#print(N)
#-----------------------------------
conn = pyodbc.connect(Driver="{SQL Server Native Client 11.0};",Server="VM05023;",Datebase="UPDATE;",UID="update;",PWD="update;" )
cursor = conn.execute("select * from updateV")
print("連接上資料庫!!!")
for r in cursor:
    sID = str(r[0]).split(" ")[0]
    L_ID.append(sID)
    df.append(r)
conn.commit()
#-----------------------------------
L_ID = list(dict.fromkeys(L_ID))
L_ID2 = []  #只留編號
L_ID_N = []
for i in range(1,len(L_ID)):
    L_ID2.append(((L_ID[i])))
# print(L_ID2)
for i in L_ID2:
    try:
        L_ID_N.append(i+"_"+N.get(int(i)))
    except:
        L_ID_N.append(i)
# print(L_ID_N)
#-----------------------------------
root = Tk()
root.geometry("800x410+10+100")
root.title('主頁面')

combo_ID = ttk.Combobox(root, values=L_ID_N)  #選設備編號
combo_ID.current(0)
combo_ID.place(x=20, y=20,width=180)
Ttime = Entry(root)                         #輸入時間
Ttime.insert(END, 'yyyymmddHHMMSS')
Ttime.place(x=220, y=20)
Ttime2 = Entry(root)                         #輸入時間
Ttime2.insert(END, 'yyyymmddHHMMSS')
Ttime2.place(x=390, y=20)
Labe = tk.Label(root,text='~')
Labe.place(x=370, y=20)
combo_type = ttk.Combobox(root, values=["W","S"])  #選資料類型
combo_type.current(0)
combo_type.place(x=540, y=20,width=40)

for i in range(len(df)):
    ID.append(str(df[i][0]).strip())
    value_time.append(str(df[i][1]).strip())
    sensor_type.append(str(df[i][2]).strip())
    value.append(str(df[i][3]).strip())
    entry_id.append(str(df[i][4]).strip())
    upload_time.append(str(df[i][5]).strip())


result = pd.DataFrame()
def F_search():
    global result
    global id,TIME
    id = ((combo_ID.get()).split("_")[0])
    #print(id)

    TIME = Ttime.get()      #開始時間
    TIME2 = Ttime2.get()    #結束時間
    textshow = tk.Text(root)
    ty = combo_type.get()   # S水位 W濁度
    

    value_time2 = []
    sensor_type2 = []
    value2 = []
    entry_id2 = []
    upload_time2 = []
    for i in range (len(ID)):                         #抓出要求站點和資料類型
        if id == ID[i] and ty==sensor_type[i]:
            value_time2.append(value_time[i])
            sensor_type2.append(sensor_type[i])
            value2.append(value[i])
            entry_id2.append(entry_id[i])
            upload_time2.append(upload_time[i])


    for i in range(len(value_time2)):                 #抓出時間範圍內的資料
        if int(TIME)<=int(value_time2[i]) and int(value_time2[i])<=int(TIME2):
            d = {"ID":id,
                "value_time":value_time2[i],
                "sensor_type":sensor_type2[i],
                "value":value2[i],
                "entry_id":entry_id2[i],
                "upload_time":upload_time2[i]
                }
            df_test = pd.DataFrame(data = d, index=[0])
            result = pd.concat([result, df_test],axis =0)
    print(result)
    

    textshow.insert(END,result)
    textshow.insert(tk.INSERT,'\n')
    textshow.place(x=10, y=50,width=750)

    def DL():
        global result
        result.to_excel(r'資料庫下載檔案.xlsx', index=False,encoding='utf_8_sig')
        Label_save = tk.Label(root, text="下載成功")
        Label_save.place(x=640, y=370)




    button_download = tk.Button(root, text='下載資料', command=DL)
    button_download.place(x=700, y=370)
    


  

button_SEARCH = tk.Button(root, text='搜尋', command=F_search)
button_SEARCH.place(x=600, y=20)



root.mainloop()