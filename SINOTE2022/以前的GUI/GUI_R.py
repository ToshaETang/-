# cd C:\TET\SINOTE2022
# python GUI_R.py
import matplotlib.pyplot as plt
from tkinter import *
import tkinter.ttk as ttk
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import pandas as pd
import numpy as np
import os
import os.path
from os import listdir
from os.path import isfile, isdir, join
import datetime,time
import plotly.express as px
from tkinter import filedialog
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
from dateutil.tz import tzutc
from tzlocal import get_localzone
import plotly.offline as offline
import matplotlib
from tkinter import filedialog
from matplotlib.figure import Figure
from tkinter.filedialog import askdirectory
from PIL import Image, ImageTk
#----去掉紅色警告-------
from sklearn import metrics
import warnings
warnings.filterwarnings("ignore")
#==========================================================================================================
root0 = Tk()
#root0.minsize(350,400)
root0.geometry("500x400+550+100")
root0.title('主頁面')
#-----------------------------------------------------------------------------雨場切割---------------------
#做雨場切割分頁
def createroot2():                     
    root2 = tk.Toplevel()
    root2.geometry("500x400+550+100")
    root2.title('雨場切割')

    first = []
    end = []
    first_new = []

    #【選擇自己測的原始降雨資料】按鈕           
    def hit_raincut1():                         
        root0.withdraw()
    
        File = filedialog.askopenfilename(title='選擇原始降雨資料', filetypes=[('csv', '*.csv'),('Excel', '*.xlsx')])   #選檔案
        try:
            df = pd.read_excel(r'{}'.format(File))
        except:
            df = pd.read_csv(r'{}'.format(File))

        CLR=["(請選擇時雨量)"]
        CLT=["(請選擇時間)"]
        for i in (df.columns):
            CLR.append(i)
            CLT.append(i)

        comboT = ttk.Combobox(root2,values=CLT)  #時雨量
        comboT.current(0)
        comboT.place(x=10, y=100, width=150)

        comboR = ttk.Combobox(root2,values=CLR)  #時間
        comboR.current(0)
        comboR.place(x=10, y=130, width=150)

        #Labe00=tk.Label(root2,text='選擇資料->選擇資料中時間、時雨量column名稱')
        #Labe00.place(x=510, y=70, width=500, height=30)

        #【取得columns】按鈕 
        def get():
            try:
                df = pd.read_excel(r'{}'.format(File))
            except:
                df = pd.read_csv(r'{}'.format(File))
                                                            
            R=(str(comboR.get()))
            T=(str(comboT.get()))

            varr = (str(comboR.get()))
            test = df['{}'.format(varr)].values.ravel()        #抓輸入的column名
            vart = (str(comboT.get()))
            df.set_index("{}".format(vart), inplace=True)
            df.index = pd.DatetimeIndex(df.index)
            df = df.resample('H').sum()
            time = df.index.values.ravel() 
            time = pd.to_datetime(pd.Series(time))
                      
            
            for i in range(len(test)):
                if test[i] > 4 :
                    first.append(int(i))
                    x = test[i + 1 : i + 7]
                    if all(j <= 4 for j in x): 
                        end.append(int(i) + 1)
                    else:
                        continue
            if len(first)>0:      
    #判斷降雨事件間隔是否有大於6小時
                first_new.append(first[0])
                for i in range(len(first)):
                    if (first[i] - first[i - 1]) > 6:
                        first_new.append(first[i])
                        rain_result = []
                        rain_sum = []
                        rain_max = []
                        time_first = []
                        time_end = []
                        time_lag = []
    #各個欄位計算
            for i in range(len(first_new)):
                timelag = end[i] - first_new[i]
                time_first.append(time[first_new[i]])  
                time_end.append(time[end[i]])      
                rain_result.append(test[first_new[i] : end[i] + 1])
                rain_sum.append(sum(test[first_new[i] : end[i] + 1]))
                time_lag.append(timelag)
            for i in range(len(rain_result)):
                rain_max.append(max(rain_result[i]))
            for i in range(len(rain_result)):
                rain_result[i]=str(rain_result[i])
                df_L_rain = pd.DataFrame(np.array([rain_result]))
        
    #有判斷欄位的原始雨場
            result = pd.DataFrame()
            index = 0
            for i in range(len(rain_result)):
                if rain_sum[i] > 12.7:
                    d = {"Index":index,
                         "ID":"try",
                         "S_time":time_first[i],
                         "E_time":time_end[i],
                         "降雨延時":time_lag[i]+1,
                         "總降雨量":rain_sum[i],
                         "最大降雨量":rain_max[i],
                         "rain_detail":df_L_rain[i],
                         "sum是否大於12.7":"1"
                         }
                    df_test = pd.DataFrame(data = d, index=[0])
                    result = pd.concat([result, df_test],axis =0)
                    index = index + 1
                else:
                    d = {"Index":index,
                         "ID":"try",
                         "S_time":time_first[i],
                         "E_time":time_end[i],
                         "降雨延時":time_lag[i]+1,
                         "總降雨量":rain_sum[i],
                         "最大降雨量":rain_max[i],
                         "rain_detail":df_L_rain[i],
                         "sum是否大於12.7":"0"
                         }
                    df_test = pd.DataFrame(data = d,index=[0])
                    result = pd.concat([result, df_test],axis =0)
                    index = index + 1
                
                    #存檔
                    var = tk.StringVar()
                    entry = tk.Entry(root2, width=20, textvariable=var)
                    entry.insert(0, "XXX_雨場切割.xlsx")     #檔名提示                  
                    entry.place(x=10, y=180,width=300)
                    #Labe00=tk.Label(root2,text='輸入檔名(要有檔案類型)->選擇存檔資料夾')
                    #Labe00.place(x=10, y=140, width=500, height=30)
                    def save():
                        var = entry.get()
                        spath = filedialog.askdirectory(title='選擇存檔資料夾')
                        result.to_excel(r'{}'.format(os.path.join(spath,str(var))))
                        Label=tk.Label(root2,text='雨場切割已儲存')
                        Label.place(x=10, y=205, width=100, height=30)
                        #LabeL2=tk.Label(root2,text='共有{}筆資料'.format(len(result)))
                        #LabeL2.place(x=20, y=155, width=200, height=30)
                        #LabeL3=tk.Label(root2,text='{}'.format(str(result['S_time'])))
                        #LabeL3.place(x=10, y=190, width=300, height=500)    
                    bsave = tk.Button(root2,text='輸入檔名',command=save)
                    bsave.place(x=325, y=179)
                
        bget = tk.Button(root2,text='取得columns',command=get)
        bget.place(x=180, y=115)  
    
      
    
    #回主畫面
    def Bm():
        root2.destroy()
        root0.deiconify()

    raincut1 = tk.Button(root2, text='選擇處理過的降雨資料', bg='WhiteSmoke',fg='gray', state=tk.NORMAL, command=hit_raincut1)
    raincut1.place(x=10, y=10, width=150, height=30)      
    Bm = tk.Button(root2, text='返回主畫面', bg='WhiteSmoke',fg='gray', state=tk.NORMAL, command=Bm)   
    Bm.place(x=400, y=350, width=80, height=30)


