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
root0.minsize(250, 300)
root0.title('主頁面')
#-----------------------------------------------------------------------------雨場切割---------------------
#做雨場切割分頁
def createroot2():                     
    root2 = tk.Toplevel()
    root2.minsize(1300, 700)
    root2.title('雨場切割')

    first = []
    end = []
    first_new = []
    test = []
    time = []

    #【選擇自己測的原始降雨資料】按鈕           
    def hit_raincut1():                         
        root0.withdraw()
    
        File = filedialog.askopenfilename(title='選擇自己測的原始降雨資料', filetypes=[('Excel', '*.xlsx'),('csv', '*.csv')])   #選檔案
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
        comboT.place(x=630, y=7, width=150)

        comboR = ttk.Combobox(root2,values=CLR)  #時間
        comboR.current(0)
        comboR.place(x=630, y=37, width=150)

        Labe00=tk.Label(root2,text='選擇資料->選擇資料中時間、時雨量column名稱')
        Labe00.place(x=510, y=70, width=500, height=30)
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
        
            for i in range(len(time)):
                time[i] = time[i].replace(tzinfo=None)                  #去掉時區
            
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
                time_first.append(time[first_new[i]]+ timedelta(hours=8))             #加8小時回去   
                time_end.append(time[end[i]]+ timedelta(hours=8))                     #加8小時回去   
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
                    entry.place(x=230, y=7)
                    Labe00=tk.Label(root2,text='輸入檔名(要有檔案類型)->選擇存檔資料夾')
                    Labe00.place(x=95, y=40, width=500, height=30)
                    def save():
                        var = entry.get()
                        spath = filedialog.askdirectory(title='選擇存檔資料夾')
                        result.to_excel(r'{}'.format(os.path.join(spath,str(var))))
                        Label=tk.Label(root2,text='雨場切割已儲存')
                        Label.place(x=100, y=5, width=100, height=30)
                        LabeL2=tk.Label(root2,text='共有{}筆資料'.format(len(result)))
                        LabeL2.place(x=20, y=155, width=200, height=30)
                        LabeL3=tk.Label(root2,text='{}'.format(str(result['S_time'])))
                        LabeL3.place(x=10, y=190, width=300, height=500)    
                    bsave = tk.Button(root2,text='輸入檔名',command=save)
                    bsave.place(x=330, y=5)
                
        bget = tk.Button(root2,text='取得columns',command=get)
        bget.place(x=850, y=20)                    
    
    #【選擇氣象站原始降雨資料】按鈕    氣象站資料clumn的名字固定，沒有時區問題
    def hit_raincut2():
        root0.withdraw()   #讓主畫面下移
        file = filedialog.askopenfilename(title='選擇氣象站原始降雨資料', filetypes=[('csv', '*.csv'),('Excel', '*.xlsx')])
        try:
            df = pd.read_csv(r'{}'.format(file))
        except:
            df = pd.read_excel(r'{}'.format(file))

        df.set_index("時間", inplace=True)
        df.index = pd.DatetimeIndex(df.index)
        df = df.resample('H').sum()
        
        test = df['時雨量'].values.ravel() 
        time = df.index.values.ravel() 
        time = pd.to_datetime(pd.Series(time))
    
        for i in range(len(time)):
            time[i] = time[i].replace(tzinfo=None)   #(雖然沒差但還是寫一下)
    
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
                df_test = pd.DataFrame(data = d,index=[0])
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
        entry.insert(0, "XXX_雨場切割.xlsx")    #檔名範例
        entry.place(x=230, y=67)
        Labe00=tk.Label(root2,text='輸入檔名(要有檔案類型)->選擇存檔資料夾')
        Labe00.place(x=95, y=100, width=500, height=30)

        def save():
            var = entry.get()
            spath = filedialog.askdirectory(title='選擇存檔資料夾')
            result.to_excel(r'{}'.format(os.path.join(spath,str(var))))
            Label=tk.Label(root2,text='雨場切割已儲存')
            Label.place(x=100, y=60, width=100, height=30)
            LabeL2=tk.Label(root2,text='共有{}筆資料'.format(len(result)))
            LabeL2.place(x=9, y=155, width=200, height=30)
            LabeL3=tk.Label(root2,text='{}'.format(str(result['S_time'])))
            LabeL3.place(x=10, y=190, width=300, height=500)
        bsave = tk.Button(root2,text='輸入檔名',command=save)
        bsave.place(x=330, y=65)
    
    #回主畫面
    def Bm():
        root2.destroy()
        root0.deiconify()

    raincut1 = tk.Button(root2, text='自己監測資料', bg='FireBrick',fg='white', state=tk.NORMAL, command=hit_raincut1)
    raincut1.place(x=10, y=5, width=80, height=30)
    raincut2 = tk.Button(root2, text='氣象站資料', bg='FireBrick',fg='white', state=tk.NORMAL, command=hit_raincut2)
    raincut2.place(x=10, y=60, width=80, height=30)      
    Bm = tk.Button(root2, text='返回主畫面', bg='WhiteSmoke',fg='gray', state=tk.NORMAL, command=Bm)   
    Bm.place(x=10, y=115, width=80, height=30)