#--------------------------------------------------------------------------------------


#做資料處理
def createroot():
    root0.withdraw()
    root = tk.Toplevel()    #做彈出視窗
    root.geometry("500x400+550+100")
    root.title('資料處理')
    
    
    def Get_OD():
        root0.withdraw()
        File_OD = filedialog.askopenfilename(title='選擇原始資料', filetypes=[('csv', '*.csv'),('Excel', '*.xlsx')])   #選檔案
        try:
            df_OD = pd.read_excel(r'{}'.format(File_OD))
        except:
            df_OD = pd.read_csv(r'{}'.format(File_OD))

        df_OD = df_OD.drop(columns = 'HQT')            #拿掉每日雨量
        File_OD = File_OD[:-4]

        YEAR = df_OD['yy'].unique()
        for Y in YEAR:
            N_df = df_OD[df_OD['yy']==Y]
            N_df.to_csv(r'{}_年切割_{}.csv'.format(File_OD,Y),index=False)

        Label=tk.Label(root,text='年切割已儲存')
        Label.place(x=10, y=50, width=100, height=30)    



    def Get_YD():
        root0.withdraw()
        
        File_YD = filedialog.askopenfilename(title='選擇年切割資料', filetypes=[('csv', '*.csv'),('Excel', '*.xlsx')])   #選檔案
        

        try:
            df_YD = pd.read_excel(r'{}'.format(File_YD))
        except:
            df_YD = pd.read_csv(r'{}'.format(File_YD))

        TIME = []
        for i in range(len(df_YD['yy'])):
            
            for h in range(1,25):
                if h == 24:
                    h=0
                n = (str(df_YD['yy'][i])+"-"+str(df_YD['mm'][i])+"-"+str(df_YD['dd'][i])+" "+str(h)+":00")
                TIME.append(n)

        dfr = np.split(df_YD,[4],axis = 1)        
        RAIN = dfr[1].values.ravel()

        result = pd.DataFrame()
        index = 0
        File_YD = File_YD[:-4]

        for i in range(len(RAIN)):
            d={
                'st_no':df_YD['st_no'][0],
                'time':TIME[i],
                'rain':RAIN[i]
            }
    
            df_test = pd.DataFrame(data = d,index=[0])
            result = pd.concat([result, df_test],axis =0)
            index = index + 1
 
        result.to_csv(r'{}_塞時間.csv'.format(File_YD),index=False)

        Label=tk.Label(root,text='塞時間已儲存')
        Label.place(x=10, y=175, width=100, height=30)

    def Bm():
        root.destroy()
        root0.deiconify()


    OrigionlData = tk.Button(root, text='選擇原始降雨資料', bg='WhiteSmoke',fg='gray', state=tk.NORMAL, command=Get_OD)
    OrigionlData.place(x=10, y=10, width=150, height=30)
    YearData = tk.Button(root, text='選擇年切割資料', bg='WhiteSmoke',fg='gray', state=tk.NORMAL, command=Get_YD)
    YearData.place(x=10, y=100, width=150, height=30)
    Bm = tk.Button(root, text='返回主畫面', bg='WhiteSmoke',fg='gray', state=tk.NORMAL, command=Bm)   
    Bm.place(x=400, y=350, width=80, height=30) 

#====================================================================================主畫面===========================
r2 = tk.Button(root0, text='雨場切割', bg='WhiteSmoke',fg='gray', state=tk.NORMAL, command=createroot2)
r2.place(x=10, y=60, width=120, height=45)
r = tk.Button(root0, text=' 資料處理', bg='WhiteSmoke',fg='gray', state=tk.NORMAL, command=createroot)
r.place(x=10, y=5, width=120, height=45)


W='''
Step1 : 點擊「資料處理」 進入該頁面

Step2 : 點擊「選擇原始降雨資料」 並選擇要進行切割的資料
              資料會被切成一年一個檔案 檔名為 XXX_年切割 且存在原位

Step3 : 點擊「選擇年切割資料」並選擇Step2產生的資料
              時間欄會從橫轉直 檔名為 XXX_年切割_塞時間 且存在原位

Step4 : 點擊「返回主畫面」

Step5 : 點擊「雨場切割」 進入該頁面
              (如果資料不須前置處理 可直接跳至此步驟)

Step6 : 點擊「選擇年切割資料」並選擇Step3產生的資料

Step7 : 跟隨介面上的指示操作 即完成雨場切割
'''
SOP = tk.Message(root0,text=W)
SOP.place(x=10, y=120)


root0.mainloop()