#---------------------------------------------------------------------------------坡面侵蝕-------------------
#做坡面侵蝕分頁
def createroot():
    root0.withdraw()
    root = tk.Toplevel()    #做彈出視窗
    root.minsize(1300, 700)
    root.title('坡面侵蝕')
    spath = filedialog.askdirectory(title='選擇存檔資料夾')  #因為生成的檔案很多，且檔名固定不變，故直接在一開始選擇存檔位置
    
    varN = tk.StringVar()
    entryN = tk.Entry(root, width=20, textvariable=varN)
    entryN.insert(0, "")  
    entryN.place(x=500, y=12)
    LabeLN=tk.Label(root,text="請輸入編號")
    LabeLN.place(x=525, y=32, width=100)

    #【切割距離】按鈕
    def hit_split2():
        
        df_1 = filedialog.askopenfilename(title='選擇檔案', filetypes=[('csv', '*.csv'),('Excel', '*.xlsx')])
        try:
            df_1 = pd.read_csv(r'{}'.format(df_1))
        except:
            df_1 = pd.read_excel(r'{}'.format(df_1))
        
        CL=["(請選擇時間)"]
        CL_D1=["(請選擇距離1)"]
        CL_D2=["(請選擇距離2)"]
        for i in (df_1.columns):
            CL.append(i)
            CL_D1.append(i)
            CL_D2.append(i)
        combo = ttk.Combobox(root,values=CL)
        combo.place(x=150, y=200, width=100)
        combo.current(0)

        combo_D1 = ttk.Combobox(root,values=CL_D1)
        combo_D1.place(x=150, y=240, width=100)
        combo_D1.current(0)

        combo_D2 = ttk.Combobox(root,values=CL_D2)
        combo_D2.place(x=150, y=280, width=100)
        combo_D2.current(0)

        def SL():   #選取時間column
            global K
            K=(str(combo.get()))
            D1=(str(combo_D1.get()))
            D2=(str(combo_D2.get()))
              
            df01=df_1.rename(columns={'{}'.format(D1):'distance1', '{}'.format(D2):'distance2','{}'.format(K):'Time'})

            df01 = df01.set_index('Time')
            df11 = df01['distance1']
            df12 = df01['distance2']
            df11.to_csv(r'{}'.format(os.path.join(spath,"ID1_d1.csv")))
            df12.to_csv(r'{}'.format(os.path.join(spath,"ID1_d2.csv")))
            Label = tk.Label(root, text='已分割儲存')
            Label.place(x=150, y=335, width=100, height=30)
            
        ASLB = tk.Button(root, text='確認', bg='Navy',fg='white', state=tk.NORMAL, command=SL)     #分割原始資料(ID)
        ASLB.place(x=180, y=310, width=40, height=15)
        

    #【做STL】按鈕
    def hit_dostl():
        global img1,img2,img3,img4,K

    #----------------------------------------------------------------------------篩選資料------#@@@@@@@@@@@@@@@@@@@@
        def Filter():
            global df
            df = filedialog.askopenfilename(title='選擇要篩選的檔案', filetypes=[('csv', '*.csv'),('Excel', '*.xlsx')])
            try:
                df = pd.read_csv(r'{}'.format(df))
            except:
                df = pd.read_excel(r'{}'.format(df))
            
            CLT=["(請選擇時間)"]
            CLD=["(請選擇距離)"]

            for i in (df.columns):
                CLT.append(i)
                CLD.append(i)

            combo_T = ttk.Combobox(root,values=CLT)
            combo_T.place(x=500, y=220, width=100)
            combo_T.current(0)
    
            combo_D = ttk.Combobox(root,values=CLD)
            combo_D.place(x=620, y=220, width=100)
            combo_D.current(0)
            
            def TD():
                global df
                TT=(str(combo_T.get()))
                DD=(str(combo_D.get()))
                
                df=df.rename(columns={'{}'.format(TT):'Time', '{}'.format(DD):'distance'})

                for i in range(len(df)):
                    try:
                        try:
                            df.Time[i]=datetime.strptime(str(df.Time[i]), "%Y/%m/%d %H:%M:%S")
                        except:
                            try:
                                df.Time[i]=datetime.strptime(str(df.Time[i]), "%Y/%m/%d %H:%M")
                            except:
                                try:
                                   df.Time[i]=datetime.strptime(str(df.Time[i]), "%Y-%m-%d %H:%M:%S")
                                except:
                                    try:
                                       df.Time[i]=datetime.strptime(str(df.Time[i]), "%Y-%m-%d %H:%M")
                                    except:
                                        try:
                                            df.Time[i]=datetime.strptime(str(df.Time[i]), "%Y/%m/%d %H:%M:%S.%f%z")
                                        except:
                                            try:
                                                df.Time[i]=datetime.strptime(str(df.Time[i]), "%Y-%m-%d %H:%M:%S.%f%z")
                                            except:
                                                try:
                                                    df.Time[i]=datetime.strptime(str(df.Time[i]), "%Y/%m/%d %H:%M:%S%z")
                                                except:
                                                    df.Time[i]=datetime.strptime(str(df.Time[i]), "%Y-%m-%d %H:%M:%S%z")
                
                
                    except:
                        continue

                try:
                    for i in range(len(df)):
                        df.Time[i] = df.Time[i].replace(tzinfo=None)
                        df.Time[i] = df.Time[i] + timedelta(hours=8)
                except:
                    pass

                df = df.loc[df['distance']!=20]
                
                df=df
                plt.figure(figsize=(10,5),dpi=100)
                T = df.Time
                D = df.distance

                plt.plot(T,D)
                plt.show()
            #----------------------------
                VarU=tk.StringVar()
                Upper = Entry(root, textvariable=VarU)
                Upper.insert(0, "(輸入上限)")
                Upper.place(x=530,y=300,width=70)

                VarL=tk.StringVar()
                Lower = Entry(root, textvariable=VarL)
                Lower.insert(0, "(輸入下限)")
                Lower.place(x=620,y=300,width=70)

                def Filter2():
                    global df
                    VU=float(VarU.get())
                    VL=float(VarL.get())

                    df=df[df['distance']>VL]
                    df=df[df['distance']<VU]
                    df=df.reset_index()
                    i = 1
                    while i<(len(df["distance"])-1):
                        a = df["distance"][i-1]
                        b = df["distance"][i]
                        c = df["distance"][i+1]
                        if (abs(b-c)+abs(a-b))/2>abs(c-a)*1.5:
                            df["distance"][i] = (a+c)/2
                            i=i+1
                        else:
                            i=i+1

                    plt.figure(figsize=(10,5),dpi=100)
                
                    T = df['Time']
                    D = df['distance']
            
                    plt.plot(T,D)
                    plt.show()

                    df['Time'] = pd.to_datetime(df['Time']) 
                    for i in range(len(df)):
                        df['Time'][i] = df['Time'][i].replace(tzinfo=None)
                        df['Time'][i] = df['Time'][i] + timedelta(hours=8)

                    def saveSN():
                        varN = entryN.get()
                        df.to_csv(r'{}'.format(os.path.join(spath,str(varN)+"_篩選後.csv")),index=False)
                        Label=tk.Label(root,text='篩選資料 {} 已儲存'.format(varN))
                        Label.place(x=520,y=400,width=200)

                    SNsave = tk.Button(root,text='儲存',command=saveSN)
                    SNsave.place(x=595, y=360)

                Fi2 = tk.Button(root, text='篩選', bg='Navy',fg='white', state=tk.NORMAL, command=Filter2)  
                Fi2.place(x=590, y=330, width=40, height=15)

            b_TD = tk.Button(root, text='確認', bg='Navy',fg='white', state=tk.NORMAL, command=TD)  
            b_TD.place(x=590, y=250, width=40, height=15)
        
        Fi = tk.Button(root, text='篩上下限', bg='Navy',fg='white', state=tk.NORMAL, command=Filter)   
        Fi.place(x=500, y=180, width=70, height=25)

    #----------------------------------------------------------------------------------------做STL---------
        def RunSTL():
            global df01,img1
            df01 = filedialog.askopenfilename(title='選擇要做STL的資料', filetypes=[('csv', '*.csv'),('Excel', '*.xlsx')])
            try:
                df01 = pd.read_csv(r'{}'.format(df01))
            except:
                df01 = pd.read_excel(r'{}'.format(df01))

            df01['Time']=pd.to_datetime(df01['Time'])
            df01.set_index('Time', drop=True, inplace=True)
            df01=df01
            df01=df01.resample(rule='30T').mean().interpolate(method='slinear')
            
            res1= STL(df01['distance'],period=103).fit()
            
            res1.plot()
            plt.savefig(r'{}'.format(os.path.join(spath,"STL.png")))
            df01['trend']=res1.trend
            df01['season']=res1.seasonal
            df01['residual']=res1.resid
            df01=df01.fillna(method='ffill')
            df01=df01.fillna(method='bfill')

    #--------------------------------------------------------------------------------------輸出圖--------
            img1=Image.open(r'{}'.format(os.path.join(spath,"STL.png")))
            img1=img1.resize((504,448),Image.ANTIALIAS)
            img1=ImageTk.PhotoImage(img1)
            img1Label=tk.Label(root,image=img1)
            img1Label.place(x=760, y=200, width=504, height=448)

            def saveSN():
                global df01
                varN = entryN.get()
                df01.to_csv(r'{}'.format(os.path.join(spath,str(varN)+"_STL.csv")))
                Label=tk.Label(root,text='STL資料 {} 已儲存'.format(varN))
                Label.place(x=510,y=540,width=200)
                
            SNsave = tk.Button(root,text='儲存',command=saveSN)
            SNsave.place(x=595, y=500)

        RSTL = tk.Button(root, text='執行STL', bg='Navy',fg='white', state=tk.NORMAL, command=RunSTL)   
        RSTL.place(x=500, y=450, width=70, height=25)
        
    def Bm():
        root.destroy()
        root0.deiconify()
  
    split2 = tk.Button(root, text='切割距離', bg='Navy',fg='white', state=tk.NORMAL, command=hit_split2)     #分割距離(d)
    split2.place(x=20, y=100, width=80, height=30)
    dostl = tk.Button(root, text='做STL', bg='Navy',fg='white',state=tk.NORMAL, command=hit_dostl)           #做stl
    dostl.place(x=450, y=100, width=80, height=30)
    Bm = tk.Button(root, text='返回主畫面', bg='WhiteSmoke',fg='gray', state=tk.NORMAL, command=Bm)   
    Bm.place(x=1000, y=10, width=80, height=30)
    Labels = tk.Label(root, text='存檔位置: {}'.format(spath))
    Labels.place(x=0, y=10, width=500, height=30)    
#--------------------------------------------------------------------------------沖蝕分析-------    
#做沖蝕分析分頁
def createroot3():
    root3 = tk.Toplevel()   
    root3.minsize(1300, 700)
    root3.title('沖蝕分析')
    
    #【沖蝕分析】按鈕
    def Erosion():
        global rain
        root0.withdraw()
        file1 = filedialog.askopenfilename(title='選擇雨場分析資料', filetypes=[('Excel', '*.xlsx'),('Excel', '*.xls'),('csv', '*.csv')])
        try:
            rain = pd.read_excel(r'{}'.format(file1))
        except:
            rain = pd.read_csv(r'{}'.format(file1))
        
        file2 = filedialog.askopenfilename(title='選擇坡面侵蝕資料', filetypes=[('csv', '*.csv'),('Excel', '*.xlsx')])
        try:
            ero = pd.read_csv(r'{}'.format(file2))
        except:
            ero = pd.read_excel(r'{}'.format(file2))

        for i in range(len(rain)):
            try:
                rain.S_time[i]=datetime.strptime(str(rain.S_time[i]), "%Y/%m/%d %H:%M:%S")
                rain.E_time[i]=datetime.strptime(str(rain.E_time[i]), "%Y/%m/%d %H:%M:%S") 
            except:
                try:
                    rain.S_time[i]=datetime.strptime(str(rain.S_time[i]), "%Y/%m/%d %H:%M")
                    rain.E_time[i]=datetime.strptime(str(rain.E_time[i]), "%Y/%m/%d %H:%M")
                except:
                    try:
                        rain.S_time[i]=datetime.strptime(str(rain.S_time[i]), "%Y-%m-%d %H:%M:%S")
                        rain.E_time[i]=datetime.strptime(str(rain.E_time[i]), "%Y-%m-%d %H:%M:%S")
                    except:
                        rain.S_time[i]=datetime.strptime(str(rain.S_time[i]), "%Y-%m-%d %H:%M")
                        rain.E_time[i]=datetime.strptime(str(rain.E_time[i]), "%Y-%m-%d %H:%M")

        try:
            for i in range(len(rain)):
                rain.S_time[i] = rain.S_time[i].replace(tzinfo=None)
                rain.S_time[i] = rain.S_time[i] + timedelta(hours=8)
                rain.E_time[i] = rain.E_time[i].replace(tzinfo=None)
                rain.E_time[i] = rain.E_time[i] + timedelta(hours=8)
        except:
            pass
        
        eroT=["(請選擇沖蝕資料時間)"]
        for i in (ero.columns):
            eroT.append(i)
        comboE = ttk.Combobox(root3,values=eroT)
        comboE.place(x=410, y=10, width=150)
        comboE.current(0)

        def SL(): 
            global rain
            K=(str(comboE.get()))

            for i in range(len(ero)):
                try:
                    ero['{}'.format(K)][i] = datetime.strptime(ero['{}'.format(K)][i],"%Y/%m/%d %H:%M:%S")                       
                except:
                    try:
                        ero['{}'.format(K)][i] = datetime.strptime(ero['{}'.format(K)][i],"%Y-%m-%d %H:%M:%S")
                    except:
                        try:
                            ero['{}'.format(K)][i] = datetime.strptime(ero['{}'.format(K)][i],"%Y/%m/%d")
                        except:
                            try:
                                ero['{}'.format(K)][i] = datetime.strptime(ero['{}'.format(K)][i],"%Y-%m-%d")
                            except:
                                try:
                                    ero['{}'.format(K)][i] = datetime.strptime(ero['{}'.format(K)][i],"%Y/%m/%d %H:%M")
                                except:
                                    ero['{}'.format(K)][i] = datetime.strptime(ero['{}'.format(K)][i],"%Y-%m-%d %H:%M")

            
            try:
                for i in range(len(rain)):
                    ero['{}'.format(K)][i] = ero['{}'.format(K)][i].replace(tzinfo=None)
                    ero['{}'.format(K)][i] = ero['{}'.format(K)][i] + timedelta(hours=8)
            except:
                pass
                
                
            rain = rain.drop(rain.loc[rain.E_time<=ero['{}'.format(K)][0]].index).reset_index(drop=True)
     
            Erosion_s = []
            Erosion_e = []
            time_record=[]
        
            for k in range(len(ero['{}'.format(K)])):
                for w in range(len(rain)):                        
                    k=2
                    while k<len(ero['{}'.format(K)]):
                        if ero['{}'.format(K)][k] > rain.S_time[w]:                                            
                            Erosion_s.append(ero.trend[k-2].round(2))
                            while k<len(ero['{}'.format(K)]):
                                if  ero['{}'.format(K)][k]> rain.E_time[w]:  
                                    Erosion_e.append(ero.trend[k].round(2))
                                    time_record.append(rain.E_time[w])
                                    break
                                else:                       
                                    k+=1
                            break
                        else:
                            k+=1
                    continue                       
                break

            d= {'Erosion_start':Erosion_s,               
                'Erosion_end':Erosion_e,
                'E_time':time_record}
        
            cc=pd.DataFrame(d)    
            cc['E_time']=cc['E_time'].astype('datetime64[ns]')
            rain['E_time']=rain['E_time'].astype('datetime64[ns]')
            rain_all = pd.merge(rain,cc,on='E_time').drop(['Index','Unnamed: 0'],axis=1)
            rain_all['Erosion']=rain_all['Erosion_end']-rain_all['Erosion_start']

            for i in range(len(rain_all)):                                                #去掉時區
                rain_all['S_time'][i] = rain_all['S_time'][i].replace(tzinfo=None)
                rain_all['E_time'][i] = rain_all['E_time'][i].replace(tzinfo=None)
                rain_all['S_time'][i] = rain_all['S_time'][i] + timedelta(hours=8)
                rain_all['S_time'][i] = rain_all['S_time'][i] + timedelta(hours=8)
            
            #存檔
            var = tk.StringVar()
            entry = tk.Entry(root3, width=20, textvariable=var)
            entry.insert(0, "XXX_沖蝕分析.xls")
            entry.place(x=230, y=10)

            def save():
                var = entry.get()
                spath = filedialog.askdirectory(title='選擇存檔資料夾')
                rain_all.to_excel(r'{}'.format(os.path.join(spath,str(var))))
                Label=tk.Label(root3,text='沖蝕分析已儲存')
                Label.place(x=100, y=8, width=100, height=30)    
            
                LabeL2=tk.Label(root3,text='監測期間共有{}場降雨'.format(len(rain)), font=2)
                LabeL2.place(x=9, y=110, width=200, height=30)
                LabeL3=tk.Label(root3,text='第1筆資料: {}'.format(rain_all.S_time[0]), font=2)
                LabeL3.place(x=10, y=155, width=250, height=35)
                LabeL4=tk.Label(root3,text='第{0}筆資料: {1}'.format(len(rain),rain_all.S_time[len(rain_all.S_time)-1]), font=2)
                LabeL4.place(x=5, y=195, width=270, height=35)
            
            bsave = tk.Button(root3,text='輸入檔名',command=save)
            bsave.place(x=330, y=8)

        ASLB = tk.Button(root3, text='確認', bg='DarkOliveGreen',fg='white', state=tk.NORMAL, command=SL)    
        ASLB.place(x=567, y=14, width=40, height=15)

    def Bm():
        root3.destroy()
        root0.deiconify()

    B = tk.Button(root3, text='沖蝕分析', bg='DarkOliveGreen',fg='white', state=tk.NORMAL, command=Erosion)
    B.place(x=10, y=5, width=80, height=30)
    Bm = tk.Button(root3, text='返回主畫面', bg='WhiteSmoke',fg='gray', state=tk.NORMAL, command=Bm)   
    Bm.place(x=10, y=50, width=80, height=30)

#====================================================================================主畫面===========================
r2 = tk.Button(root0, text='雨場切割', bg='WhiteSmoke',fg='FireBrick', state=tk.NORMAL, command=createroot2)
r2.place(x=10, y=5, width=120, height=45)
r = tk.Button(root0, text='坡面侵蝕', bg='WhiteSmoke',fg='navy', state=tk.NORMAL, command=createroot)
r.place(x=10, y=60, width=120, height=45)
r3 = tk.Button(root0, text='沖蝕分析', bg='WhiteSmoke',fg='DarkOliveGreen', state=tk.NORMAL, command=createroot3)
r3.place(x=10, y=115, width=120, height=45)

root0.mainloop()
