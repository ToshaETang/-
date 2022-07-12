import re
from typing_extensions import ParamSpecArgs
import requests
import pandas as pd
import time
import random
from bs4 import BeautifulSoup
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
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import openpyxl
import pytz
from datetime import datetime
from datetime import timedelta
from dateutil.parser import parse
from dateutil.tz import tzutc
from tzlocal import get_localzone
import plotly.offline as offline
import matplotlib
from tkinter import filedialog
from matplotlib.figure import Figure
from tkinter.filedialog import askdirectory
from PIL import Image, ImageTk
#==========================================================================================================
root = Tk()
root.minsize(900, 690)
root.title('主頁面')
#-------------------------------------------------------------------
LabeL1=tk.Label(root,text='輸入格式範例')
LabeL1.place(x=50, y=20, width=100, height=30)
LabeL2=tk.Label(root,text='C0R100')
LabeL2.place(x=185, y=20, width=100, height=30)
LabeL3=tk.Label(root,text='2020-08-06')
LabeL3.place(x=320, y=20, width=100, height=30)
LabeL4=tk.Label(root,text='01')
LabeL4.place(x=425, y=20, width=100, height=30)
LabeL5=tk.Label(root,text='2020-12-27')
LabeL5.place(x=560, y=20, width=100, height=30)
LabeL6=tk.Label(root,text='24 (範圍:01~24)')
LabeL6.place(x=665, y=20, width=100, height=30)

ID1=tk.StringVar()
input_ID1 = Entry(root, textvariable=ID1)
input_ID1.insert(0, "(輸入站點編號)")
input_ID1.place(x=185,y=10+50,width=100,height=30)

s_date1=tk.StringVar()
input_s_date1 = Entry(root, textvariable=s_date1)
input_s_date1.insert(0, "(輸入起始日期)")
input_s_date1.place(x=320,y=10+50,width=100,height=30)

s_time1=tk.StringVar()
input_s_time1 = Entry(root, textvariable=s_time1)
input_s_time1.insert(0, "(輸入起始時間)")
input_s_time1.place(x=425,y=10+50,width=100,height=30)

Labe1=tk.Label(root,text="~")
Labe1.place(x=532, y=15+50, width=20, height=20)

e_date1=tk.StringVar()
input_e_date1 = Entry(root, textvariable=e_date1)
input_e_date1.insert(0, "(輸入結束日期)")
input_e_date1.place(x=560,y=10+50,width=100,height=30)

e_time1=tk.StringVar()
input_e_time1 = Entry(root, textvariable=e_time1)
input_e_time1.insert(0, "(輸入結束時間)")
input_e_time1.place(x=665,y=10+50,width=100,height=30)

EVENT1=tk.StringVar()
input_EVENT1 = Entry(root, textvariable=EVENT1)
input_EVENT1.insert(0, "(輸入事件名稱)")
input_EVENT1.place(x=50,y=10+50,width=100,height=30)
################################################################
ID2=tk.StringVar()
input_ID2 = Entry(root, textvariable=ID2)
input_ID2.insert(0, "(輸入站點編號)")
input_ID2.place(x=185,y=10+50*2,width=100,height=30)

s_date2=tk.StringVar()
input_s_date2 = Entry(root, textvariable=s_date2)
input_s_date2.insert(0, "(輸入起始日期)")
input_s_date2.place(x=320,y=10+50*2,width=100,height=30)

s_time2=tk.StringVar()
input_s_time2 = Entry(root, textvariable=s_time2)
input_s_time2.insert(0, "(輸入起始時間)")
input_s_time2.place(x=425,y=10+50*2,width=100,height=30)

Labe2=tk.Label(root,text="~")
Labe2.place(x=532, y=15+50*2, width=20, height=20)

e_date2=tk.StringVar()
input_e_date2 = Entry(root, textvariable=e_date2)
input_e_date2.insert(0, "(輸入結束日期)")
input_e_date2.place(x=560,y=10+50*2,width=100,height=30)

e_time2=tk.StringVar()
input_e_time2 = Entry(root, textvariable=e_time2)
input_e_time2.insert(0, "(輸入結束時間)")
input_e_time2.place(x=665,y=10+50*2,width=100,height=30)

EVENT2=tk.StringVar()
input_EVENT2 = Entry(root, textvariable=EVENT2)
input_EVENT2.insert(0, "(輸入事件名稱)")
input_EVENT2.place(x=50,y=10+50*2,width=100,height=30)
################################################################
ID3=tk.StringVar()
input_ID3 = Entry(root, textvariable=ID3)
input_ID3.insert(0, "(輸入站點編號)")
input_ID3.place(x=185,y=10+50*3,width=100,height=30)

s_date3=tk.StringVar()
input_s_date3 = Entry(root, textvariable=s_date3)
input_s_date3.insert(0, "(輸入起始日期)")
input_s_date3.place(x=320,y=10+50*3,width=100,height=30)

s_time3=tk.StringVar()
input_s_time3 = Entry(root, textvariable=s_time3)
input_s_time3.insert(0, "(輸入起始時間)")
input_s_time3.place(x=425,y=10+50*3,width=100,height=30)

Labe3=tk.Label(root,text="~")
Labe3.place(x=532, y=15+50*3, width=20, height=20)

e_date3=tk.StringVar()
input_e_date3 = Entry(root, textvariable=e_date3)
input_e_date3.insert(0, "(輸入結束日期)")
input_e_date3.place(x=560,y=10+50*3,width=100,height=30)

e_time3=tk.StringVar()
input_e_time3 = Entry(root, textvariable=e_time3)
input_e_time3.insert(0, "(輸入結束時間)")
input_e_time3.place(x=665,y=10+50*3,width=100,height=30)

EVENT3=tk.StringVar()
input_EVENT3 = Entry(root, textvariable=EVENT3)
input_EVENT3.insert(0, "(輸入事件名稱)")
input_EVENT3.place(x=50,y=10+50*3,width=100,height=30)
################################################################
ID4=tk.StringVar()
input_ID4 = Entry(root, textvariable=ID4)
input_ID4.insert(0, "(輸入站點編號)")
input_ID4.place(x=185,y=10+50*4,width=100,height=30)

s_date4=tk.StringVar()
input_s_date4 = Entry(root, textvariable=s_date4)
input_s_date4.insert(0, "(輸入起始日期)")
input_s_date4.place(x=320,y=10+50*4,width=100,height=30)

s_time4=tk.StringVar()
input_s_time4 = Entry(root, textvariable=s_time4)
input_s_time4.insert(0, "(輸入起始時間)")
input_s_time4.place(x=425,y=10+50*4,width=100,height=30)

Labe4=tk.Label(root,text="~")
Labe4.place(x=532, y=15+50*4, width=20, height=20)

e_date4=tk.StringVar()
input_e_date4 = Entry(root, textvariable=e_date4)
input_e_date4.insert(0, "(輸入結束日期)")
input_e_date4.place(x=560,y=10+50*4,width=100,height=30)

e_time4=tk.StringVar()
input_e_time4 = Entry(root, textvariable=e_time4)
input_e_time4.insert(0, "(輸入結束時間)")
input_e_time4.place(x=665,y=10+50*4,width=100,height=30)

EVENT4=tk.StringVar()
input_EVENT4 = Entry(root, textvariable=EVENT4)
input_EVENT4.insert(0, "(輸入事件名稱)")
input_EVENT4.place(x=50,y=10+50*4,width=100,height=30)
################################################################
ID5=tk.StringVar()
input_ID5 = Entry(root, textvariable=ID5)
input_ID5.insert(0, "(輸入站點編號)")
input_ID5.place(x=185,y=10+50*5,width=100,height=30)

s_date5=tk.StringVar()
input_s_date5 = Entry(root, textvariable=s_date5)
input_s_date5.insert(0, "(輸入起始日期)")
input_s_date5.place(x=320,y=10+50*5,width=100,height=30)

s_time5=tk.StringVar()
input_s_time5 = Entry(root, textvariable=s_time5)
input_s_time5.insert(0, "(輸入起始時間)")
input_s_time5.place(x=425,y=10+50*5,width=100,height=30)

Labe5=tk.Label(root,text="~")
Labe5.place(x=532, y=15+50*5, width=20, height=20)

e_date5=tk.StringVar()
input_e_date5 = Entry(root, textvariable=e_date5)
input_e_date5.insert(0, "(輸入結束日期)")
input_e_date5.place(x=560,y=10+50*5,width=100,height=30)

e_time5=tk.StringVar()
input_e_time5 = Entry(root, textvariable=e_time5)
input_e_time5.insert(0, "(輸入結束時間)")
input_e_time5.place(x=665,y=10+50*5,width=100,height=30)

EVENT5=tk.StringVar()
input_EVENT5 = Entry(root, textvariable=EVENT5)
input_EVENT5.insert(0, "(輸入事件名稱)")
input_EVENT5.place(x=50,y=10+50*5,width=100,height=30)
################################################################
ID6=tk.StringVar()
input_ID6 = Entry(root, textvariable=ID6)
input_ID6.insert(0, "(輸入站點編號)")
input_ID6.place(x=185,y=10+50*6,width=100,height=30)

s_date6=tk.StringVar()
input_s_date6 = Entry(root, textvariable=s_date6)
input_s_date6.insert(0, "(輸入起始日期)")
input_s_date6.place(x=320,y=10+50*6,width=100,height=30)

s_time6=tk.StringVar()
input_s_time6 = Entry(root, textvariable=s_time6)
input_s_time6.insert(0, "(輸入起始時間)")
input_s_time6.place(x=425,y=10+50*6,width=100,height=30)

Labe6=tk.Label(root,text="~")
Labe6.place(x=532, y=15+50*6, width=20, height=20)

e_date6=tk.StringVar()
input_e_date6 = Entry(root, textvariable=e_date6)
input_e_date6.insert(0, "(輸入結束日期)")
input_e_date6.place(x=560,y=10+50*6,width=100,height=30)

e_time6=tk.StringVar()
input_e_time6 = Entry(root, textvariable=e_time6)
input_e_time6.insert(0, "(輸入結束時間)")
input_e_time6.place(x=665,y=10+50*6,width=100,height=30)

EVENT6=tk.StringVar()
input_EVENT6 = Entry(root, textvariable=EVENT6)
input_EVENT6.insert(0, "(輸入事件名稱)")
input_EVENT6.place(x=50,y=10+50*6,width=100,height=30)
################################################################
ID7=tk.StringVar()
input_ID7 = Entry(root, textvariable=ID7)
input_ID7.insert(0, "(輸入站點編號)")
input_ID7.place(x=185,y=10+50*7,width=100,height=30)

s_date7=tk.StringVar()
input_s_date7 = Entry(root, textvariable=s_date7)
input_s_date7.insert(0, "(輸入起始日期)")
input_s_date7.place(x=320,y=10+50*7,width=100,height=30)

s_time7=tk.StringVar()
input_s_time7 = Entry(root, textvariable=s_time7)
input_s_time7.insert(0, "(輸入起始時間)")
input_s_time7.place(x=425,y=10+50*7,width=100,height=30)

Labe7=tk.Label(root,text="~")
Labe7.place(x=532, y=15+50*7, width=20, height=20)

e_date7=tk.StringVar()
input_e_date7 = Entry(root, textvariable=e_date7)
input_e_date7.insert(0, "(輸入結束日期)")
input_e_date7.place(x=560,y=10+50*7,width=100,height=30)

e_time7=tk.StringVar()
input_e_time7 = Entry(root, textvariable=e_time7)
input_e_time7.insert(0, "(輸入結束時間)")
input_e_time7.place(x=665,y=10+50*7,width=100,height=30)

EVENT7=tk.StringVar()
input_EVENT7 = Entry(root, textvariable=EVENT7)
input_EVENT7.insert(0, "(輸入事件名稱)")
input_EVENT7.place(x=50,y=10+50*7,width=100,height=30)
################################################################
ID8=tk.StringVar()
input_ID8 = Entry(root, textvariable=ID8)
input_ID8.insert(0, "(輸入站點編號)")
input_ID8.place(x=185,y=10+50*8,width=100,height=30)

s_date8=tk.StringVar()
input_s_date8 = Entry(root, textvariable=s_date8)
input_s_date8.insert(0, "(輸入起始日期)")
input_s_date8.place(x=320,y=10+50*8,width=100,height=30)

s_time8=tk.StringVar()
input_s_time8 = Entry(root, textvariable=s_time8)
input_s_time8.insert(0, "(輸入起始時間)")
input_s_time8.place(x=425,y=10+50*8,width=100,height=30)

Labe8=tk.Label(root,text="~")
Labe8.place(x=532, y=15+50*8, width=20, height=20)

e_date8=tk.StringVar()
input_e_date8 = Entry(root, textvariable=e_date8)
input_e_date8.insert(0, "(輸入結束日期)")
input_e_date8.place(x=560,y=10+50*8,width=100,height=30)

e_time8=tk.StringVar()
input_e_time8 = Entry(root, textvariable=e_time8)
input_e_time8.insert(0, "(輸入結束時間)")
input_e_time8.place(x=665,y=10+50*8,width=100,height=30)

EVENT8=tk.StringVar()
input_EVENT8 = Entry(root, textvariable=EVENT8)
input_EVENT8.insert(0, "(輸入事件名稱)")
input_EVENT8.place(x=50,y=10+50*8,width=100,height=30)
################################################################
ID9=tk.StringVar()
input_ID9 = Entry(root, textvariable=ID9)
input_ID9.insert(0, "(輸入站點編號)")
input_ID9.place(x=185,y=10+50*9,width=100,height=30)

s_date9=tk.StringVar()
input_s_date9 = Entry(root, textvariable=s_date9)
input_s_date9.insert(0, "(輸入起始日期)")
input_s_date9.place(x=320,y=10+50*9,width=100,height=30)

s_time9=tk.StringVar()
input_s_time9 = Entry(root, textvariable=s_time9)
input_s_time9.insert(0, "(輸入起始時間)")
input_s_time9.place(x=425,y=10+50*9,width=100,height=30)

Labe9=tk.Label(root,text="~")
Labe9.place(x=532, y=15+50*9, width=20, height=20)

e_date9=tk.StringVar()
input_e_date9 = Entry(root, textvariable=e_date9)
input_e_date9.insert(0, "(輸入結束日期)")
input_e_date9.place(x=560,y=10+50*9,width=100,height=30)

e_time9=tk.StringVar()
input_e_time9 = Entry(root, textvariable=e_time9)
input_e_time9.insert(0, "(輸入結束時間)")
input_e_time9.place(x=665,y=10+50*9,width=100,height=30)

EVENT9=tk.StringVar()
input_EVENT9 = Entry(root, textvariable=EVENT9)
input_EVENT9.insert(0, "(輸入事件名稱)")
input_EVENT9.place(x=50,y=10+50*9,width=100,height=30)
################################################################
ID10=tk.StringVar()
input_ID10 = Entry(root, textvariable=ID10)
input_ID10.insert(0, "(輸入站點編號)")
input_ID10.place(x=185,y=10+50*10,width=100,height=30)

s_date10=tk.StringVar()
input_s_date10 = Entry(root, textvariable=s_date10)
input_s_date10.insert(0, "(輸入起始日期)")
input_s_date10.place(x=320,y=10+50*10,width=100,height=30)

s_time10=tk.StringVar()
input_s_time10 = Entry(root, textvariable=s_time10)
input_s_time10.insert(0, "(輸入起始時間)")
input_s_time10.place(x=425,y=10+50*10,width=100,height=30)

Labe10=tk.Label(root,text="~")
Labe10.place(x=532, y=15+50*10, width=20, height=20)

e_date10=tk.StringVar()
input_e_date10 = Entry(root, textvariable=e_date10)
input_e_date10.insert(0, "(輸入結束日期)")
input_e_date10.place(x=560,y=10+50*10,width=100,height=30)

e_time10=tk.StringVar()
input_e_time10 = Entry(root, textvariable=e_time10)
input_e_time10.insert(0, "(輸入結束時間)")
input_e_time10.place(x=665,y=10+50*10,width=100,height=30)

EVENT10=tk.StringVar()
input_EVENT10 = Entry(root, textvariable=EVENT10)
input_EVENT10.insert(0, "(輸入事件名稱)")
input_EVENT10.place(x=50,y=10+50*10,width=100,height=30)


def b_plus1():
    button_plus1.configure(bg="FireBrick")
    global ID1,s_d1,s_t1,e_d1,e_t1,EVENT1,Y11,M11,D11,Y21,M21,D21
    ID1=(input_ID1.get())
    s_d1=str(input_s_date1.get())
    s_t1=str(input_s_time1.get())
    e_d1=str(input_e_date1.get())
    e_t1=str(input_e_time1.get())
    EVENT1=str(input_EVENT1.get())

    Y11 = s_d1.split('-')[0]     
    M11 = s_d1.split('-')[1]
    D11 = s_d1.split('-')[2]
    Y21 = e_d1.split('-')[0]
    M21 = e_d1.split('-')[1]
    D21 = e_d1.split('-')[2]
    button_plus1.configure(bg="DimGray")
#------------

def b_plus2():
    button_plus2.configure(bg="FireBrick")
    global ID2,s_d2,s_t2,e_d2,e_t2,EVENT2,Y12,M12,D12,Y22,M22,D22
    ID2=(input_ID2.get())
    s_d2=str(input_s_date2.get())
    s_t2=str(input_s_time2.get())
    e_d2=str(input_e_date2.get())
    e_t2=str(input_e_time2.get())
    EVENT2=str(input_EVENT2.get())

    Y12 = s_d2.split('-')[0]     
    M12 = s_d2.split('-')[1]
    D12 = s_d2.split('-')[2]
    Y22 = e_d2.split('-')[0]
    M22 = e_d2.split('-')[1]
    D22 = e_d2.split('-')[2]
    button_plus2.configure(bg="DimGray")
#------------

def b_plus3():
    button_plus3.configure(bg="FireBrick")
    global ID3,s_d3,s_t3,e_d3,e_t3,EVENT3,Y13,M13,D13,Y23,M23,D23
    ID3=(input_ID3.get())
    s_d3=str(input_s_date3.get())
    s_t3=str(input_s_time3.get())
    e_d3=str(input_e_date3.get())
    e_t3=str(input_e_time3.get())
    EVENT3=str(input_EVENT3.get())

    Y13 = s_d3.split('-')[0]     
    M13 = s_d3.split('-')[1]
    D13 = s_d3.split('-')[2]
    Y23 = e_d3.split('-')[0]
    M23 = e_d3.split('-')[1]
    D23 = e_d3.split('-')[2]
    button_plus3.configure(bg="DimGray")
#------------

def b_plus4():
    button_plus4.configure(bg="FireBrick")
    global ID4,s_d4,s_t4,e_d4,e_t4,EVENT4,Y14,M14,D14,Y24,M24,D24
    ID4=(input_ID4.get())
    s_d4=str(input_s_date4.get())
    s_t4=str(input_s_time4.get())
    e_d4=str(input_e_date4.get())
    e_t4=str(input_e_time4.get())
    EVENT4=str(input_EVENT4.get())

    Y14 = s_d4.split('-')[0]     
    M14 = s_d4.split('-')[1]
    D14 = s_d4.split('-')[2]
    Y24 = e_d4.split('-')[0]
    M24 = e_d4.split('-')[1]
    D24 = e_d4.split('-')[2]
    button_plus4.configure(bg="DimGray")
#------------

def b_plus5():
    button_plus5.configure(bg="FireBrick")
    global ID5,s_d5,s_t5,e_d5,e_t5,EVENT5,Y15,M15,D15,Y25,M25,D25
    ID5=(input_ID5.get())
    s_d5=str(input_s_date5.get())
    s_t5=str(input_s_time5.get())
    e_d5=str(input_e_date5.get())
    e_t5=str(input_e_time5.get())
    EVENT5=str(input_EVENT5.get())

    Y15 = s_d5.split('-')[0]     
    M15 = s_d5.split('-')[1]
    D15 = s_d5.split('-')[2]
    Y25 = e_d5.split('-')[0]
    M25 = e_d5.split('-')[1]
    D25 = e_d5.split('-')[2]
    button_plus5.configure(bg="DimGray")
#------------

def b_plus6():
    button_plus6.configure(bg="FireBrick")
    global ID6,s_d6,s_t6,e_d6,e_t6,EVENT6,Y16,M16,D16,Y26,M26,D26
    ID6=(input_ID6.get())
    s_d6=str(input_s_date6.get())
    s_t6=str(input_s_time6.get())
    e_d6=str(input_e_date6.get())
    e_t6=str(input_e_time6.get())
    EVENT6=str(input_EVENT6.get())

    Y16 = s_d6.split('-')[0]     
    M16 = s_d6.split('-')[1]
    D16 = s_d6.split('-')[2]
    Y26 = e_d6.split('-')[0]
    M26 = e_d6.split('-')[1]
    D26 = e_d6.split('-')[2]
    button_plus6.configure(bg="DimGray")
#------------

def b_plus7():
    button_plus7.configure(bg="FireBrick")
    global ID7,s_d7,s_t7,e_d7,e_t7,EVENT7,Y17,M17,D17,Y27,M27,D27
    ID7=(input_ID7.get())
    s_d7=str(input_s_date7.get())
    s_t7=str(input_s_time7.get())
    e_d7=str(input_e_date7.get())
    e_t7=str(input_e_time7.get())
    EVENT7=str(input_EVENT7.get())

    Y17 = s_d7.split('-')[0]     
    M17 = s_d7.split('-')[1]
    D17 = s_d7.split('-')[2]
    Y27 = e_d7.split('-')[0]
    M27 = e_d7.split('-')[1]
    D27 = e_d7.split('-')[2]
    button_plus7.configure(bg="DimGray")
#------------

def b_plus8():
    button_plus8.configure(bg="FireBrick")
    global ID8,s_d8,s_t8,e_d8,e_t8,EVENT8,Y18,M18,D18,Y28,M28,D28
    ID8=(input_ID8.get())
    s_d8=str(input_s_date8.get())
    s_t8=str(input_s_time8.get())
    e_d8=str(input_e_date8.get())
    e_t8=str(input_e_time8.get())
    EVENT8=str(input_EVENT8.get())

    Y18 = s_d8.split('-')[0]     
    M18 = s_d8.split('-')[1]
    D18 = s_d8.split('-')[2]
    Y28 = e_d8.split('-')[0]
    M28 = e_d8.split('-')[1]
    D28 = e_d8.split('-')[2]
    button_plus8.configure(bg="DimGray")
#------------

def b_plus9():
    button_plus9.configure(bg="FireBrick")
    global ID9,s_d9,s_t9,e_d9,e_t9,EVENT9,Y19,M19,D19,Y29,M29,D29
    ID9=(input_ID9.get())
    s_d9=str(input_s_date9.get())
    s_t9=str(input_s_time9.get())
    e_d9=str(input_e_date9.get())
    e_t9=str(input_e_time9.get())
    EVENT9=str(input_EVENT9.get())

    Y19 = s_d9.split('-')[0]     
    M19 = s_d9.split('-')[1]
    D19 = s_d9.split('-')[2]
    Y29 = e_d9.split('-')[0]
    M29 = e_d9.split('-')[1]
    D29 = e_d9.split('-')[2]
    button_plus9.configure(bg="DimGray")
#------------

def b_plus10():
    button_plus10.configure(bg="FireBrick")
    global ID10,s_d10,s_t10,e_d10,e_t10,EVENT10,Y110,M110,D110,Y210,M210,D210
    ID10=(input_ID10.get())
    s_d10=str(input_s_date10.get())
    s_t10=str(input_s_time10.get())
    e_d10=str(input_e_date10.get())
    e_t10=str(input_e_time10.get())
    EVENT10=str(input_EVENT10.get())

    Y110 = s_d10.split('-')[0]     
    M110 = s_d10.split('-')[1]
    D110 = s_d10.split('-')[2]
    Y201 = e_d10.split('-')[0]
    M210 = e_d10.split('-')[1]
    D210 = e_d10.split('-')[2]
    button_plus10.configure(bg="DimGray")
#------------

def b_start():                                          ##########################
    button_start.configure(bg="darkgray")
    global rainfall1,Time1,TH1,r1,s_d1,s_t1,e_d1,e_t1,d1
    global rainfall2,Time2,TH2,r2,s_d2,s_t2,e_d2,e_t2,d2
    global rainfall3,Time3,TH3,r3,s_d3,s_t3,e_d3,e_t3,d3
    global rainfall4,Time4,TH4,r4,s_d4,s_t4,e_d4,e_t4,d4
    global rainfall5,Time5,TH5,r5,s_d5,s_t5,e_d5,e_t5,d5
    global rainfall6,Time6,TH6,r6,s_d6,s_t6,e_d6,e_t6,d6
    global rainfall7,Time7,TH7,r7,s_d7,s_t7,e_d7,e_t7,d7
    global rainfall8,Time8,TH8,r8,s_d8,s_t8,e_d8,e_t8,d8
    global rainfall9,Time9,TH9,r9,s_d9,s_t9,e_d9,e_t9,d9
    global rainfall10,Time10,TH10,r10,s_d10,s_t10,e_d10,e_t10,d10
    global DF
    try:
        M1=[]
        D1=[]
        st_no1=[]

        yy1=[]
        mm1=[]
        dd1=[]

        HQ011=[]
        HQ021=[]
        HQ031=[]
        HQ041=[]
        HQ051=[]
        HQ061=[]
        HQ071=[]
        HQ081=[]
        HQ091=[]
        HQ101=[]
        HQ111=[]
        HQ121=[]
        HQ131=[]
        HQ141=[]
        HQ151=[]
        HQ161=[]
        HQ171=[]
        HQ181=[]
        HQ191=[]
        HQ201=[]
        HQ211=[]
        HQ221=[]
        HQ231=[]
        HQ241=[]
    
        rainfall1=[]
        Time1=[]
        TH1=[]
        r1=0
   
        if int(M21)-int(M11)>1:
            for i in range(31-int(D11)+1):
                M1.append(int(M11))
            for i in range(int(D11),32):
                D1.append(i)
            for i in range(int(M11)+1,int(M21)):
                for j in range(1,32):
                    M1.append(i)
            for i in range(int(M11),int(M21)-1):
                for j in range(1,32):
                    D1.append(j)
            for i in range(int(D21)):
                M1.append(int(M21))
            for i in range(1,int(D21)+1):
                D1.append(i)                
        elif int(M21)-int(M11)==1:
            for i in range(31-int(D11)+1):
                M1.append(int(M11))
            for i in range(int(D11),32):
                D1.append(i)
            for i in range(int(D21)):
                M1.append(int(M21))
            for i in range(1,int(D21)+1):
                D1.append(i)
        else:
            for i in range(int(D21)-int(D11)+1):
                M1.append(int(M11))
            for i in range(int(D11),int(D21)+1):
                D1.append(i)

        OUT1=[]
        SAVE_M1=[]
        SAVE_D1=[]
        for i in range(len(M1)):
        # print(M[i],D[i])
            if (M1[i]==2 and D1[i]>28) or (M1[i]==4 and D1[i]>30) or (M1[i]==6 and D1[i]>30) or (M1[i]==9 and D1[i]>30) or (M1[i]==11 and D1[i]>30):
                OUT1.append(i)
            
        for i in range(len(M1)):
            if i not in OUT1:
                SAVE_M1.append(M1[i])
                SAVE_D1.append(D1[i])  
        M1=SAVE_M1
        D1=SAVE_D1       

        for i in range(len(M1)):
            Yy1=Y11
            if M1[i]<10:
                Mm1='0{}'.format(M1[i])
            else:
                Mm1=str(M1[i])
    
            if D1[i]<10:
                Dd1='0{}'.format(D1[i])
            else:
                Dd1=str(D1[i])
            
            url1 = r'https://e-service.cwb.gov.tw/HistoryDataQuery/DayDataController.do?command=viewMain&station={0}&stname=%25E4%25B8%258A%25E5%25BE%25B7%25E6%2596%2587&datepicker={1}-{2}-{3}#'.format(ID1,Yy1,Mm1,Dd1)
        
            re1 = requests.get(url1) 
            soup1 = BeautifulSoup(re1.text, "html.parser")
            result1 = soup1.find_all("td")
            RR1 = soup1.find_all("head")
            t1 = str(RR1).split(";")
            x1 = t1[4].split("\"")
            y1=x1[1].split("-")
            st_no1.append(y1[0])
            dd1.append(y1[3]) 
            mm1.append(y1[2])
            yy1.append(y1[1])
    
            HQ011.append((str(result1[20]).split())[0].split(">")[1])  #01
            try:
                r1=r1+float((str(result1[20]).split())[0].split(">")[1])
            except:
                r1=r1
            rainfall1.append(r1)
            Time1.append('{0}-{1}-{2} 01:00'.format(Yy1,Mm1,Dd1)) 
            HQ021.append((str(result1[37]).split())[0].split(">")[1])  #02
            try:
                r1=r1+float((str(result1[37]).split())[0].split(">")[1])
            except:
                r1=r1
            rainfall1.append(r1)
            Time1.append('{0}-{1}-{2} 02:00'.format(Yy1,Mm1,Dd1))
            HQ031.append((str(result1[54]).split())[0].split(">")[1])  #03
            try:
                r1=r1+float((str(result1[54]).split())[0].split(">")[1])
            except:
                r1=r1
            rainfall1.append(r1)
            Time1.append('{0}-{1}-{2} 03:00'.format(Yy1,Mm1,Dd1))
            HQ041.append((str(result1[71]).split())[0].split(">")[1])  #04
            try:
                r1=r1+float((str(result1[71]).split())[0].split(">")[1])
            except:
                r1=r1
            rainfall1.append(r1)
            Time1.append('{0}-{1}-{2} 04:00'.format(Yy1,Mm1,Dd1))
            HQ051.append((str(result1[88]).split())[0].split(">")[1])  #05
            try:
                r1=r1+float((str(result1[88]).split())[0].split(">")[1])
            except:
                r1=r1
            rainfall1.append(r1)
            Time1.append('{0}-{1}-{2} 05:00'.format(Yy1,Mm1,Dd1))
            HQ061.append((str(result1[105]).split())[0].split(">")[1])  #06
            try:
                r1=r1+float((str(result1[105]).split())[0].split(">")[1])
            except:
                r1=r1
            rainfall1.append(r1)
            Time1.append('{0}-{1}-{2} 06:00'.format(Yy1,Mm1,Dd1))
            HQ071.append((str(result1[122]).split())[0].split(">")[1])  #07 
            try:
                r1=r1+float((str(result1[122]).split())[0].split(">")[1])
            except:
                r1=r1
            rainfall1.append(r1)
            Time1.append('{0}-{1}-{2} 07:00'.format(Yy1,Mm1,Dd1))
            HQ081.append((str(result1[139]).split())[0].split(">")[1])  #08
            try:
                r1=r1+float((str(result1[139]).split())[0].split(">")[1])
            except:
                r1=r1
            rainfall1.append(r1)
            Time1.append('{0}-{1}-{2} 08:00'.format(Yy1,Mm1,Dd1))
            HQ091.append((str(result1[156]).split())[0].split(">")[1])  #09
            try:
                r1=r1+float((str(result1[156]).split())[0].split(">")[1])
            except:
                r1=r1
            rainfall1.append(r1)
            Time1.append('{0}-{1}-{2} 09:00'.format(Yy1,Mm1,Dd1))
            HQ101.append((str(result1[173]).split())[0].split(">")[1])  #10
            try:
                r1=r1+float((str(result1[173]).split())[0].split(">")[1])
            except:
                r1=r1
            rainfall1.append(r1)
            Time1.append('{0}-{1}-{2} 10:00'.format(Yy1,Mm1,Dd1))
            HQ111.append((str(result1[190]).split())[0].split(">")[1])  #11
            try:
                r1=r1+float((str(result1[190]).split())[0].split(">")[1])
            except:
                r1=r1
            rainfall1.append(r1)
            Time1.append('{0}-{1}-{2} 11:00'.format(Yy1,Mm1,Dd1))
            HQ121.append((str(result1[207]).split())[0].split(">")[1])  #12
            try:
                r1=r1+float((str(result1[207]).split())[0].split(">")[1])
            except:
                r1=r1
            rainfall1.append(r1)
            Time1.append('{0}-{1}-{2} 12:00'.format(Yy1,Mm1,Dd1))
            HQ131.append((str(result1[224]).split())[0].split(">")[1])  #13
            try:
                r1=r1+float((str(result1[224]).split())[0].split(">")[1])
            except:
                r1=r1
            rainfall1.append(r1)
            Time1.append('{0}-{1}-{2} 13:00'.format(Yy1,Mm1,Dd1))
            HQ141.append((str(result1[241]).split())[0].split(">")[1])  #14
            try:
                r1=r1+float((str(result1[241]).split())[0].split(">")[1])
            except:
                r1=r1
            rainfall1.append(r1)
            Time1.append('{0}-{1}-{2} 14:00'.format(Yy1,Mm1,Dd1))
            HQ151.append((str(result1[258]).split())[0].split(">")[1])  #15
            try:
                r1=r1+float((str(result1[258]).split())[0].split(">")[1])
            except:
                r1=r1
            rainfall1.append(r1)
            Time1.append('{0}-{1}-{2} 15:00'.format(Yy1,Mm1,Dd1))
            HQ161.append((str(result1[275]).split())[0].split(">")[1])  #16
            try:
                r1=r1+float((str(result1[275]).split())[0].split(">")[1])
            except:
                r1=r1
            rainfall1.append(r1)
            Time1.append('{0}-{1}-{2} 16:00'.format(Yy1,Mm1,Dd1))
            HQ171.append((str(result1[292]).split())[0].split(">")[1])  #17
            try:
                r1=r1+float((str(result1[292]).split())[0].split(">")[1])
            except:
                r1=r1
            rainfall1.append(r1)
            Time1.append('{0}-{1}-{2} 17:00'.format(Yy1,Mm1,Dd1))
            HQ181.append((str(result1[309]).split())[0].split(">")[1])  #18
            try:
                r1=r1+float((str(result1[309]).split())[0].split(">")[1])
            except:
                r1=r1
            rainfall1.append(r1)
            Time1.append('{0}-{1}-{2} 18:00'.format(Yy1,Mm1,Dd1))
            HQ191.append((str(result1[326]).split())[0].split(">")[1])  #19
            try:
                r1=r1+float((str(result1[326]).split())[0].split(">")[1])
            except:
                r1=r1
            rainfall1.append(r1)
            Time1.append('{0}-{1}-{2} 19:00'.format(Yy1,Mm1,Dd1))
            HQ201.append((str(result1[343]).split())[0].split(">")[1])  #20
            try:
                r1=r1+float((str(result1[343]).split())[0].split(">")[1])
            except:
                r1=r1
            rainfall1.append(r1)
            Time1.append('{0}-{1}-{2} 20:00'.format(Yy1,Mm1,Dd1))
            HQ211.append((str(result1[360]).split())[0].split(">")[1])  #21
            try:
                r1=r1+float((str(result1[360]).split())[0].split(">")[1])
            except:
                r1=r1
            rainfall1.append(r1)
            Time1.append('{0}-{1}-{2} 21:00'.format(Yy1,Mm1,Dd1))
            HQ221.append((str(result1[377]).split())[0].split(">")[1])  #22
            try:
                r1=r1+float((str(result1[377]).split())[0].split(">")[1])
            except:
                r1=r1
            rainfall1.append(r1)
            Time1.append('{0}-{1}-{2} 22:00'.format(Yy1,Mm1,Dd1))
            HQ231.append((str(result1[394]).split())[0].split(">")[1])  #23
            try:
                r1=r1+float((str(result1[394]).split())[0].split(">")[1])
            except:
                r1=r1
            rainfall1.append(r1)
            Time1.append('{0}-{1}-{2} 23:00'.format(Yy1,Mm1,Dd1))
            HQ241.append((str(result1[411]).split())[0].split(">")[1])  #24
            try:
                r1=r1+float((str(result1[411]).split())[0].split(">")[1])
            except:
                r1=r1
            rainfall1.append(r1)
            Time1.append('{0}-{1}-{2} 24:00'.format(Yy1,Mm1,Dd1))

            d1 = {
                "st_no":st_no1,
                "yy":yy1,
                "mm":mm1,
                "dd":dd1,
                "HQ01":HQ011,
                "HQ02":HQ021,
                "HQ03":HQ031,
                "HQ04":HQ041,
                "HQ05":HQ051,
                "HQ06":HQ061,
                "HQ07":HQ071,
                "HQ08":HQ081,
                "HQ09":HQ091,
                "HQ10":HQ101,
                "HQ11":HQ111,
                "HQ12":HQ121,
                "HQ13":HQ131,
                "HQ14":HQ141,
                "HQ15":HQ151,
                "HQ16":HQ161,
                "HQ17":HQ171,
                "HQ18":HQ181,
                "HQ19":HQ191,
                "HQ20":HQ201,
                "HQ21":HQ211,
                "HQ22":HQ221,
                "HQ23":HQ231,
                "HQ24":HQ241,
                }
    
            time.sleep(random.uniform(0,0.1))

        START1=("{0} {1}:00".format(s_d1,s_t1))
        END1=("{0} {1}:00".format(e_d1,e_t1))
        for i in range(len(Time1)):
            if START1 == Time1[i]:
                SC1=i    
            if END1 == Time1[i]:
                EC1=i+1 

        del Time1[EC1:]
        del rainfall1[EC1:]
        del Time1[0:SC1]
        del rainfall1[0:SC1]
    
        for i in range(len(Time1)):
            TH1.append(i+1)

        T1=TH1
        RF1=rainfall1

        df1_test=(pd.DataFrame(data = d1))

        print("1-OKKK")
        button_start.configure(bg="Maroon")
        button_plus1.configure(bg="DarkGoldenrod")
    except:
        print("1-NO")
        button_start.configure(bg="Maroon")
        pass
    ################ˇˇ
    try:
        M2=[]
        D2=[]
        st_no2=[]

        yy2=[]
        mm2=[]
        dd2=[]

        HQ012=[]
        HQ022=[]
        HQ032=[]
        HQ042=[]
        HQ052=[]
        HQ062=[]
        HQ072=[]
        HQ082=[]
        HQ092=[]
        HQ102=[]
        HQ112=[]
        HQ122=[]
        HQ132=[]
        HQ142=[]
        HQ152=[]
        HQ162=[]
        HQ172=[]
        HQ182=[]
        HQ192=[]
        HQ202=[]
        HQ212=[]
        HQ222=[]
        HQ232=[]
        HQ242=[]
    
        rainfall2=[]
        Time2=[]
        TH2=[]
        r2=0
   
        if int(M22)-int(M12)>1:
            for i in range(31-int(D12)+1):
                M2.append(int(M12))
            for i in range(int(D12),32):
                D2.append(i)
            for i in range(int(M12)+1,int(M22)):
                for j in range(1,32):
                    M2.append(i)
            for i in range(int(M12),int(M22)-1):
                for j in range(1,32):
                    D2.append(j)
            for i in range(int(D22)):
                M2.append(int(M22))
            for i in range(1,int(D22)+1):
                D2.append(i)                
        elif int(M22)-int(M12)==1:
            for i in range(31-int(D12)+1):
                M2.append(int(M12))
            for i in range(int(D12),32):
                D2.append(i)
            for i in range(int(D22)):
                M2.append(int(M22))
            for i in range(1,int(D22)+1):
                D2.append(i)
        else:
            for i in range(int(D22)-int(D12)+1):
                M2.append(int(M12))
            for i in range(int(D12),int(D22)+1):
                D2.append(i)

        OUT2=[]
        SAVE_M2=[]
        SAVE_D2=[]
        for i in range(len(M2)):
        # print(M[i],D[i])
            if (M2[i]==2 and D2[i]>28) or (M2[i]==4 and D2[i]>30) or (M2[i]==6 and D2[i]>30) or (M2[i]==9 and D2[i]>30) or (M2[i]==11 and D2[i]>30):
                OUT2.append(i)
            
        for i in range(len(M2)):
            if i not in OUT2:
                SAVE_M2.append(M2[i])
                SAVE_D2.append(D2[i])  
        M2=SAVE_M2
        D2=SAVE_D2       

        for i in range(len(M2)):
            Yy2=Y12
            if M2[i]<10:
                Mm2='0{}'.format(M2[i])
            else:
                Mm2=str(M2[i])
    
            if D2[i]<10:
                Dd2='0{}'.format(D2[i])
            else:
                Dd2=str(D2[i])
            
            url2 = r'https://e-service.cwb.gov.tw/HistoryDataQuery/DayDataController.do?command=viewMain&station={0}&stname=%25E4%25B8%258A%25E5%25BE%25B7%25E6%2596%2587&datepicker={1}-{2}-{3}#'.format(ID2,Yy2,Mm2,Dd2)
        
            re2 = requests.get(url2) 
            soup2 = BeautifulSoup(re2.text, "html.parser")
            result2 = soup2.find_all("td")
            RR2 = soup2.find_all("head")
            t2 = str(RR2).split(";")
            x2 = t2[4].split("\"")
            y2=x2[1].split("-")
            st_no2.append(y2[0])
            dd2.append(y2[3]) 
            mm2.append(y2[2])
            yy2.append(y2[1])
    
            HQ012.append((str(result2[20]).split())[0].split(">")[1])  #01
            try:
                r2=r2+float((str(result2[20]).split())[0].split(">")[1])
            except:
                r2=r2
            rainfall2.append(r2)
            Time2.append('{0}-{1}-{2} 01:00'.format(Yy2,Mm2,Dd2)) 
            HQ022.append((str(result2[37]).split())[0].split(">")[1])  #02
            try:
                r2=r2+float((str(result2[37]).split())[0].split(">")[1])
            except:
                r2=r2
            rainfall2.append(r2)
            Time2.append('{0}-{1}-{2} 02:00'.format(Yy2,Mm2,Dd2))
            HQ032.append((str(result2[54]).split())[0].split(">")[1])  #03
            try:
                r2=r2+float((str(result2[54]).split())[0].split(">")[1])
            except:
                r2=r2
            rainfall2.append(r2)
            Time2.append('{0}-{1}-{2} 03:00'.format(Yy2,Mm2,Dd2))
            HQ042.append((str(result2[71]).split())[0].split(">")[1])  #04
            try:
                r2=r2+float((str(result2[71]).split())[0].split(">")[1])
            except:
                r2=r2
            rainfall2.append(r2)
            Time2.append('{0}-{1}-{2} 04:00'.format(Yy2,Mm2,Dd2))
            HQ052.append((str(result2[88]).split())[0].split(">")[1])  #05 
            try:
                r2=r2+float((str(result2[88]).split())[0].split(">")[1])
            except:
                r2=r2
            rainfall2.append(r2)
            Time2.append('{0}-{1}-{2} 05:00'.format(Yy2,Mm2,Dd2))
            HQ062.append((str(result2[105]).split())[0].split(">")[1])  #06
            try:
                r2=r2+float((str(result2[105]).split())[0].split(">")[1])
            except:
                r2=r2
            rainfall2.append(r2)
            Time2.append('{0}-{1}-{2} 06:00'.format(Yy2,Mm2,Dd2))
            HQ072.append((str(result2[122]).split())[0].split(">")[1])  #07 
            try:
                r2=r2+float((str(result2[122]).split())[0].split(">")[1])
            except:
                r2=r2
            rainfall2.append(r2)
            Time2.append('{0}-{1}-{2} 07:00'.format(Yy2,Mm2,Dd2))
            HQ082.append((str(result2[139]).split())[0].split(">")[1])  #08
            try:
                r2=r2+float((str(result2[139]).split())[0].split(">")[1])
            except:
                r2=r2
            rainfall2.append(r2)
            Time2.append('{0}-{1}-{2} 08:00'.format(Yy2,Mm2,Dd2))
            HQ092.append((str(result2[156]).split())[0].split(">")[1])  #09
            try:
                r2=r2+float((str(result2[156]).split())[0].split(">")[1])
            except:
                r2=r2
            rainfall2.append(r2)
            Time2.append('{0}-{1}-{2} 09:00'.format(Yy2,Mm2,Dd2))
            HQ102.append((str(result2[173]).split())[0].split(">")[1])  #10
            try:
                r2=r2+float((str(result2[173]).split())[0].split(">")[1])
            except:
                r2=r2
            rainfall2.append(r2)
            Time2.append('{0}-{1}-{2} 10:00'.format(Yy2,Mm2,Dd2))
            HQ112.append((str(result2[190]).split())[0].split(">")[1])  #11
            try:
                r2=r2+float((str(result2[190]).split())[0].split(">")[1])
            except:
                r2=r2
            rainfall2.append(r2)
            Time2.append('{0}-{1}-{2} 11:00'.format(Yy2,Mm2,Dd2))
            HQ122.append((str(result2[207]).split())[0].split(">")[1])  #12
            try:
                r2=r2+float((str(result2[207]).split())[0].split(">")[1])
            except:
                r2=r2
            rainfall2.append(r2)
            Time2.append('{0}-{1}-{2} 12:00'.format(Yy2,Mm2,Dd2))
            HQ132.append((str(result2[224]).split())[0].split(">")[1])  #13
            try:
                r2=r2+float((str(result2[224]).split())[0].split(">")[1])
            except:
                r2=r2
            rainfall2.append(r2)
            Time2.append('{0}-{1}-{2} 13:00'.format(Yy2,Mm2,Dd2))
            HQ142.append((str(result2[241]).split())[0].split(">")[1])  #14
            try:
                r2=r2+float((str(result2[241]).split())[0].split(">")[1])
            except:
                r2=r2
            rainfall2.append(r2)
            Time2.append('{0}-{1}-{2} 14:00'.format(Yy2,Mm2,Dd2))
            HQ152.append((str(result2[258]).split())[0].split(">")[1])  #15
            try:
                r2=r2+float((str(result2[258]).split())[0].split(">")[1])
            except:
                r2=r2
            rainfall2.append(r2)
            Time2.append('{0}-{1}-{2} 15:00'.format(Yy2,Mm2,Dd2))
            HQ162.append((str(result2[275]).split())[0].split(">")[1])  #16
            try:
                r2=r2+float((str(result2[275]).split())[0].split(">")[1])
            except:
                r2=r2
            rainfall2.append(r2)
            Time2.append('{0}-{1}-{2} 16:00'.format(Yy2,Mm2,Dd2))
            HQ172.append((str(result2[292]).split())[0].split(">")[1])  #17
            try:
                r2=r2+float((str(result2[292]).split())[0].split(">")[1])
            except:
                r2=r2
            rainfall2.append(r2)
            Time2.append('{0}-{1}-{2} 17:00'.format(Yy2,Mm2,Dd2))
            HQ182.append((str(result2[309]).split())[0].split(">")[1])  #18
            try:
                r2=r2+float((str(result2[309]).split())[0].split(">")[1])
            except:
                r2=r2
            rainfall2.append(r2)
            Time2.append('{0}-{1}-{2} 18:00'.format(Yy2,Mm2,Dd2))
            HQ192.append((str(result2[326]).split())[0].split(">")[1])  #19
            try:
                r2=r2+float((str(result2[326]).split())[0].split(">")[1])
            except:
                r2=r2
            rainfall2.append(r2)
            Time2.append('{0}-{1}-{2} 19:00'.format(Yy2,Mm2,Dd2))
            HQ202.append((str(result2[343]).split())[0].split(">")[1])  #20
            try:
                r2=r2+float((str(result2[343]).split())[0].split(">")[1])
            except:
                r2=r2
            rainfall2.append(r2)
            Time2.append('{0}-{1}-{2} 20:00'.format(Yy2,Mm2,Dd2))
            HQ212.append((str(result2[360]).split())[0].split(">")[1])  #21
            try:
                r2=r2+float((str(result2[360]).split())[0].split(">")[1])
            except:
                r2=r2
            rainfall2.append(r2)
            Time2.append('{0}-{1}-{2} 21:00'.format(Yy2,Mm2,Dd2))
            HQ222.append((str(result2[377]).split())[0].split(">")[1])  #22
            try:
                r2=r2+float((str(result2[377]).split())[0].split(">")[1])
            except:
                r2=r2
            rainfall2.append(r2)
            Time2.append('{0}-{1}-{2} 22:00'.format(Yy2,Mm2,Dd2))
            HQ232.append((str(result2[394]).split())[0].split(">")[1])  #23
            try:
                r2=r2+float((str(result2[394]).split())[0].split(">")[1])
            except:
                r2=r2
            rainfall2.append(r2)
            Time2.append('{0}-{1}-{2} 23:00'.format(Yy2,Mm2,Dd2))
            HQ242.append((str(result2[411]).split())[0].split(">")[1])  #24
            try:
                r2=r2+float((str(result2[411]).split())[0].split(">")[1])
            except:
                r2=r2
            rainfall2.append(r2)
            Time2.append('{0}-{1}-{2} 24:00'.format(Yy2,Mm2,Dd2))

            d2 = {
                "st_no":st_no2,
                "yy":yy2,
                "mm":mm2,
                "dd":dd2,
                "HQ01":HQ012,
                "HQ02":HQ022,
                "HQ03":HQ032,
                "HQ04":HQ042,
                "HQ05":HQ052,
                "HQ06":HQ062,
                "HQ07":HQ072,
                "HQ08":HQ082,
                "HQ09":HQ092,
                "HQ10":HQ102,
                "HQ11":HQ112,
                "HQ12":HQ122,
                "HQ13":HQ132,
                "HQ14":HQ142,
                "HQ15":HQ152,
                "HQ16":HQ162,
                "HQ17":HQ172,
                "HQ18":HQ182,
                "HQ19":HQ192,
                "HQ20":HQ202,
                "HQ21":HQ212,
                "HQ22":HQ222,
                "HQ23":HQ232,
                "HQ24":HQ242,
                }
    
            time.sleep(random.uniform(0,0.1))

        START2=("{0} {1}:00".format(s_d2,s_t2))
        END2=("{0} {1}:00".format(e_d2,e_t2))
        for i in range(len(Time2)):
            if START2 == Time2[i]:
                SC2=i    
            if END2 == Time2[i]:
                EC2=i+1 

        del Time2[EC2:]
        del rainfall2[EC2:]
        del Time2[0:SC2]
        del rainfall2[0:SC2]
    
        for i in range(len(Time2)):
            TH2.append(i+1)

        T2=TH2
        RF2=rainfall2

        df2_test=(pd.DataFrame(data = d2))

        print("2-OKKK")
        button_start.configure(bg="Maroon")
        button_plus2.configure(bg="DarkGoldenrod")
    except:
        print("2-NO")
        button_start.configure(bg="Maroon")
        pass

       ########################
    try:
        M3=[]
        D3=[]
        st_no3=[]

        yy3=[]
        mm3=[]
        dd3=[]

        HQ013=[]
        HQ023=[]
        HQ033=[]
        HQ043=[]
        HQ053=[]
        HQ063=[]
        HQ073=[]
        HQ083=[]
        HQ093=[]
        HQ103=[]
        HQ113=[]
        HQ123=[]
        HQ133=[]
        HQ143=[]
        HQ153=[]
        HQ163=[]
        HQ173=[]
        HQ183=[]
        HQ193=[]
        HQ203=[]
        HQ213=[]
        HQ223=[]
        HQ233=[]
        HQ243=[]
    
        rainfall3=[]
        Time3=[]
        TH3=[]
        r3=0
   
        if int(M23)-int(M13)>1:
            for i in range(31-int(D13)+1):
                M3.append(int(M13))
            for i in range(int(D13),32):
                D3.append(i)
            for i in range(int(M13)+1,int(M23)):
                for j in range(1,32):
                    M3.append(i)
            for i in range(int(M13),int(M23)-1):
                for j in range(1,32):
                    D3.append(j)
            for i in range(int(D23)):
                M3.append(int(M23))
            for i in range(1,int(D23)+1):
                D3.append(i)                
        elif int(M23)-int(M13)==1:
            for i in range(31-int(D13)+1):
                M3.append(int(M13))
            for i in range(int(D13),32):
                D3.append(i)
            for i in range(int(D23)):
                M3.append(int(M23))
            for i in range(1,int(D23)+1):
                D3.append(i)
        else:
            for i in range(int(D23)-int(D13)+1):
                M3.append(int(M13))
            for i in range(int(D13),int(D23)+1):
                D3.append(i)

        OUT3=[]
        SAVE_M3=[]
        SAVE_D3=[]
        for i in range(len(M3)):
        # print(M[i],D[i])
            if (M3[i]==2 and D3[i]>28) or (M3[i]==4 and D3[i]>30) or (M3[i]==6 and D3[i]>30) or (M3[i]==9 and D3[i]>30) or (M3[i]==11 and D3[i]>30):
                OUT3.append(i)
            
        for i in range(len(M3)):
            if i not in OUT3:
                SAVE_M3.append(M3[i])
                SAVE_D3.append(D3[i])  
        M3=SAVE_M3
        D3=SAVE_D3       

        for i in range(len(M3)):
            Yy3=Y13
            if M3[i]<10:
                Mm3='0{}'.format(M3[i])
            else:
                Mm3=str(M3[i])
    
            if D3[i]<10:
                Dd3='0{}'.format(D3[i])
            else:
                Dd3=str(D3[i])
            
            url3 = r'https://e-service.cwb.gov.tw/HistoryDataQuery/DayDataController.do?command=viewMain&station={0}&stname=%25E4%25B8%258A%25E5%25BE%25B7%25E6%2596%2587&datepicker={1}-{2}-{3}#'.format(ID3,Yy3,Mm3,Dd3)
        
            re3 = requests.get(url3) 
            soup3 = BeautifulSoup(re3.text, "html.parser")
            result3 = soup3.find_all("td")
            RR3 = soup3.find_all("head")
            t3 = str(RR3).split(";")
            x3 = t3[4].split("\"")
            y3=x3[1].split("-")
            st_no3.append(y3[0])
            dd3.append(y3[3]) 
            mm3.append(y3[2])
            yy3.append(y3[1])
    
            HQ013.append((str(result3[20]).split())[0].split(">")[1])  #01
            try:
                r3=r3+float((str(result3[20]).split())[0].split(">")[1])
            except:
                r3=r3
            rainfall3.append(r3)
            Time3.append('{0}-{1}-{2} 01:00'.format(Yy3,Mm3,Dd3)) 
            HQ023.append((str(result3[37]).split())[0].split(">")[1])  #02
            try:
                r3=r3+float((str(result3[37]).split())[0].split(">")[1])
            except:
                r3=r3
            rainfall3.append(r3)
            Time3.append('{0}-{1}-{2} 02:00'.format(Yy3,Mm3,Dd3))
            HQ033.append((str(result3[54]).split())[0].split(">")[1])  #03
            try:
                r3=r3+float((str(result3[54]).split())[0].split(">")[1])
            except:
                r3=r3
            rainfall3.append(r3)
            Time3.append('{0}-{1}-{2} 03:00'.format(Yy3,Mm3,Dd3))
            HQ043.append((str(result3[71]).split())[0].split(">")[1])  #04
            try:
                r3=r3+float((str(result3[71]).split())[0].split(">")[1])
            except:
                r3=r3
            rainfall3.append(r3)
            Time3.append('{0}-{1}-{2} 04:00'.format(Yy3,Mm3,Dd3))
            HQ053.append((str(result3[88]).split())[0].split(">")[1])  #05 
            try:
                r3=r3+float((str(result3[88]).split())[0].split(">")[1])
            except:
                r3=r3
            rainfall3.append(r3)
            Time3.append('{0}-{1}-{2} 05:00'.format(Yy3,Mm3,Dd3))
            HQ063.append((str(result3[105]).split())[0].split(">")[1])  #06
            try:
                r3=r3+float((str(result3[105]).split())[0].split(">")[1])
            except:
                r3=r3
            rainfall3.append(r3)
            Time3.append('{0}-{1}-{2} 06:00'.format(Yy3,Mm3,Dd3))
            HQ073.append((str(result3[122]).split())[0].split(">")[1])  #07 
            try:
                r3=r3+float((str(result3[122]).split())[0].split(">")[1])
            except:
                r3=r3
            rainfall3.append(r3)
            Time3.append('{0}-{1}-{2} 07:00'.format(Yy3,Mm3,Dd3))
            HQ083.append((str(result3[139]).split())[0].split(">")[1])  #08
            try:
                r3=r3+float((str(result3[139]).split())[0].split(">")[1])
            except:
                r3=r3
            rainfall3.append(r3)
            Time3.append('{0}-{1}-{2} 08:00'.format(Yy3,Mm3,Dd3))
            HQ093.append((str(result3[156]).split())[0].split(">")[1])  #09
            try:
                r3=r3+float((str(result3[156]).split())[0].split(">")[1])
            except:
                r3=r3
            rainfall3.append(r3)
            Time3.append('{0}-{1}-{2} 09:00'.format(Yy3,Mm3,Dd3))
            HQ103.append((str(result3[173]).split())[0].split(">")[1])  #10
            try:
                r3=r3+float((str(result3[173]).split())[0].split(">")[1])
            except:
                r3=r3
            rainfall3.append(r3)
            Time3.append('{0}-{1}-{2} 10:00'.format(Yy3,Mm3,Dd3))
            HQ113.append((str(result3[190]).split())[0].split(">")[1])  #11
            try:
                r3=r3+float((str(result3[190]).split())[0].split(">")[1])
            except:
                r3=r3
            rainfall3.append(r3)
            Time3.append('{0}-{1}-{2} 11:00'.format(Yy3,Mm3,Dd3))
            HQ123.append((str(result3[207]).split())[0].split(">")[1])  #12
            try:
                r3=r3+float((str(result3[207]).split())[0].split(">")[1])
            except:
                r3=r3
            rainfall3.append(r3)
            Time3.append('{0}-{1}-{2} 12:00'.format(Yy3,Mm3,Dd3))
            HQ133.append((str(result3[224]).split())[0].split(">")[1])  #13
            try:
                r3=r3+float((str(result3[224]).split())[0].split(">")[1])
            except:
                r3=r3
            rainfall3.append(r3)
            Time3.append('{0}-{1}-{2} 13:00'.format(Yy3,Mm3,Dd3))
            HQ143.append((str(result3[241]).split())[0].split(">")[1])  #14
            try:
                r3=r3+float((str(result3[241]).split())[0].split(">")[1])
            except:
                r3=r3
            rainfall3.append(r3)
            Time3.append('{0}-{1}-{2} 14:00'.format(Yy3,Mm3,Dd3))
            HQ153.append((str(result3[258]).split())[0].split(">")[1])  #15
            try:
                r3=r3+float((str(result3[258]).split())[0].split(">")[1])
            except:
                r3=r3
            rainfall3.append(r3)
            Time3.append('{0}-{1}-{2} 15:00'.format(Yy3,Mm3,Dd3))
            HQ163.append((str(result3[275]).split())[0].split(">")[1])  #16
            try:
                r3=r3+float((str(result3[275]).split())[0].split(">")[1])
            except:
                r3=r3
            rainfall3.append(r3)
            Time3.append('{0}-{1}-{2} 16:00'.format(Yy3,Mm3,Dd3))
            HQ173.append((str(result3[292]).split())[0].split(">")[1])  #17
            try:
                r3=r3+float((str(result3[292]).split())[0].split(">")[1])
            except:
                r3=r3
            rainfall3.append(r3)
            Time3.append('{0}-{1}-{2} 17:00'.format(Yy3,Mm3,Dd3)) 
            HQ183.append((str(result3[309]).split())[0].split(">")[1])  #18
            try:
                r3=r3+float((str(result3[309]).split())[0].split(">")[1])
            except:
                r3=r3
            rainfall3.append(r3)
            Time3.append('{0}-{1}-{2} 18:00'.format(Yy3,Mm3,Dd3))
            HQ193.append((str(result3[326]).split())[0].split(">")[1])  #19
            try:
                r3=r3+float((str(result3[326]).split())[0].split(">")[1])
            except:
                r3=r3
            rainfall3.append(r3)
            Time3.append('{0}-{1}-{2} 19:00'.format(Yy3,Mm3,Dd3))
            HQ203.append((str(result3[343]).split())[0].split(">")[1])  #20
            try:
                r3=r3+float((str(result3[343]).split())[0].split(">")[1])
            except:
                r3=r3
            rainfall3.append(r3)
            Time3.append('{0}-{1}-{2} 20:00'.format(Yy3,Mm3,Dd3))
            HQ213.append((str(result3[360]).split())[0].split(">")[1])  #21
            try:
                r3=r3+float((str(result3[360]).split())[0].split(">")[1])
            except:
                r3=r3
            rainfall3.append(r3)
            Time3.append('{0}-{1}-{2} 21:00'.format(Yy3,Mm3,Dd3))
            HQ223.append((str(result3[377]).split())[0].split(">")[1])  #22
            try:
                r3=r3+float((str(result3[377]).split())[0].split(">")[1])
            except:
                r3=r3
            rainfall3.append(r3)
            Time3.append('{0}-{1}-{2} 22:00'.format(Yy3,Mm3,Dd3))
            HQ233.append((str(result3[394]).split())[0].split(">")[1])  #23
            try:
                r3=r3+float((str(result3[394]).split())[0].split(">")[1])
            except:
                r3=r3
            rainfall3.append(r3)
            Time3.append('{0}-{1}-{2} 23:00'.format(Yy3,Mm3,Dd3))
            HQ243.append((str(result3[411]).split())[0].split(">")[1])  #24
            try:
                r3=r3+float((str(result3[411]).split())[0].split(">")[1])
            except:
                r3=r3
            rainfall3.append(r3)
            Time3.append('{0}-{1}-{2} 24:00'.format(Yy3,Mm3,Dd3))

            d3 = {
                "st_no":st_no3,
                "yy":yy3,
                "mm":mm3,
                "dd":dd3,
                "HQ01":HQ013,
                "HQ02":HQ023,
                "HQ03":HQ033,
                "HQ04":HQ043,
                "HQ05":HQ053,
                "HQ06":HQ063,
                "HQ07":HQ073,
                "HQ08":HQ083,
                "HQ09":HQ093,
                "HQ10":HQ103,
                "HQ11":HQ113,
                "HQ12":HQ123,
                "HQ13":HQ133,
                "HQ14":HQ143,
                "HQ15":HQ153,
                "HQ16":HQ163,
                "HQ17":HQ173,
                "HQ18":HQ183,
                "HQ19":HQ193,
                "HQ20":HQ203,
                "HQ21":HQ213,
                "HQ22":HQ223,
                "HQ23":HQ233,
                "HQ24":HQ243,
                }
    
            time.sleep(random.uniform(0,0.1))

        START3=("{0} {1}:00".format(s_d3,s_t3))
        END3=("{0} {1}:00".format(e_d3,e_t3))
        for i in range(len(Time3)):
            if START3 == Time3[i]:
                SC3=i    
            if END3 == Time3[i]:
                EC3=i+1 

        del Time3[EC3:]
        del rainfall3[EC3:]
        del Time3[0:SC3]
        del rainfall3[0:SC3]
    
        for i in range(len(Time3)):
            TH3.append(i+1)

        T3=TH3
        RF3=rainfall3

        df3_test=(pd.DataFrame(data = d3))

        print("3-OKKK")
        button_start.configure(bg="Maroon")
        button_plus3.configure(bg="DarkGoldenrod")
    except:
        print("3-NO")
        button_start.configure(bg="Maroon")
        pass

    ################################
    try:
        M4=[]
        D4=[]
        st_no4=[]

        yy4=[]
        mm4=[]
        dd4=[]

        HQ014=[]
        HQ024=[]
        HQ034=[]
        HQ044=[]
        HQ054=[]
        HQ064=[]
        HQ074=[]
        HQ084=[]
        HQ094=[]
        HQ104=[]
        HQ114=[]
        HQ124=[]
        HQ134=[]
        HQ144=[]
        HQ154=[]
        HQ164=[]
        HQ174=[]
        HQ184=[]
        HQ194=[]
        HQ204=[]
        HQ214=[]
        HQ224=[]
        HQ234=[]
        HQ244=[]
    
        rainfall4=[]
        Time4=[]
        TH4=[]
        r4=0
   
        if int(M24)-int(M14)>1:
            for i in range(31-int(D14)+1):
                M4.append(int(M14))
            for i in range(int(D14),32):
                D4.append(i)
            for i in range(int(M14)+1,int(M24)):
                for j in range(1,32):
                    M4.append(i)
            for i in range(int(M14),int(M24)-1):
                for j in range(1,32):
                    D4.append(j)
            for i in range(int(D24)):
                M4.append(int(M24))
            for i in range(1,int(D24)+1):
                D4.append(i)                
        elif int(M24)-int(M14)==1:
            for i in range(31-int(D14)+1):
                M4.append(int(M14))
            for i in range(int(D14),32):
                D4.append(i)
            for i in range(int(D24)):
                M4.append(int(M24))
            for i in range(1,int(D24)+1):
                D4.append(i)
        else:
            for i in range(int(D24)-int(D14)+1):
                M4.append(int(M14))
            for i in range(int(D14),int(D24)+1):
                D4.append(i)

        OUT4=[]
        SAVE_M4=[]
        SAVE_D4=[]
        for i in range(len(M4)):
        # print(M[i],D[i])
            if (M4[i]==2 and D4[i]>28) or (M4[i]==4 and D4[i]>30) or (M4[i]==6 and D4[i]>30) or (M4[i]==9 and D4[i]>30) or (M4[i]==11 and D4[i]>30):
                OUT4.append(i)
            
        for i in range(len(M4)):
            if i not in OUT4:
                SAVE_M4.append(M4[i])
                SAVE_D4.append(D4[i])  
        M4=SAVE_M4
        D4=SAVE_D4       

        for i in range(len(M4)):
            Yy4=Y14
            if M4[i]<10:
                Mm4='0{}'.format(M4[i])
            else:
                Mm4=str(M4[i])
    
            if D4[i]<10:
                Dd4='0{}'.format(D4[i])
            else:
                Dd4=str(D4[i])
            
            url4 = r'https://e-service.cwb.gov.tw/HistoryDataQuery/DayDataController.do?command=viewMain&station={0}&stname=%25E4%25B8%258A%25E5%25BE%25B7%25E6%2596%2587&datepicker={1}-{2}-{3}#'.format(ID4,Yy4,Mm4,Dd4)
        
            re4 = requests.get(url4) 
            soup4 = BeautifulSoup(re4.text, "html.parser")
            result4 = soup4.find_all("td")
            RR4 = soup4.find_all("head")
            t4 = str(RR4).split(";")
            x4 = t4[4].split("\"")
            y4=x4[1].split("-")
            st_no4.append(y4[0])
            dd4.append(y4[3]) 
            mm4.append(y4[2])
            yy4.append(y4[1])
    
            HQ014.append((str(result4[20]).split())[0].split(">")[1])  #01
            try:
                r4=r4+float((str(result4[20]).split())[0].split(">")[1])
            except:
                r4=r4
            rainfall4.append(r4)
            Time4.append('{0}-{1}-{2} 01:00'.format(Yy4,Mm4,Dd4)) 
            HQ024.append((str(result4[37]).split())[0].split(">")[1])  #02
            try:
                r4=r4+float((str(result4[37]).split())[0].split(">")[1])
            except:
                r4=r4
            rainfall4.append(r4)
            Time4.append('{0}-{1}-{2} 02:00'.format(Yy4,Mm4,Dd4))
            HQ034.append((str(result4[54]).split())[0].split(">")[1])  #03
            try:
                r4=r4+float((str(result4[54]).split())[0].split(">")[1])
            except:
                r4=r4
            rainfall4.append(r4)
            Time4.append('{0}-{1}-{2} 03:00'.format(Yy4,Mm4,Dd4))
            HQ044.append((str(result4[71]).split())[0].split(">")[1])  #04
            try:
                r4=r4+float((str(result4[71]).split())[0].split(">")[1])
            except:
                r4=r4
            rainfall4.append(r4)
            Time4.append('{0}-{1}-{2} 04:00'.format(Yy4,Mm4,Dd4))
            HQ054.append((str(result4[88]).split())[0].split(">")[1])  #05 
            try:
                r4=r4+float((str(result4[88]).split())[0].split(">")[1])
            except:
                r4=r4
            rainfall4.append(r4)
            Time4.append('{0}-{1}-{2} 05:00'.format(Yy4,Mm4,Dd4))
            HQ064.append((str(result4[105]).split())[0].split(">")[1])  #06
            try:
                r4=r4+float((str(result4[105]).split())[0].split(">")[1])
            except:
                r4=r4
            rainfall4.append(r4)
            Time4.append('{0}-{1}-{2} 06:00'.format(Yy4,Mm4,Dd4))
            HQ074.append((str(result4[122]).split())[0].split(">")[1])  #07 
            try:
                r4=r4+float((str(result4[122]).split())[0].split(">")[1])
            except:
                r4=r4
            rainfall4.append(r4)
            Time4.append('{0}-{1}-{2} 07:00'.format(Yy4,Mm4,Dd4))
            HQ084.append((str(result4[139]).split())[0].split(">")[1])  #08
            try:
                r4=r4+float((str(result4[139]).split())[0].split(">")[1])
            except:
                r4=r4
            rainfall4.append(r4)
            Time4.append('{0}-{1}-{2} 08:00'.format(Yy4,Mm4,Dd4))
            HQ094.append((str(result4[156]).split())[0].split(">")[1])  #09
            try:
                r4=r4+float((str(result4[156]).split())[0].split(">")[1])
            except:
                r4=r4
            rainfall4.append(r4)
            Time4.append('{0}-{1}-{2} 09:00'.format(Yy4,Mm4,Dd4))
            HQ104.append((str(result4[173]).split())[0].split(">")[1])  #10
            try:
                r4=r4+float((str(result4[173]).split())[0].split(">")[1])
            except:
                r4=r4
            rainfall4.append(r4)
            Time4.append('{0}-{1}-{2} 10:00'.format(Yy4,Mm4,Dd4))
            HQ114.append((str(result4[190]).split())[0].split(">")[1])  #11
            try:
                r4=r4+float((str(result4[190]).split())[0].split(">")[1])
            except:
                r4=r4
            rainfall4.append(r4)
            Time4.append('{0}-{1}-{2} 11:00'.format(Yy4,Mm4,Dd4))
            HQ124.append((str(result4[207]).split())[0].split(">")[1])  #12
            try:
                r4=r4+float((str(result4[207]).split())[0].split(">")[1])
            except:
                r4=r4
            rainfall4.append(r4)
            Time4.append('{0}-{1}-{2} 12:00'.format(Yy4,Mm4,Dd4))
            HQ134.append((str(result4[224]).split())[0].split(">")[1])  #13
            try:
                r4=r4+float((str(result4[224]).split())[0].split(">")[1])
            except:
                r4=r4
            rainfall4.append(r4)
            Time4.append('{0}-{1}-{2} 13:00'.format(Yy4,Mm4,Dd4))
            HQ144.append((str(result4[241]).split())[0].split(">")[1])  #14
            try:
                r4=r4+float((str(result4[241]).split())[0].split(">")[1])  
            except:
                r4=r4
            rainfall4.append(r4)
            Time4.append('{0}-{1}-{2} 14:00'.format(Yy4,Mm4,Dd4))
            HQ154.append((str(result4[258]).split())[0].split(">")[1])  #15
            try:
                r4=r4+float((str(result4[258]).split())[0].split(">")[1])
            except:
                r4=r4
            rainfall4.append(r4)
            Time4.append('{0}-{1}-{2} 15:00'.format(Yy4,Mm4,Dd4))
            HQ164.append((str(result4[275]).split())[0].split(">")[1])  #16
            try:
                r4=r4+float((str(result4[275]).split())[0].split(">")[1])
            except:
                r4=r4
            rainfall4.append(r4)
            Time4.append('{0}-{1}-{2} 16:00'.format(Yy4,Mm4,Dd4))
            HQ174.append((str(result4[292]).split())[0].split(">")[1])  #17
            try:
                r4=r4+float((str(result4[292]).split())[0].split(">")[1])
            except:
                r4=r4
            rainfall4.append(r4)
            Time4.append('{0}-{1}-{2} 17:00'.format(Yy4,Mm4,Dd4)) 
            HQ184.append((str(result4[309]).split())[0].split(">")[1])  #18
            try:
                r4=r4+float((str(result4[309]).split())[0].split(">")[1])
            except:
                r4=r4
            rainfall4.append(r4)
            Time4.append('{0}-{1}-{2} 18:00'.format(Yy4,Mm4,Dd4))
            HQ194.append((str(result4[326]).split())[0].split(">")[1])  #19
            try:
                r4=r4+float((str(result4[326]).split())[0].split(">")[1])
            except:
                r4=r4
            rainfall4.append(r4)
            Time4.append('{0}-{1}-{2} 19:00'.format(Yy4,Mm4,Dd4))
            HQ204.append((str(result4[343]).split())[0].split(">")[1])  #20
            try:
                r4=r4+float((str(result4[343]).split())[0].split(">")[1])
            except:
                r4=r4
            rainfall4.append(r4)
            Time4.append('{0}-{1}-{2} 20:00'.format(Yy4,Mm4,Dd4))
            HQ214.append((str(result4[360]).split())[0].split(">")[1])  #21
            try:
                r4=r4+float((str(result4[360]).split())[0].split(">")[1])
            except:
                r4=r4
            rainfall4.append(r4)
            Time4.append('{0}-{1}-{2} 21:00'.format(Yy4,Mm4,Dd4))
            HQ224.append((str(result4[377]).split())[0].split(">")[1])  #22
            try:
                r4=r4+float((str(result4[377]).split())[0].split(">")[1])
            except:
                r4=r4
            rainfall4.append(r4)
            Time4.append('{0}-{1}-{2} 22:00'.format(Yy4,Mm4,Dd4))
            HQ234.append((str(result4[394]).split())[0].split(">")[1])  #23
            try:
                r4=r4+float((str(result4[394]).split())[0].split(">")[1])
            except:
                r4=r4
            rainfall4.append(r4)
            Time4.append('{0}-{1}-{2} 23:00'.format(Yy4,Mm4,Dd4))
            HQ244.append((str(result4[411]).split())[0].split(">")[1])  #24
            try:
                r4=r4+float((str(result4[411]).split())[0].split(">")[1])
            except:
                r4=r4
            rainfall4.append(r4)
            Time4.append('{0}-{1}-{2} 24:00'.format(Yy4,Mm4,Dd4))

            d4 = {
                "st_no":st_no4,   #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                "yy":yy4,
                "mm":mm4,
                "dd":dd4,
                "HQ01":HQ014,
                "HQ02":HQ024,
                "HQ03":HQ034,
                "HQ04":HQ044,
                "HQ05":HQ054,
                "HQ06":HQ064,
                "HQ07":HQ074,
                "HQ08":HQ084,
                "HQ09":HQ094,
                "HQ10":HQ104,
                "HQ11":HQ114,
                "HQ12":HQ124,
                "HQ13":HQ134,
                "HQ14":HQ144,
                "HQ15":HQ154,
                "HQ16":HQ164,
                "HQ17":HQ174,
                "HQ18":HQ184,
                "HQ19":HQ194,
                "HQ20":HQ204,
                "HQ21":HQ214,
                "HQ22":HQ224,
                "HQ23":HQ234,
                "HQ24":HQ244,
                }
    
            time.sleep(random.uniform(0,0.1))

        START4=("{0} {1}:00".format(s_d4,s_t4))
        END4=("{0} {1}:00".format(e_d4,e_t4))
        for i in range(len(Time4)):
            if START4 == Time4[i]:
                SC4=i    
            if END4 == Time4[i]:
                EC4=i+1 

        del Time4[EC4:]
        del rainfall4[EC4:]
        del Time4[0:SC4]
        del rainfall4[0:SC4]
    
        for i in range(len(Time4)):
            TH4.append(i+1)

        T4=TH4
        RF4=rainfall4

        df4_test=(pd.DataFrame(data = d4))

        print("4-OKKK")
        button_start.configure(bg="Maroon")
        button_plus4.configure(bg="DarkGoldenrod")
    except:
        print("4-NO")
        button_start.configure(bg="Maroon")
        pass
    #################################################
    try:
        M5=[]
        D5=[]
        st_no5=[]

        yy5=[]
        mm5=[]
        dd5=[]

        HQ015=[]
        HQ025=[]
        HQ035=[]
        HQ045=[]
        HQ055=[]
        HQ065=[]
        HQ075=[]
        HQ085=[]
        HQ095=[]
        HQ105=[]
        HQ115=[]
        HQ125=[]
        HQ135=[] ##
        HQ145=[]
        HQ155=[]
        HQ165=[]
        HQ175=[]
        HQ185=[]
        HQ195=[]
        HQ205=[]
        HQ215=[]
        HQ225=[]
        HQ235=[]
        HQ245=[]
    
        rainfall5=[]
        Time5=[]
        TH5=[]
        r5=0
   
        if int(M25)-int(M15)>1:
            for i in range(31-int(D15)+1):
                M5.append(int(M15))
            for i in range(int(D15),32):
                D5.append(i)
            for i in range(int(M15)+1,int(M25)):
                for j in range(1,32):
                    M5.append(i)
            for i in range(int(M15),int(M25)-1):
                for j in range(1,32):
                    D5.append(j)
            for i in range(int(D25)):
                M5.append(int(M25))
            for i in range(1,int(D25)+1):
                D5.append(i)                
        elif int(M25)-int(M15)==1:
            for i in range(31-int(D15)+1):
                M5.append(int(M15))
            for i in range(int(D15),32):
                D5.append(i)
            for i in range(int(D25)):
                M5.append(int(M25))
            for i in range(1,int(D25)+1):
                D5.append(i)
        else:
            for i in range(int(D25)-int(D15)+1):
                M5.append(int(M15))
            for i in range(int(D15),int(D25)+1):
                D5.append(i)

        OUT5=[]
        SAVE_M5=[]
        SAVE_D5=[]
        for i in range(len(M5)):
        # print(M[i],D[i])
            if (M5[i]==2 and D5[i]>28) or (M5[i]==4 and D5[i]>30) or (M5[i]==6 and D5[i]>30) or (M5[i]==9 and D5[i]>30) or (M5[i]==11 and D5[i]>30):
                OUT5.append(i)
            
        for i in range(len(M5)):
            if i not in OUT5:
                SAVE_M5.append(M5[i])
                SAVE_D5.append(D5[i])  
        M5=SAVE_M5
        D5=SAVE_D5       

        for i in range(len(M5)):
            Yy5=Y15
            if M5[i]<10:
                Mm5='0{}'.format(M5[i])
            else:
                Mm5=str(M5[i])
    
            if D5[i]<10:
                Dd5='0{}'.format(D5[i])
            else:
                Dd5=str(D5[i])
            
            url5 = r'https://e-service.cwb.gov.tw/HistoryDataQuery/DayDataController.do?command=viewMain&station={0}&stname=%25E4%25B8%258A%25E5%25BE%25B7%25E6%2596%2587&datepicker={1}-{2}-{3}#'.format(ID5,Yy5,Mm5,Dd5)
        
            re5 = requests.get(url5) 
            soup5 = BeautifulSoup(re5.text, "html.parser")
            result5 = soup5.find_all("td")
            RR5 = soup5.find_all("head")
            t5 = str(RR5).split(";")
            x5 = t5[4].split("\"")
            y5=x5[1].split("-")
            st_no5.append(y5[0])
            dd5.append(y5[3]) 
            mm5.append(y5[2])
            yy5.append(y5[1])
    
            HQ015.append((str(result5[20]).split())[0].split(">")[1])  #01
            try:
                r5=r5+float((str(result5[20]).split())[0].split(">")[1])
            except:
                r5=r5
            rainfall5.append(r5)
            Time5.append('{0}-{1}-{2} 01:00'.format(Yy5,Mm5,Dd5)) 
            HQ025.append((str(result5[37]).split())[0].split(">")[1])  #02
            try:
                r5=r5+float((str(result5[37]).split())[0].split(">")[1])
            except:
                r5=r5
            rainfall5.append(r5)
            Time5.append('{0}-{1}-{2} 02:00'.format(Yy5,Mm5,Dd5)) 
            HQ035.append((str(result5[54]).split())[0].split(">")[1])  #03
            try:
                r5=r5+float((str(result5[54]).split())[0].split(">")[1])
            except:
                r5=r5
            rainfall5.append(r5)
            Time5.append('{0}-{1}-{2} 03:00'.format(Yy5,Mm5,Dd5))
            HQ045.append((str(result5[71]).split())[0].split(">")[1])  #04
            try:
                r5=r5+float((str(result5[71]).split())[0].split(">")[1])
            except:
                r5=r5
            rainfall5.append(r5)
            Time5.append('{0}-{1}-{2} 04:00'.format(Yy5,Mm5,Dd5))
            HQ055.append((str(result5[88]).split())[0].split(">")[1])  #05 
            try:
                r5=r5+float((str(result5[88]).split())[0].split(">")[1])
            except:
                r5=r5
            rainfall5.append(r5)
            Time5.append('{0}-{1}-{2} 05:00'.format(Yy5,Mm5,Dd5))
            HQ065.append((str(result5[105]).split())[0].split(">")[1])  #06
            try:
                r5=r5+float((str(result5[105]).split())[0].split(">")[1])
            except:
                r5=r5
            rainfall5.append(r5)
            Time5.append('{0}-{1}-{2} 06:00'.format(Yy5,Mm5,Dd5))
            HQ075.append((str(result5[122]).split())[0].split(">")[1])  #07 
            try:
                r5=r5+float((str(result5[122]).split())[0].split(">")[1])
            except:
                r5=r5
            rainfall5.append(r5)
            Time5.append('{0}-{1}-{2} 07:00'.format(Yy5,Mm5,Dd5))
            HQ085.append((str(result5[139]).split())[0].split(">")[1])  #08
            try:
                r5=r5+float((str(result5[139]).split())[0].split(">")[1])
            except:
                r5=r5
            rainfall5.append(r5)
            Time5.append('{0}-{1}-{2} 08:00'.format(Yy5,Mm5,Dd5))
            HQ095.append((str(result5[156]).split())[0].split(">")[1])  #09
            try:
                r5=r5+float((str(result5[156]).split())[0].split(">")[1])
            except:
                r5=r5
            rainfall5.append(r5)
            Time5.append('{0}-{1}-{2} 09:00'.format(Yy5,Mm5,Dd5))
            HQ105.append((str(result5[173]).split())[0].split(">")[1])  #10
            try:
                r5=r5+float((str(result5[173]).split())[0].split(">")[1])
            except:
                r5=r5
            rainfall5.append(r5)
            Time5.append('{0}-{1}-{2} 10:00'.format(Yy5,Mm5,Dd5))
            HQ115.append((str(result5[190]).split())[0].split(">")[1])  #11
            try:
                r5=r5+float((str(result5[190]).split())[0].split(">")[1])
            except:
                r5=r5
            rainfall5.append(r5)
            Time5.append('{0}-{1}-{2} 11:00'.format(Yy5,Mm5,Dd5))
            HQ125.append((str(result5[207]).split())[0].split(">")[1])  #12
            try:
                r5=r5+float((str(result5[207]).split())[0].split(">")[1])
            except:
                r5=r5
            rainfall5.append(r5)
            Time5.append('{0}-{1}-{2} 12:00'.format(Yy5,Mm5,Dd5))
            HQ135.append((str(result5[224]).split())[0].split(">")[1])  #13
            try:
                r5=r5+float((str(result5[224]).split())[0].split(">")[1])
            except:
                r5=r5
            rainfall5.append(r5)
            Time5.append('{0}-{1}-{2} 13:00'.format(Yy5,Mm5,Dd5))
            HQ145.append((str(result5[241]).split())[0].split(">")[1])  #14
            try:
                r5=r5+float((str(result5[241]).split())[0].split(">")[1])  
            except:
                r5=r5
            rainfall5.append(r5)
            Time5.append('{0}-{1}-{2} 14:00'.format(Yy5,Mm5,Dd5))
            HQ155.append((str(result5[258]).split())[0].split(">")[1])  #15
            try:
                r5=r5+float((str(result5[258]).split())[0].split(">")[1])
            except:
                r5=r5
            rainfall5.append(r5)
            Time5.append('{0}-{1}-{2} 15:00'.format(Yy5,Mm5,Dd5))
            HQ165.append((str(result5[275]).split())[0].split(">")[1])  #16
            try:
                r5=r5+float((str(result5[275]).split())[0].split(">")[1])
            except:
                r5=r5
            rainfall5.append(r5)
            Time5.append('{0}-{1}-{2} 16:00'.format(Yy5,Mm5,Dd5))
            HQ175.append((str(result5[292]).split())[0].split(">")[1])  #17
            try:
                r5=r5+float((str(result5[292]).split())[0].split(">")[1])
            except:
                r5=r5
            rainfall5.append(r5)
            Time5.append('{0}-{1}-{2} 17:00'.format(Yy5,Mm5,Dd5)) 
            HQ185.append((str(result5[309]).split())[0].split(">")[1])  #18
            try:
                r5=r5+float((str(result5[309]).split())[0].split(">")[1])
            except:
                r5=r5
            rainfall5.append(r5)
            Time5.append('{0}-{1}-{2} 18:00'.format(Yy5,Mm5,Dd5))
            HQ195.append((str(result5[326]).split())[0].split(">")[1])  #19
            try:
                r5=r5+float((str(result5[326]).split())[0].split(">")[1])
            except:
                r5=r5
            rainfall5.append(r5)
            Time5.append('{0}-{1}-{2} 19:00'.format(Yy5,Mm5,Dd5))
            HQ205.append((str(result5[343]).split())[0].split(">")[1])  #20
            try:
                r5=r5+float((str(result5[343]).split())[0].split(">")[1])
            except:
                r5=r5
            rainfall5.append(r5)
            Time5.append('{0}-{1}-{2} 20:00'.format(Yy5,Mm5,Dd5))
            HQ215.append((str(result5[360]).split())[0].split(">")[1])  #21
            try:
                r5=r5+float((str(result5[360]).split())[0].split(">")[1])
            except:
                r5=r5
            rainfall5.append(r5)
            Time5.append('{0}-{1}-{2} 21:00'.format(Yy5,Mm5,Dd5))
            HQ225.append((str(result5[377]).split())[0].split(">")[1])  #22
            try:
                r5=r5+float((str(result5[377]).split())[0].split(">")[1])
            except:
                r5=r5
            rainfall5.append(r5)
            Time5.append('{0}-{1}-{2} 22:00'.format(Yy5,Mm5,Dd5))
            HQ235.append((str(result5[394]).split())[0].split(">")[1])  #23
            try:
                r5=r5+float((str(result5[394]).split())[0].split(">")[1])
            except:
                r5=r5
            rainfall5.append(r5)
            Time5.append('{0}-{1}-{2} 23:00'.format(Yy5,Mm5,Dd5))
            HQ245.append((str(result5[411]).split())[0].split(">")[1])  #24
            try:
                r5=r5+float((str(result5[411]).split())[0].split(">")[1])
            except:
                r5=r5
            rainfall5.append(r5)
            Time5.append('{0}-{1}-{2} 24:00'.format(Yy5,Mm5,Dd5))

            d5 = {
                "st_no":st_no5,   
                "yy":yy5,
                "mm":mm5,
                "dd":dd5,
                "HQ01":HQ015,
                "HQ02":HQ025,
                "HQ03":HQ035,
                "HQ04":HQ045,
                "HQ05":HQ055,
                "HQ06":HQ065,
                "HQ07":HQ075,
                "HQ08":HQ085,
                "HQ09":HQ095,
                "HQ10":HQ105,
                "HQ11":HQ115, ##
                "HQ12":HQ125,
                "HQ13":HQ135,
                "HQ14":HQ145,
                "HQ15":HQ155,
                "HQ16":HQ165,
                "HQ17":HQ175,
                "HQ18":HQ185,
                "HQ19":HQ195,
                "HQ20":HQ205,
                "HQ21":HQ215,
                "HQ22":HQ225,
                "HQ23":HQ235,
                "HQ24":HQ245,
                }
    
            time.sleep(random.uniform(0,0.1))

        START5=("{0} {1}:00".format(s_d5,s_t5))
        END5=("{0} {1}:00".format(e_d5,e_t5))
        for i in range(len(Time5)):
            if START5 == Time5[i]:
                SC5=i    
            if END5 == Time5[i]:
                EC5=i+1 

        del Time5[EC5:]
        del rainfall5[EC5:]
        del Time5[0:SC5]
        del rainfall5[0:SC5]
    
        for i in range(len(Time5)):
            TH5.append(i+1)

        T5=TH5
        RF5=rainfall5

        df5_test=(pd.DataFrame(data = d5))

        print("5-OKKK")
        button_start.configure(bg="Maroon")
        button_plus5.configure(bg="DarkGoldenrod")
    except:
        print("5-NO")
        button_start.configure(bg="Maroon")
        pass
    #################################################
    try:
        M6=[]
        D6=[]
        st_no6=[]

        yy6=[]
        mm6=[]
        dd6=[]

        HQ016=[]
        HQ026=[]
        HQ036=[]
        HQ046=[]
        HQ056=[]
        HQ066=[]
        HQ076=[]
        HQ086=[]
        HQ096=[]
        HQ106=[]
        HQ116=[]
        HQ126=[]
        HQ136=[] ##
        HQ146=[]
        HQ156=[]
        HQ166=[]
        HQ176=[]
        HQ186=[]
        HQ196=[]
        HQ206=[]
        HQ216=[]
        HQ226=[]
        HQ236=[]
        HQ246=[]
    
        rainfall6=[]
        Time6=[]
        TH6=[]
        r6=0
   
        if int(M26)-int(M16)>1:
            for i in range(31-int(D16)+1):
                M6.append(int(M16))
            for i in range(int(D16),32):
                D6.append(i)
            for i in range(int(M16)+1,int(M26)):
                for j in range(1,32):
                    M6.append(i)
            for i in range(int(M16),int(M26)-1):
                for j in range(1,32):
                    D6.append(j)
            for i in range(int(D26)):
                M6.append(int(M26))
            for i in range(1,int(D26)+1):
                D6.append(i)                
        elif int(M26)-int(M16)==1:
            for i in range(31-int(D16)+1):
                M6.append(int(M16))
            for i in range(int(D16),32):
                D6.append(i)
            for i in range(int(D26)):
                M6.append(int(M26))
            for i in range(1,int(D26)+1):
                D6.append(i)
        else:
            for i in range(int(D26)-int(D16)+1):
                M6.append(int(M16))
            for i in range(int(D16),int(D26)+1):
                D6.append(i)

        OUT6=[]
        SAVE_M6=[]
        SAVE_D6=[]
        for i in range(len(M6)):
        # print(M[i],D[i])
            if (M6[i]==2 and D6[i]>28) or (M6[i]==4 and D6[i]>30) or (M6[i]==6 and D6[i]>30) or (M6[i]==9 and D6[i]>30) or (M6[i]==11 and D6[i]>30):
                OUT6.append(i)
            
        for i in range(len(M6)):
            if i not in OUT6:
                SAVE_M6.append(M6[i])
                SAVE_D6.append(D6[i])  
        M6=SAVE_M6
        D6=SAVE_D6       

        for i in range(len(M6)):
            Yy6=Y16
            if M6[i]<10:
                Mm6='0{}'.format(M6[i])
            else:
                Mm6=str(M6[i])
    
            if D6[i]<10:
                Dd6='0{}'.format(D6[i])
            else:
                Dd6=str(D6[i])
            
            url6 = r'https://e-service.cwb.gov.tw/HistoryDataQuery/DayDataController.do?command=viewMain&station={0}&stname=%25E4%25B8%258A%25E5%25BE%25B7%25E6%2596%2587&datepicker={1}-{2}-{3}#'.format(ID6,Yy6,Mm6,Dd6)
        
            re6 = requests.get(url6) 
            soup6 = BeautifulSoup(re6.text, "html.parser")
            result6 = soup6.find_all("td")
            RR6 = soup6.find_all("head")
            t6 = str(RR6).split(";")
            x6 = t6[4].split("\"")   
            y6 = x6[1].split("-")
            st_no6.append(y6[0])
            dd6.append(y6[3]) 
            mm6.append(y6[2])
            yy6.append(y6[1])
    
            HQ016.append((str(result6[20]).split())[0].split(">")[1])  #01
            try:
                r6=r6+float((str(result6[20]).split())[0].split(">")[1])
            except:
                r6=r6
            rainfall6.append(r6)
            Time6.append('{0}-{1}-{2} 01:00'.format(Yy6,Mm6,Dd6)) 
            HQ026.append((str(result6[37]).split())[0].split(">")[1])  #02
            try:
                r6=r6+float((str(result6[37]).split())[0].split(">")[1])
            except:
                r6=r6
            rainfall6.append(r6)
            Time6.append('{0}-{1}-{2} 02:00'.format(Yy6,Mm6,Dd6)) 
            HQ036.append((str(result6[54]).split())[0].split(">")[1])  #03
            try:
                r6=r6+float((str(result6[54]).split())[0].split(">")[1])
            except:
                r6=r6
            rainfall6.append(r6)
            Time6.append('{0}-{1}-{2} 03:00'.format(Yy6,Mm6,Dd6))
            HQ046.append((str(result6[71]).split())[0].split(">")[1])  #04
            try:
                r6=r6+float((str(result6[71]).split())[0].split(">")[1])
            except:
                r6=r6
            rainfall6.append(r6)
            Time6.append('{0}-{1}-{2} 04:00'.format(Yy6,Mm6,Dd6))
            HQ056.append((str(result6[88]).split())[0].split(">")[1])  #05 
            try:
                r6=r6+float((str(result6[88]).split())[0].split(">")[1])
            except:
                r6=r6
            rainfall6.append(r6)
            Time6.append('{0}-{1}-{2} 05:00'.format(Yy6,Mm6,Dd6))
            HQ066.append((str(result6[105]).split())[0].split(">")[1])  #06
            try:
                r6=r6+float((str(result6[105]).split())[0].split(">")[1])
            except:
                r6=r6
            rainfall6.append(r6)
            Time6.append('{0}-{1}-{2} 06:00'.format(Yy6,Mm6,Dd6))
            HQ076.append((str(result6[122]).split())[0].split(">")[1])  #07 
            try:
                r6=r6+float((str(result6[122]).split())[0].split(">")[1])
            except:
                r6=r6
            rainfall6.append(r6)
            Time6.append('{0}-{1}-{2} 07:00'.format(Yy6,Mm6,Dd6))
            HQ086.append((str(result6[139]).split())[0].split(">")[1])  #08
            try:
                r6=r6+float((str(result6[139]).split())[0].split(">")[1])
            except:
                r6=r6
            rainfall6.append(r6)
            Time6.append('{0}-{1}-{2} 08:00'.format(Yy6,Mm6,Dd6))
            HQ096.append((str(result6[156]).split())[0].split(">")[1])  #09
            try:
                r6=r6+float((str(result6[156]).split())[0].split(">")[1])
            except:
                r6=r6
            rainfall6.append(r6)
            Time6.append('{0}-{1}-{2} 09:00'.format(Yy6,Mm6,Dd6))
            HQ106.append((str(result6[173]).split())[0].split(">")[1])  #10
            try:
                r6=r6+float((str(result6[173]).split())[0].split(">")[1])
            except:
                r6=r6
            rainfall6.append(r6)
            Time6.append('{0}-{1}-{2} 10:00'.format(Yy6,Mm6,Dd6))
            HQ116.append((str(result6[190]).split())[0].split(">")[1])  #11
            try:
                r6=r6+float((str(result6[190]).split())[0].split(">")[1])
            except:
                r6=r6
            rainfall6.append(r6)
            Time6.append('{0}-{1}-{2} 11:00'.format(Yy6,Mm6,Dd6))
            HQ126.append((str(result6[207]).split())[0].split(">")[1])  #12
            try:
                r6=r6+float((str(result6[207]).split())[0].split(">")[1])
            except:
                r6=r6
            rainfall6.append(r6)
            Time6.append('{0}-{1}-{2} 12:00'.format(Yy6,Mm6,Dd6))
            HQ136.append((str(result6[224]).split())[0].split(">")[1])  #13
            try:
                r6=r6+float((str(result6[224]).split())[0].split(">")[1])
            except:
                r6=r6
            rainfall6.append(r6)
            Time6.append('{0}-{1}-{2} 13:00'.format(Yy6,Mm6,Dd6))
            HQ146.append((str(result6[241]).split())[0].split(">")[1])  #14
            try:
                r6=r6+float((str(result6[241]).split())[0].split(">")[1])  
            except:
                r6=r6
            rainfall6.append(r6)
            Time6.append('{0}-{1}-{2} 14:00'.format(Yy6,Mm6,Dd6))
            HQ156.append((str(result6[258]).split())[0].split(">")[1])  #15
            try:
                r6=r6+float((str(result6[258]).split())[0].split(">")[1])
            except:
                r6=r6
            rainfall6.append(r6)
            Time6.append('{0}-{1}-{2} 15:00'.format(Yy6,Mm6,Dd6))
            HQ166.append((str(result6[275]).split())[0].split(">")[1])  #16
            try:
                r6=r6+float((str(result6[275]).split())[0].split(">")[1])
            except:
                r6=r6
            rainfall6.append(r6)
            Time6.append('{0}-{1}-{2} 16:00'.format(Yy6,Mm6,Dd6))
            HQ176.append((str(result6[292]).split())[0].split(">")[1])  #17
            try:
                r6=r6+float((str(result6[292]).split())[0].split(">")[1])
            except:
                r6=r6
            rainfall6.append(r6)
            Time6.append('{0}-{1}-{2} 17:00'.format(Yy6,Mm6,Dd6)) 
            HQ186.append((str(result6[309]).split())[0].split(">")[1])  #18
            try:
                r6=r6+float((str(result6[309]).split())[0].split(">")[1])
            except:
                r6=r6
            rainfall6.append(r6)
            Time6.append('{0}-{1}-{2} 18:00'.format(Yy6,Mm6,Dd6))
            HQ196.append((str(result6[326]).split())[0].split(">")[1])  #19
            try:
                r6=r6+float((str(result6[326]).split())[0].split(">")[1])
            except:
                r6=r6
            rainfall6.append(r6)
            Time6.append('{0}-{1}-{2} 19:00'.format(Yy6,Mm6,Dd6))
            HQ206.append((str(result6[343]).split())[0].split(">")[1])  #20
            try:
                r6=r6+float((str(result6[343]).split())[0].split(">")[1])
            except:
                r6=r6
            rainfall6.append(r6)
            Time6.append('{0}-{1}-{2} 20:00'.format(Yy6,Mm6,Dd6))
            HQ216.append((str(result6[360]).split())[0].split(">")[1])  #21
            try:
                r6=r6+float((str(result6[360]).split())[0].split(">")[1])
            except:
                r6=r6
            rainfall6.append(r6)
            Time6.append('{0}-{1}-{2} 21:00'.format(Yy6,Mm6,Dd6))
            HQ226.append((str(result6[377]).split())[0].split(">")[1])  #22
            try:
                r6=r6+float((str(result6[377]).split())[0].split(">")[1])
            except:
                r6=r6
            rainfall6.append(r6)
            Time6.append('{0}-{1}-{2} 22:00'.format(Yy6,Mm6,Dd6))
            HQ236.append((str(result6[394]).split())[0].split(">")[1])  #23
            try:
                r6=r6+float((str(result6[394]).split())[0].split(">")[1])
            except:
                r6=r6
            rainfall6.append(r6)
            Time6.append('{0}-{1}-{2} 23:00'.format(Yy6,Mm6,Dd6))
            HQ246.append((str(result6[411]).split())[0].split(">")[1])  #24
            try:
                r6=r6+float((str(result6[411]).split())[0].split(">")[1])
            except:
                r6=r6
            rainfall6.append(r6)
            Time6.append('{0}-{1}-{2} 24:00'.format(Yy6,Mm6,Dd6))

            d6 = {
                "st_no":st_no6,   
                "yy":yy6,
                "mm":mm6,
                "dd":dd6,
                "HQ01":HQ016,
                "HQ02":HQ026,
                "HQ03":HQ036,
                "HQ04":HQ046,
                "HQ05":HQ056,
                "HQ06":HQ066,
                "HQ07":HQ076,
                "HQ08":HQ086,
                "HQ09":HQ096,
                "HQ10":HQ106,
                "HQ11":HQ116, ##
                "HQ12":HQ126,
                "HQ13":HQ136,
                "HQ14":HQ146,
                "HQ15":HQ156,
                "HQ16":HQ166,
                "HQ17":HQ176,
                "HQ18":HQ186,
                "HQ19":HQ196,
                "HQ20":HQ206,
                "HQ21":HQ216,
                "HQ22":HQ226,
                "HQ23":HQ236,
                "HQ24":HQ246,
                }
    
            time.sleep(random.uniform(0,0.1))

        START6=("{0} {1}:00".format(s_d6,s_t6))
        END6=("{0} {1}:00".format(e_d6,e_t6))
        for i in range(len(Time6)):
            if START6 == Time6[i]:
                SC6=i    
            if END6 == Time6[i]:
                EC6=i+1 

        del Time6[EC6:]
        del rainfall6[EC6:]
        del Time6[0:SC6]
        del rainfall6[0:SC6]
    
        for i in range(len(Time6)):
            TH6.append(i+1)

        T6=TH6
        RF6=rainfall6

        df6_test=(pd.DataFrame(data = d6))

        print("6-OKKK")
        button_start.configure(bg="Maroon")
        button_plus6.configure(bg="DarkGoldenrod")
    except:
        print("6-NO")
        button_start.configure(bg="Maroon")
        pass
    #################################3
    try:
        M7=[]
        D7=[]
        st_no7=[]

        yy7=[]
        mm7=[]
        dd7=[]

        HQ017=[]
        HQ027=[]
        HQ037=[]
        HQ047=[]
        HQ057=[]
        HQ067=[]
        HQ077=[]
        HQ087=[]
        HQ097=[]
        HQ107=[]
        HQ117=[]
        HQ127=[]
        HQ137=[] ##
        HQ147=[]
        HQ157=[]
        HQ167=[]
        HQ177=[]
        HQ187=[]
        HQ197=[]
        HQ207=[]
        HQ217=[]
        HQ227=[]
        HQ237=[]
        HQ247=[]
    
        rainfall7=[]
        Time7=[]
        TH7=[]
        r7=0
   
        if int(M27)-int(M17)>1:
            for i in range(31-int(D17)+1):
                M7.append(int(M17))
            for i in range(int(D17),32):
                D7.append(i)
            for i in range(int(M17)+1,int(M27)):
                for j in range(1,32):
                    M7.append(i)
            for i in range(int(M17),int(M27)-1):
                for j in range(1,32):
                    D7.append(j)
            for i in range(int(D27)):
                M7.append(int(M27))
            for i in range(1,int(D27)+1):
                D7.append(i)                
        elif int(M27)-int(M17)==1:
            for i in range(31-int(D17)+1):
                M7.append(int(M17))
            for i in range(int(D17),32):
                D7.append(i)
            for i in range(int(D27)):
                M7.append(int(M27))
            for i in range(1,int(D27)+1):
                D7.append(i)
        else:
            for i in range(int(D27)-int(D17)+1):
                M7.append(int(M17))
            for i in range(int(D17),int(D27)+1):
                D7.append(i)

        OUT7=[]
        SAVE_M7=[]
        SAVE_D7=[]
        for i in range(len(M7)):
        # print(M[i],D[i])
            if (M7[i]==2 and D7[i]>28) or (M7[i]==4 and D7[i]>30) or (M7[i]==6 and D7[i]>30) or (M7[i]==9 and D7[i]>30) or (M7[i]==11 and D7[i]>30):
                OUT7.append(i)
            
        for i in range(len(M7)):
            if i not in OUT7:
                SAVE_M7.append(M7[i])
                SAVE_D7.append(D7[i])  
        M7=SAVE_M7
        D7=SAVE_D7       

        for i in range(len(M7)):
            Yy7=Y17
            if M7[i]<10:
                Mm7='0{}'.format(M7[i])
            else:
                Mm7=str(M7[i])
    
            if D7[i]<10:
                Dd7='0{}'.format(D7[i])
            else:
                Dd7=str(D7[i])
            
            url7 = r'https://e-service.cwb.gov.tw/HistoryDataQuery/DayDataController.do?command=viewMain&station={0}&stname=%25E4%25B8%258A%25E5%25BE%25B7%25E6%2596%2587&datepicker={1}-{2}-{3}#'.format(ID7,Yy7,Mm7,Dd7)
        
            re7 = requests.get(url7) 
            soup7 = BeautifulSoup(re7.text, "html.parser")
            result7 = soup7.find_all("td")
            RR7 = soup7.find_all("head")
            t7 = str(RR7).split(";")
            x7 = t7[4].split("\"")   
            y7 = x7[1].split("-")
            st_no7.append(y7[0])
            dd7.append(y7[3]) 
            mm7.append(y7[2])
            yy7.append(y7[1])
    
            HQ017.append((str(result7[20]).split())[0].split(">")[1])  #01
            try:
                r7=r7+float((str(result7[20]).split())[0].split(">")[1])
            except:
                r7=r7
            rainfall7.append(r7)
            Time7.append('{0}-{1}-{2} 01:00'.format(Yy7,Mm7,Dd7)) 
            HQ027.append((str(result7[37]).split())[0].split(">")[1])  #02
            try:
                r7=r7+float((str(result7[37]).split())[0].split(">")[1])
            except:
                r7=r7
            rainfall7.append(r7)
            Time7.append('{0}-{1}-{2} 02:00'.format(Yy7,Mm7,Dd7)) 
            HQ037.append((str(result7[54]).split())[0].split(">")[1])  #03
            try:
                r7=r7+float((str(result7[54]).split())[0].split(">")[1])
            except:
                r7=r7
            rainfall7.append(r7)
            Time7.append('{0}-{1}-{2} 03:00'.format(Yy7,Mm7,Dd7))
            HQ047.append((str(result7[71]).split())[0].split(">")[1])  #04
            try:
                r7=r7+float((str(result7[71]).split())[0].split(">")[1])
            except:
                r7=r7
            rainfall7.append(r7)
            Time7.append('{0}-{1}-{2} 04:00'.format(Yy7,Mm7,Dd7))
            HQ057.append((str(result7[88]).split())[0].split(">")[1])  #05 
            try:
                r7=r7+float((str(result7[88]).split())[0].split(">")[1])
            except:
                r7=r7
            rainfall7.append(r7)
            Time7.append('{0}-{1}-{2} 05:00'.format(Yy7,Mm7,Dd7))
            HQ067.append((str(result7[105]).split())[0].split(">")[1])  #06
            try:
                r7=r7+float((str(result7[105]).split())[0].split(">")[1])
            except:
                r7=r7
            rainfall7.append(r7)
            Time7.append('{0}-{1}-{2} 06:00'.format(Yy7,Mm7,Dd7))
            HQ077.append((str(result7[122]).split())[0].split(">")[1])  #07 
            try:
                r7=r7+float((str(result7[122]).split())[0].split(">")[1])
            except:
                r7=r7
            rainfall7.append(r7)
            Time7.append('{0}-{1}-{2} 07:00'.format(Yy7,Mm7,Dd7))
            HQ087.append((str(result7[139]).split())[0].split(">")[1])  #08
            try:
                r7=r7+float((str(result7[139]).split())[0].split(">")[1])
            except:
                r7=r7
            rainfall7.append(r7)
            Time7.append('{0}-{1}-{2} 08:00'.format(Yy7,Mm7,Dd7))
            HQ097.append((str(result7[156]).split())[0].split(">")[1])  #09
            try:
                r7=r7+float((str(result7[156]).split())[0].split(">")[1])
            except:
                r7=r7
            rainfall7.append(r7)
            Time7.append('{0}-{1}-{2} 09:00'.format(Yy7,Mm7,Dd7))
            HQ107.append((str(result7[173]).split())[0].split(">")[1])  #10
            try:
                r7=r7+float((str(result7[173]).split())[0].split(">")[1])
            except:
                r7=r7
            rainfall7.append(r7)
            Time7.append('{0}-{1}-{2} 10:00'.format(Yy7,Mm7,Dd7))
            HQ117.append((str(result7[190]).split())[0].split(">")[1])  #11
            try:
                r7=r7+float((str(result7[190]).split())[0].split(">")[1])
            except:
                r7=r7
            rainfall7.append(r7)
            Time7.append('{0}-{1}-{2} 11:00'.format(Yy7,Mm7,Dd7))
            HQ127.append((str(result7[207]).split())[0].split(">")[1])  #12
            try:
                r7=r7+float((str(result7[207]).split())[0].split(">")[1])
            except:
                r7=r7
            rainfall7.append(r7)
            Time7.append('{0}-{1}-{2} 12:00'.format(Yy7,Mm7,Dd7))
            HQ137.append((str(result7[224]).split())[0].split(">")[1])  #13
            try:
                r7=r7+float((str(result7[224]).split())[0].split(">")[1])
            except:
                r7=r7
            rainfall7.append(r7)
            Time7.append('{0}-{1}-{2} 13:00'.format(Yy7,Mm7,Dd7))
            HQ147.append((str(result7[241]).split())[0].split(">")[1])  #14
            try:
                r7=r7+float((str(result7[241]).split())[0].split(">")[1])  
            except:
                r7=r7
            rainfall7.append(r7)
            Time7.append('{0}-{1}-{2} 14:00'.format(Yy7,Mm7,Dd7))
            HQ157.append((str(result7[258]).split())[0].split(">")[1])  #15
            try:
                r7=r7+float((str(result7[258]).split())[0].split(">")[1])
            except:
                r7=r7
            rainfall7.append(r7)
            Time7.append('{0}-{1}-{2} 15:00'.format(Yy7,Mm7,Dd7))
            HQ167.append((str(result7[275]).split())[0].split(">")[1])  #16
            try:
                r7=r7+float((str(result7[275]).split())[0].split(">")[1])
            except:
                r7=r7
            rainfall7.append(r7)
            Time7.append('{0}-{1}-{2} 16:00'.format(Yy7,Mm7,Dd7))
            HQ177.append((str(result7[292]).split())[0].split(">")[1])  #17
            try:
                r7=r7+float((str(result7[292]).split())[0].split(">")[1])
            except:
                r7=r7
            rainfall7.append(r7)
            Time7.append('{0}-{1}-{2} 17:00'.format(Yy7,Mm7,Dd7)) 
            HQ187.append((str(result7[309]).split())[0].split(">")[1])  #18
            try:
                r7=r7+float((str(result7[309]).split())[0].split(">")[1])
            except:
                r7=r7
            rainfall7.append(r7)
            Time7.append('{0}-{1}-{2} 18:00'.format(Yy7,Mm7,Dd7))
            HQ197.append((str(result7[326]).split())[0].split(">")[1])  #19
            try:
                r7=r7+float((str(result7[326]).split())[0].split(">")[1])
            except:
                r7=r7
            rainfall7.append(r7)
            Time7.append('{0}-{1}-{2} 19:00'.format(Yy7,Mm7,Dd7))
            HQ207.append((str(result7[343]).split())[0].split(">")[1])  #20
            try:
                r7=r7+float((str(result7[343]).split())[0].split(">")[1])
            except:
                r7=r7
            rainfall7.append(r7)
            Time7.append('{0}-{1}-{2} 20:00'.format(Yy7,Mm7,Dd7))
            HQ217.append((str(result7[360]).split())[0].split(">")[1])  #21
            try:
                r7=r7+float((str(result7[360]).split())[0].split(">")[1])
            except:
                r7=r7
            rainfall7.append(r7)
            Time7.append('{0}-{1}-{2} 21:00'.format(Yy7,Mm7,Dd7))
            HQ227.append((str(result7[377]).split())[0].split(">")[1])  #22
            try:
                r7=r7+float((str(result7[377]).split())[0].split(">")[1])
            except:
                r7=r7
            rainfall7.append(r7)
            Time7.append('{0}-{1}-{2} 22:00'.format(Yy7,Mm7,Dd7))
            HQ237.append((str(result7[394]).split())[0].split(">")[1])  #23
            try:
                r7=r7+float((str(result7[394]).split())[0].split(">")[1])
            except:
                r7=r7
            rainfall7.append(r7)
            Time7.append('{0}-{1}-{2} 23:00'.format(Yy7,Mm7,Dd7))
            HQ247.append((str(result7[411]).split())[0].split(">")[1])  #24
            try:
                r7=r7+float((str(result7[411]).split())[0].split(">")[1])
            except:
                r7=r7
            rainfall7.append(r7)
            Time7.append('{0}-{1}-{2} 24:00'.format(Yy7,Mm7,Dd7))

            d7 = {
                "st_no":st_no7,   
                "yy":yy7,
                "mm":mm7,
                "dd":dd7,
                "HQ01":HQ017,
                "HQ02":HQ027,
                "HQ03":HQ037,
                "HQ04":HQ047,
                "HQ05":HQ057,
                "HQ06":HQ067,
                "HQ07":HQ077,
                "HQ08":HQ087,
                "HQ09":HQ097,
                "HQ10":HQ107,
                "HQ11":HQ117, ##
                "HQ12":HQ127,
                "HQ13":HQ137,
                "HQ14":HQ147,
                "HQ15":HQ157,
                "HQ16":HQ167,
                "HQ17":HQ177,
                "HQ18":HQ187,
                "HQ19":HQ197,
                "HQ20":HQ207,
                "HQ21":HQ217,
                "HQ22":HQ227,
                "HQ23":HQ237,
                "HQ24":HQ247,
                }
    
            time.sleep(random.uniform(0,0.1))

        START7=("{0} {1}:00".format(s_d7,s_t7))
        END7=("{0} {1}:00".format(e_d7,e_t7))
        for i in range(len(Time7)):
            if START7 == Time7[i]:
                SC7=i    
            if END7 == Time7[i]:
                EC7=i+1 

        del Time7[EC7:]
        del rainfall7[EC7:]
        del Time7[0:SC7]
        del rainfall7[0:SC7]
    
        for i in range(len(Time7)):
            TH7.append(i+1)

        T7=TH7
        RF7=rainfall7

        df7_test=(pd.DataFrame(data = d7))

        print("7-OKKK")
        button_start.configure(bg="Maroon")
        button_plus7.configure(bg="DarkGoldenrod")
    except:
        print("7-NO")
        button_start.configure(bg="Maroon")
        pass
    ###############################
    try:
        M8=[]
        D8=[]
        st_no8=[]

        yy8=[]
        mm8=[]
        dd8=[]

        HQ018=[]
        HQ028=[]
        HQ038=[]
        HQ048=[]
        HQ058=[]
        HQ068=[]
        HQ078=[]
        HQ088=[]
        HQ098=[]
        HQ108=[]
        HQ118=[]
        HQ128=[]
        HQ138=[] ##
        HQ148=[]
        HQ158=[]
        HQ168=[]
        HQ178=[]
        HQ188=[]
        HQ198=[]
        HQ208=[]
        HQ218=[]
        HQ228=[]
        HQ238=[]
        HQ248=[]
    
        rainfall8=[]
        Time8=[]
        TH8=[]
        r8=0
   
        if int(M28)-int(M18)>1:
            for i in range(31-int(D18)+1):
                M8.append(int(M18))
            for i in range(int(D18),32):
                D8.append(i)
            for i in range(int(M18)+1,int(M28)):
                for j in range(1,32):
                    M8.append(i)
            for i in range(int(M18),int(M28)-1):
                for j in range(1,32):
                    D8.append(j)
            for i in range(int(D28)):
                M8.append(int(M28))
            for i in range(1,int(D28)+1):
                D8.append(i)                
        elif int(M28)-int(M18)==1:
            for i in range(31-int(D18)+1):
                M8.append(int(M18))
            for i in range(int(D18),32):
                D8.append(i)
            for i in range(int(D28)):
                M8.append(int(M28))
            for i in range(1,int(D28)+1):
                D8.append(i)
        else:
            for i in range(int(D28)-int(D18)+1):
                M8.append(int(M18))
            for i in range(int(D18),int(D28)+1):
                D8.append(i)

        OUT8=[]
        SAVE_M8=[]
        SAVE_D8=[]
        for i in range(len(M8)):
        # print(M[i],D[i])
            if (M8[i]==2 and D8[i]>28) or (M8[i]==4 and D8[i]>30) or (M8[i]==6 and D8[i]>30) or (M8[i]==9 and D8[i]>30) or (M8[i]==11 and D8[i]>30):
                OUT8.append(i)
            
        for i in range(len(M8)):
            if i not in OUT8:
                SAVE_M8.append(M8[i])
                SAVE_D8.append(D8[i])  
        M8=SAVE_M8
        D8=SAVE_D8       

        for i in range(len(M8)):
            Yy8=Y18
            if M8[i]<10:
                Mm8='0{}'.format(M8[i])
            else:
                Mm8=str(M8[i])
    
            if D8[i]<10:
                Dd8='0{}'.format(D8[i])
            else:
                Dd8=str(D8[i])
            
            url8 = r'https://e-service.cwb.gov.tw/HistoryDataQuery/DayDataController.do?command=viewMain&station={0}&stname=%25E4%25B8%258A%25E5%25BE%25B7%25E6%2596%2587&datepicker={1}-{2}-{3}#'.format(ID8,Yy8,Mm8,Dd8)
        
            re8 = requests.get(url8) 
            soup8 = BeautifulSoup(re8.text, "html.parser")
            result8 = soup8.find_all("td")
            RR8 = soup8.find_all("head")
            t8 = str(RR8).split(";")
            x8 = t8[4].split("\"")   
            y8 = x8[1].split("-")
            st_no8.append(y8[0])
            dd8.append(y8[3]) 
            mm8.append(y8[2])
            yy8.append(y8[1])
    
            HQ018.append((str(result8[20]).split())[0].split(">")[1])  #01
            try:
                r8=r8+float((str(result8[20]).split())[0].split(">")[1])
            except:
                r8=r8
            rainfall8.append(r8)
            Time8.append('{0}-{1}-{2} 01:00'.format(Yy8,Mm8,Dd8)) 
            HQ028.append((str(result8[37]).split())[0].split(">")[1])  #02
            try:
                r8=r8+float((str(result8[37]).split())[0].split(">")[1])
            except:
                r8=r8
            rainfall8.append(r8)
            Time8.append('{0}-{1}-{2} 02:00'.format(Yy8,Mm8,Dd8)) 
            HQ038.append((str(result8[54]).split())[0].split(">")[1])  #03
            try:
                r8=r8+float((str(result8[54]).split())[0].split(">")[1])
            except:
                r8=r8
            rainfall8.append(r8)
            Time8.append('{0}-{1}-{2} 03:00'.format(Yy8,Mm8,Dd8))
            HQ048.append((str(result8[71]).split())[0].split(">")[1])  #04
            try:
                r8=r8+float((str(result8[71]).split())[0].split(">")[1])
            except:
                r8=r8
            rainfall8.append(r8)
            Time8.append('{0}-{1}-{2} 04:00'.format(Yy8,Mm8,Dd8))
            HQ058.append((str(result8[88]).split())[0].split(">")[1])  #05 
            try:
                r8=r8+float((str(result8[88]).split())[0].split(">")[1])
            except:
                r8=r8
            rainfall8.append(r8)
            Time8.append('{0}-{1}-{2} 05:00'.format(Yy8,Mm8,Dd8))
            HQ068.append((str(result8[105]).split())[0].split(">")[1])  #06
            try:
                r8=r8+float((str(result8[105]).split())[0].split(">")[1])
            except:
                r8=r8
            rainfall8.append(r8)
            Time8.append('{0}-{1}-{2} 06:00'.format(Yy8,Mm8,Dd8))
            HQ078.append((str(result8[122]).split())[0].split(">")[1])  #07 
            try:
                r8=r8+float((str(result8[122]).split())[0].split(">")[1])
            except:
                r8=r8
            rainfall8.append(r8)
            Time8.append('{0}-{1}-{2} 07:00'.format(Yy8,Mm8,Dd8))
            HQ088.append((str(result8[139]).split())[0].split(">")[1])  #08
            try:
                r8=r8+float((str(result8[139]).split())[0].split(">")[1])
            except:
                r8=r8
            rainfall8.append(r8)
            Time8.append('{0}-{1}-{2} 08:00'.format(Yy8,Mm8,Dd8))
            HQ098.append((str(result8[156]).split())[0].split(">")[1])  #09
            try:
                r8=r8+float((str(result8[156]).split())[0].split(">")[1])
            except:
                r8=r8
            rainfall8.append(r8)
            Time8.append('{0}-{1}-{2} 09:00'.format(Yy8,Mm8,Dd8))
            HQ108.append((str(result8[173]).split())[0].split(">")[1])  #10
            try:
                r8=r8+float((str(result8[173]).split())[0].split(">")[1])
            except:
                r8=r8
            rainfall8.append(r8)
            Time8.append('{0}-{1}-{2} 10:00'.format(Yy8,Mm8,Dd8))
            HQ118.append((str(result8[190]).split())[0].split(">")[1])  #11
            try:
                r8=r8+float((str(result8[190]).split())[0].split(">")[1])
            except:
                r8=r8
            rainfall8.append(r8)
            Time8.append('{0}-{1}-{2} 11:00'.format(Yy8,Mm8,Dd8))
            HQ128.append((str(result8[207]).split())[0].split(">")[1])  #12
            try:
                r8=r8+float((str(result8[207]).split())[0].split(">")[1])
            except:
                r8=r8
            rainfall8.append(r8)
            Time8.append('{0}-{1}-{2} 12:00'.format(Yy8,Mm8,Dd8))
            HQ138.append((str(result8[224]).split())[0].split(">")[1])  #13
            try:
                r8=r8+float((str(result8[224]).split())[0].split(">")[1])
            except:
                r8=r8
            rainfall8.append(r8)
            Time8.append('{0}-{1}-{2} 13:00'.format(Yy8,Mm8,Dd8))
            HQ148.append((str(result8[241]).split())[0].split(">")[1])  #14
            try:
                r8=r8+float((str(result8[241]).split())[0].split(">")[1])  
            except:
                r8=r8
            rainfall8.append(r8)
            Time8.append('{0}-{1}-{2} 14:00'.format(Yy8,Mm8,Dd8))
            HQ158.append((str(result8[258]).split())[0].split(">")[1])  #15
            try:
                r8=r8+float((str(result8[258]).split())[0].split(">")[1])
            except:
                r8=r8
            rainfall8.append(r8)
            Time8.append('{0}-{1}-{2} 15:00'.format(Yy8,Mm8,Dd8))
            HQ168.append((str(result8[275]).split())[0].split(">")[1])  #16
            try:
                r8=r8+float((str(result8[275]).split())[0].split(">")[1])
            except:
                r8=r8
            rainfall8.append(r8)
            Time8.append('{0}-{1}-{2} 16:00'.format(Yy8,Mm8,Dd8))
            HQ178.append((str(result8[292]).split())[0].split(">")[1])  #17
            try:
                r8=r8+float((str(result8[292]).split())[0].split(">")[1])
            except:
                r8=r8
            rainfall8.append(r8)
            Time8.append('{0}-{1}-{2} 17:00'.format(Yy8,Mm8,Dd8)) 
            HQ188.append((str(result8[309]).split())[0].split(">")[1])  #18
            try:
                r8=r8+float((str(result8[309]).split())[0].split(">")[1])
            except:
                r8=r8
            rainfall8.append(r8)
            Time8.append('{0}-{1}-{2} 18:00'.format(Yy8,Mm8,Dd8))
            HQ198.append((str(result8[326]).split())[0].split(">")[1])  #19
            try:
                r8=r8+float((str(result8[326]).split())[0].split(">")[1])
            except:
                r8=r8
            rainfall8.append(r8)
            Time8.append('{0}-{1}-{2} 19:00'.format(Yy8,Mm8,Dd8))
            HQ208.append((str(result8[343]).split())[0].split(">")[1])  #20
            try:
                r8=r8+float((str(result8[343]).split())[0].split(">")[1])
            except:
                r8=r8
            rainfall8.append(r8)
            Time8.append('{0}-{1}-{2} 20:00'.format(Yy8,Mm8,Dd8))
            HQ218.append((str(result8[360]).split())[0].split(">")[1])  #21
            try:
                r8=r8+float((str(result8[360]).split())[0].split(">")[1])
            except:
                r8=r8
            rainfall8.append(r8)
            Time8.append('{0}-{1}-{2} 21:00'.format(Yy8,Mm8,Dd8))
            HQ228.append((str(result8[377]).split())[0].split(">")[1])  #22
            try:
                r8=r8+float((str(result8[377]).split())[0].split(">")[1])
            except:
                r8=r8
            rainfall8.append(r8)
            Time8.append('{0}-{1}-{2} 22:00'.format(Yy8,Mm8,Dd8))
            HQ238.append((str(result8[394]).split())[0].split(">")[1])  #23
            try:
                r8=r8+float((str(result8[394]).split())[0].split(">")[1])
            except:
                r8=r8
            rainfall8.append(r8)
            Time8.append('{0}-{1}-{2} 23:00'.format(Yy8,Mm8,Dd8))
            HQ248.append((str(result8[411]).split())[0].split(">")[1])  #24
            try:
                r8=r8+float((str(result8[411]).split())[0].split(">")[1])
            except:
                r8=r8
            rainfall8.append(r8)
            Time8.append('{0}-{1}-{2} 24:00'.format(Yy8,Mm8,Dd8))

            d8 = {
                "st_no":st_no8,   
                "yy":yy8,
                "mm":mm8,
                "dd":dd8,
                "HQ01":HQ018,
                "HQ02":HQ028,
                "HQ03":HQ038,
                "HQ04":HQ048,
                "HQ05":HQ058,
                "HQ06":HQ068,
                "HQ07":HQ078,
                "HQ08":HQ088,
                "HQ09":HQ098,
                "HQ10":HQ108,
                "HQ11":HQ118, ##
                "HQ12":HQ128,
                "HQ13":HQ138,
                "HQ14":HQ148,
                "HQ15":HQ158,
                "HQ16":HQ168,
                "HQ17":HQ178,
                "HQ18":HQ188,
                "HQ19":HQ198,
                "HQ20":HQ208,
                "HQ21":HQ218,
                "HQ22":HQ228,
                "HQ23":HQ238,
                "HQ24":HQ248,
                }
    
            time.sleep(random.uniform(0,0.1))

        START8=("{0} {1}:00".format(s_d8,s_t8))
        END8=("{0} {1}:00".format(e_d8,e_t8))
        for i in range(len(Time8)):
            if START8 == Time8[i]:
                SC8=i    
            if END8 == Time8[i]:
                EC8=i+1 

        del Time8[EC8:]
        del rainfall8[EC8:]
        del Time8[0:SC8]
        del rainfall8[0:SC8]
    
        for i in range(len(Time8)):
            TH8.append(i+1)

        T8=TH8
        RF8=rainfall8

        df8_test=(pd.DataFrame(data = d8))

        print("8-OKKK")
        button_start.configure(bg="Maroon")
        button_plus8.configure(bg="DarkGoldenrod")
    except:
        print("8-NO")
        button_start.configure(bg="Maroon")
        pass
    #################################3
    try:
        M9=[]
        D9=[]
        st_no9=[]

        yy9=[]
        mm9=[]
        dd9=[]

        HQ019=[]
        HQ029=[]
        HQ039=[]
        HQ049=[]
        HQ059=[]
        HQ069=[]
        HQ079=[]
        HQ089=[]
        HQ099=[]
        HQ109=[]
        HQ119=[]
        HQ129=[]
        HQ139=[] ##
        HQ149=[]
        HQ159=[]
        HQ169=[]
        HQ179=[]
        HQ189=[]
        HQ199=[]
        HQ209=[]
        HQ219=[]
        HQ229=[]
        HQ239=[]
        HQ249=[]
    
        rainfall9=[]
        Time9=[]
        TH9=[]
        r9=0
   
        if int(M29)-int(M19)>1:
            for i in range(31-int(D19)+1):
                M9.append(int(M19))
            for i in range(int(D19),32):
                D9.append(i)
            for i in range(int(M19)+1,int(M29)):
                for j in range(1,32):
                    M9.append(i)
            for i in range(int(M19),int(M29)-1):
                for j in range(1,32):
                    D9.append(j)
            for i in range(int(D29)):
                M9.append(int(M29))
            for i in range(1,int(D29)+1):
                D9.append(i)                
        elif int(M29)-int(M19)==1:
            for i in range(31-int(D19)+1):
                M9.append(int(M19))
            for i in range(int(D19),32):
                D9.append(i)
            for i in range(int(D29)):
                M9.append(int(M29))
            for i in range(1,int(D29)+1):
                D9.append(i)
        else:
            for i in range(int(D29)-int(D19)+1):
                M9.append(int(M19))
            for i in range(int(D19),int(D29)+1):
                D9.append(i)

        OUT9=[]
        SAVE_M9=[]
        SAVE_D9=[]
        for i in range(len(M9)):
        # print(M[i],D[i])
            if (M9[i]==2 and D9[i]>28) or (M9[i]==4 and D9[i]>30) or (M9[i]==6 and D9[i]>30) or (M9[i]==9 and D9[i]>30) or (M9[i]==11 and D9[i]>30):
                OUT9.append(i)
            
        for i in range(len(M9)):
            if i not in OUT9:
                SAVE_M9.append(M9[i])
                SAVE_D9.append(D9[i])  
        M9=SAVE_M9
        D9=SAVE_D9       

        for i in range(len(M9)):
            Yy9=Y19
            if M9[i]<10:
                Mm9='0{}'.format(M9[i])
            else:
                Mm9=str(M9[i])
    
            if D9[i]<10:
                Dd9='0{}'.format(D9[i])
            else:
                Dd9=str(D9[i])
            
            url9 = r'https://e-service.cwb.gov.tw/HistoryDataQuery/DayDataController.do?command=viewMain&station={0}&stname=%25E4%25B8%258A%25E5%25BE%25B7%25E6%2596%2587&datepicker={1}-{2}-{3}#'.format(ID9,Yy9,Mm9,Dd9)
        
            re9 = requests.get(url9) 
            soup9 = BeautifulSoup(re9.text, "html.parser")
            result9 = soup9.find_all("td")
            RR9 = soup9.find_all("head")
            t9 = str(RR9).split(";")
            x9 = t9[4].split("\"")   
            y9 = x9[1].split("-")
            st_no9.append(y9[0])
            dd9.append(y9[3]) 
            mm9.append(y9[2])
            yy9.append(y9[1])
    
            HQ019.append((str(result9[20]).split())[0].split(">")[1])  #01
            try:
                r9=r9+float((str(result9[20]).split())[0].split(">")[1])
            except:
                r9=r9
            rainfall9.append(r9)
            Time9.append('{0}-{1}-{2} 01:00'.format(Yy9,Mm9,Dd9)) 
            HQ029.append((str(result9[37]).split())[0].split(">")[1])  #02
            try:
                r9=r9+float((str(result9[37]).split())[0].split(">")[1])
            except:
                r9=r9
            rainfall9.append(r9)
            Time9.append('{0}-{1}-{2} 02:00'.format(Yy9,Mm9,Dd9)) 
            HQ039.append((str(result9[54]).split())[0].split(">")[1])  #03
            try:
                r9=r9+float((str(result9[54]).split())[0].split(">")[1])
            except:
                r9=r9
            rainfall9.append(r9)
            Time9.append('{0}-{1}-{2} 03:00'.format(Yy9,Mm9,Dd9))
            HQ049.append((str(result9[71]).split())[0].split(">")[1])  #04
            try:
                r9=r9+float((str(result9[71]).split())[0].split(">")[1])
            except:
                r9=r9
            rainfall9.append(r9)
            Time9.append('{0}-{1}-{2} 04:00'.format(Yy9,Mm9,Dd9))
            HQ059.append((str(result9[88]).split())[0].split(">")[1])  #05 
            try:
                r9=r9+float((str(result9[88]).split())[0].split(">")[1])
            except:
                r9=r9
            rainfall9.append(r9)
            Time9.append('{0}-{1}-{2} 05:00'.format(Yy9,Mm9,Dd9))
            HQ069.append((str(result9[105]).split())[0].split(">")[1])  #06
            try:
                r9=r9+float((str(result9[105]).split())[0].split(">")[1])
            except:
                r9=r9
            rainfall9.append(r9)
            Time9.append('{0}-{1}-{2} 06:00'.format(Yy9,Mm9,Dd9))
            HQ079.append((str(result9[122]).split())[0].split(">")[1])  #07 
            try:
                r9=r9+float((str(result9[122]).split())[0].split(">")[1])
            except:
                r9=r9
            rainfall9.append(r9)
            Time9.append('{0}-{1}-{2} 07:00'.format(Yy9,Mm9,Dd9))
            HQ089.append((str(result9[139]).split())[0].split(">")[1])  #08
            try:
                r9=r9+float((str(result9[139]).split())[0].split(">")[1])
            except:
                r9=r9
            rainfall9.append(r9)
            Time9.append('{0}-{1}-{2} 08:00'.format(Yy9,Mm9,Dd9))
            HQ099.append((str(result9[156]).split())[0].split(">")[1])  #09
            try:
                r9=r9+float((str(result9[156]).split())[0].split(">")[1])
            except:
                r9=r9
            rainfall9.append(r9)
            Time9.append('{0}-{1}-{2} 09:00'.format(Yy9,Mm9,Dd9))
            HQ109.append((str(result9[173]).split())[0].split(">")[1])  #10
            try:
                r9=r9+float((str(result9[173]).split())[0].split(">")[1])
            except:
                r9=r9
            rainfall9.append(r9)
            Time9.append('{0}-{1}-{2} 10:00'.format(Yy9,Mm9,Dd9))
            HQ119.append((str(result9[190]).split())[0].split(">")[1])  #11
            try:
                r9=r9+float((str(result9[190]).split())[0].split(">")[1])
            except:
                r9=r9
            rainfall9.append(r9)
            Time9.append('{0}-{1}-{2} 11:00'.format(Yy9,Mm9,Dd9))
            HQ129.append((str(result9[207]).split())[0].split(">")[1])  #12
            try:
                r9=r9+float((str(result9[207]).split())[0].split(">")[1])
            except:
                r9=r9
            rainfall9.append(r9)
            Time9.append('{0}-{1}-{2} 12:00'.format(Yy9,Mm9,Dd9))
            HQ139.append((str(result9[224]).split())[0].split(">")[1])  #13
            try:
                r9=r9+float((str(result9[224]).split())[0].split(">")[1])
            except:
                r9=r9
            rainfall9.append(r9)
            Time9.append('{0}-{1}-{2} 13:00'.format(Yy9,Mm9,Dd9))
            HQ149.append((str(result9[241]).split())[0].split(">")[1])  #14
            try:
                r9=r9+float((str(result9[241]).split())[0].split(">")[1])  
            except:
                r9=r9
            rainfall9.append(r9)
            Time9.append('{0}-{1}-{2} 14:00'.format(Yy9,Mm9,Dd9))
            HQ159.append((str(result9[258]).split())[0].split(">")[1])  #15
            try:
                r9=r9+float((str(result9[258]).split())[0].split(">")[1])
            except:
                r9=r9
            rainfall9.append(r9)
            Time9.append('{0}-{1}-{2} 15:00'.format(Yy9,Mm9,Dd9))
            HQ169.append((str(result9[275]).split())[0].split(">")[1])  #16
            try:
                r9=r9+float((str(result9[275]).split())[0].split(">")[1])
            except:
                r9=r9
            rainfall9.append(r9)
            Time9.append('{0}-{1}-{2} 16:00'.format(Yy9,Mm9,Dd9))
            HQ179.append((str(result9[292]).split())[0].split(">")[1])  #17
            try:
                r9=r9+float((str(result9[292]).split())[0].split(">")[1])
            except:
                r9=r9
            rainfall9.append(r9)
            Time9.append('{0}-{1}-{2} 17:00'.format(Yy9,Mm9,Dd9)) 
            HQ189.append((str(result9[309]).split())[0].split(">")[1])  #18
            try:
                r9=r9+float((str(result9[309]).split())[0].split(">")[1])
            except:
                r9=r9
            rainfall9.append(r9)
            Time9.append('{0}-{1}-{2} 18:00'.format(Yy9,Mm9,Dd9))
            HQ199.append((str(result9[326]).split())[0].split(">")[1])  #19
            try:
                r9=r9+float((str(result9[326]).split())[0].split(">")[1])
            except:
                r9=r9
            rainfall9.append(r9)
            Time9.append('{0}-{1}-{2} 19:00'.format(Yy9,Mm9,Dd9))
            HQ209.append((str(result9[343]).split())[0].split(">")[1])  #20
            try:
                r9=r9+float((str(result9[343]).split())[0].split(">")[1])
            except:
                r9=r9
            rainfall9.append(r9)
            Time9.append('{0}-{1}-{2} 20:00'.format(Yy9,Mm9,Dd9))
            HQ219.append((str(result9[360]).split())[0].split(">")[1])  #21
            try:
                r9=r9+float((str(result9[360]).split())[0].split(">")[1])
            except:
                r9=r9
            rainfall9.append(r9)
            Time9.append('{0}-{1}-{2} 21:00'.format(Yy9,Mm9,Dd9))
            HQ229.append((str(result9[377]).split())[0].split(">")[1])  #22
            try:
                r9=r9+float((str(result9[377]).split())[0].split(">")[1])
            except:
                r9=r9
            rainfall9.append(r9)
            Time9.append('{0}-{1}-{2} 22:00'.format(Yy9,Mm9,Dd9))
            HQ239.append((str(result9[394]).split())[0].split(">")[1])  #23
            try:
                r9=r9+float((str(result9[394]).split())[0].split(">")[1])
            except:
                r9=r9
            rainfall9.append(r9)
            Time9.append('{0}-{1}-{2} 23:00'.format(Yy9,Mm9,Dd9))
            HQ249.append((str(result9[411]).split())[0].split(">")[1])  #24
            try:
                r9=r9+float((str(result9[411]).split())[0].split(">")[1])
            except:
                r9=r9
            rainfall9.append(r9)
            Time9.append('{0}-{1}-{2} 24:00'.format(Yy9,Mm9,Dd9))

            d9 = {
                "st_no":st_no9,   
                "yy":yy9,
                "mm":mm9,
                "dd":dd9,
                "HQ01":HQ019,
                "HQ02":HQ029,
                "HQ03":HQ039,
                "HQ04":HQ049,
                "HQ05":HQ059,
                "HQ06":HQ069,
                "HQ07":HQ079,
                "HQ08":HQ089,
                "HQ09":HQ099,
                "HQ10":HQ109,
                "HQ11":HQ119, ##
                "HQ12":HQ129,
                "HQ13":HQ139,
                "HQ14":HQ149,
                "HQ15":HQ159,
                "HQ16":HQ169,
                "HQ17":HQ179,
                "HQ18":HQ189,
                "HQ19":HQ199,
                "HQ20":HQ209,
                "HQ21":HQ219,
                "HQ22":HQ229,
                "HQ23":HQ239,
                "HQ24":HQ249,
                }
    
            time.sleep(random.uniform(0,0.1))

        START9=("{0} {1}:00".format(s_d9,s_t9))
        END9=("{0} {1}:00".format(e_d9,e_t9))
        for i in range(len(Time9)):
            if START9 == Time9[i]:
                SC9=i    
            if END9 == Time9[i]:
                EC9=i+1 

        del Time9[EC9:]
        del rainfall9[EC9:]
        del Time9[0:SC9]
        del rainfall9[0:SC9]
    
        for i in range(len(Time9)):
            TH9.append(i+1)

        T9=TH9
        RF9=rainfall9

        df9_test=(pd.DataFrame(data = d9))

        print("9-OKKK")
        button_start.configure(bg="Maroon")
        button_plus9.configure(bg="DarkGoldenrod")
    except:
        print("9-NO")
        button_start.configure(bg="Maroon")
        pass
    ###############################
    try:
        M10=[]
        D10=[]
        st_no10=[]

        yy10=[]
        mm10=[]
        dd10=[]

        HQ0110=[]
        HQ0210=[]
        HQ0310=[]
        HQ0410=[]
        HQ0510=[]
        HQ0610=[]
        HQ0710=[]
        HQ0810=[]
        HQ0910=[]
        HQ1010=[]
        HQ1110=[]
        HQ1210=[]
        HQ1310=[] ##
        HQ1410=[]
        HQ1510=[]
        HQ1610=[]
        HQ1710=[]
        HQ1810=[]
        HQ1910=[]
        HQ2010=[]
        HQ2110=[]
        HQ2210=[]
        HQ2310=[]
        HQ2410=[]
    
        rainfall10=[]
        Time10=[]
        TH10=[]
        r10=0
   
        if int(M210)-int(M110)>1:
            for i in range(31-int(D110)+1):
                M10.append(int(M110))
            for i in range(int(D110),32):
                D10.append(i)
            for i in range(int(M110)+1,int(M210)):
                for j in range(1,32):
                    M10.append(i)
            for i in range(int(M110),int(M210)-1):
                for j in range(1,32):
                    D10.append(j)
            for i in range(int(D210)):
                M10.append(int(M210))
            for i in range(1,int(D210)+1):
                D10.append(i)                
        elif int(M210)-int(M110)==1:
            for i in range(31-int(D110)+1):
                M10.append(int(M110))
            for i in range(int(D110),32):
                D10.append(i)
            for i in range(int(D210)):
                M10.append(int(M210))
            for i in range(1,int(D210)+1):
                D10.append(i)
        else:
            for i in range(int(D210)-int(D110)+1):
                M10.append(int(M110))
            for i in range(int(D110),int(D210)+1):
                D10.append(i)

        OUT10=[]
        SAVE_M10=[]
        SAVE_D10=[]
        for i in range(len(M10)):
        # print(M[i],D[i])
            if (M10[i]==2 and D10[i]>28) or (M10[i]==4 and D10[i]>30) or (M10[i]==6 and D10[i]>30) or (M10[i]==9 and D10[i]>30) or (M10[i]==11 and D10[i]>30):
                OUT10.append(i)
            
        for i in range(len(M10)):
            if i not in OUT10:
                SAVE_M10.append(M10[i])
                SAVE_D10.append(D10[i])  
        M10=SAVE_M10
        D10=SAVE_D10       

        for i in range(len(M10)):
            Yy10=Y110
            if M10[i]<10:
                Mm10='0{}'.format(M10[i])
            else:
                Mm10=str(M10[i])
    
            if D10[i]<10:
                Dd10='0{}'.format(D10[i])
            else:
                Dd10=str(D10[i])
            
            url10= r'https://e-service.cwb.gov.tw/HistoryDataQuery/DayDataController.do?command=viewMain&station={0}&stname=%25E4%25B8%258A%25E5%25BE%25B7%25E6%2596%2587&datepicker={1}-{2}-{3}#'.format(ID10,Yy10,Mm10,Dd10)
        
            re10 = requests.get(url10) 
            soup10 = BeautifulSoup(re10.text, "html.parser")
            result10 = soup10.find_all("td")
            RR10 = soup10.find_all("head")
            t10 = str(RR10).split(";")
            x10 = t10[4].split("\"")   
            y10 = x10[1].split("-")
            st_no10.append(y10[0])
            dd10.append(y10[3]) 
            mm10.append(y10[2])
            yy10.append(y10[1])
    
            HQ0110.append((str(result10[20]).split())[0].split(">")[1])  #01
            try:
                r10=r10+float((str(result10[20]).split())[0].split(">")[1])
            except:
                r10=r10
            rainfall10.append(r10)
            Time10.append('{0}-{1}-{2} 01:00'.format(Yy10,Mm10,Dd10)) 
            HQ0210.append((str(result10[37]).split())[0].split(">")[1])  #02
            try:
                r10=r10+float((str(result10[37]).split())[0].split(">")[1])
            except:
                r10=r10
            rainfall10.append(r10)
            Time10.append('{0}-{1}-{2} 02:00'.format(Yy10,Mm10,Dd10)) 
            HQ0310.append((str(result10[54]).split())[0].split(">")[1])  #03
            try:
                r10=r10+float((str(result10[54]).split())[0].split(">")[1])
            except:
                r10=r10
            rainfall10.append(r10)
            Time10.append('{0}-{1}-{2} 03:00'.format(Yy10,M10,Dd10))
            HQ0410.append((str(result10[71]).split())[0].split(">")[1])  #04
            try:
                r10=r10+float((str(result10[71]).split())[0].split(">")[1])
            except:
                r10=r10
            rainfall10.append(r10)
            Time10.append('{0}-{1}-{2} 04:00'.format(Yy10,Mm10,Dd10))
            HQ0510.append((str(result10[88]).split())[0].split(">")[1])  #05 
            try:
                r10=r10+float((str(result10[88]).split())[0].split(">")[1])
            except:
                r10=r10
            rainfall10.append(r10)
            Time10.append('{0}-{1}-{2} 05:00'.format(Yy10,Mm10,Dd10))
            HQ0610.append((str(result10[105]).split())[0].split(">")[1])  #06
            try:
                r10=r10+float((str(result10[105]).split())[0].split(">")[1])
            except:
                r10=r10
            rainfall10.append(r10)
            Time10.append('{0}-{1}-{2} 06:00'.format(Yy10,Mm10,Dd10))
            HQ0710.append((str(result10[122]).split())[0].split(">")[1])  #07 
            try:
                r10=r10+float((str(result10[122]).split())[0].split(">")[1])
            except:
                r10=r10
            rainfall10.append(r10)
            Time10.append('{0}-{1}-{2} 07:00'.format(Yy10,Mm10,Dd10))
            HQ0810.append((str(result10[139]).split())[0].split(">")[1])  #08
            try:
                r10=r10+float((str(result10[139]).split())[0].split(">")[1])
            except:
                r10=r10
            rainfall10.append(r10)
            Time10.append('{0}-{1}-{2} 08:00'.format(Yy10,Mm10,Dd10))
            HQ0910.append((str(result10[156]).split())[0].split(">")[1])  #09
            try:
                r10=r10+float((str(result10[156]).split())[0].split(">")[1])
            except:
                r10=r10
            rainfall10.append(r10)
            Time10.append('{0}-{1}-{2} 09:00'.format(Yy10,Mm10,Dd10))
            HQ1010.append((str(result10[173]).split())[0].split(">")[1])  #10
            try:
                r10=r10+float((str(result10[173]).split())[0].split(">")[1])
            except:
                r10=r10
            rainfall10.append(r10)
            Time10.append('{0}-{1}-{2} 10:00'.format(Yy10,Mm10,Dd10))
            HQ1110.append((str(result10[190]).split())[0].split(">")[1])  #11
            try:
                r10=r10+float((str(result10[190]).split())[0].split(">")[1])
            except:
                r10=r10
            rainfall10.append(r10)
            Time10.append('{0}-{1}-{2} 11:00'.format(Yy10,Mm10,Dd10))
            HQ1210.append((str(result10[207]).split())[0].split(">")[1])  #12
            try:
                r10=r10+float((str(result10[207]).split())[0].split(">")[1])
            except:
                r10=r10
            rainfall10.append(r10)
            Time10.append('{0}-{1}-{2} 12:00'.format(Yy10,Mm10,Dd10))
            HQ1310.append((str(result10[224]).split())[0].split(">")[1])  #13
            try:
                r10=r10+float((str(result10[224]).split())[0].split(">")[1])
            except:
                r10=r10
            rainfall10.append(r10)
            Time10.append('{0}-{1}-{2} 13:00'.format(Yy10,Mm10,Dd10))
            HQ1410.append((str(result10[241]).split())[0].split(">")[1])  #14
            try:
                r10=r10+float((str(result10[241]).split())[0].split(">")[1])  
            except:
                r10=r10
            rainfall10.append(r10)
            Time10.append('{0}-{1}-{2} 14:00'.format(Yy10,Mm10,Dd10))
            HQ1510.append((str(result10[258]).split())[0].split(">")[1])  #15
            try:
                r10=r10+float((str(result10[258]).split())[0].split(">")[1])
            except:
                r10=r10
            rainfall10.append(r10)
            Time10.append('{0}-{1}-{2} 15:00'.format(Yy10,Mm10,Dd10))
            HQ1610.append((str(result10[275]).split())[0].split(">")[1])  #16
            try:
                r10=r10+float((str(result10[275]).split())[0].split(">")[1])
            except:
                r10=r10
            rainfall10.append(r10)
            Time10.append('{0}-{1}-{2} 16:00'.format(Yy10,Mm10,Dd10))
            HQ1710.append((str(result10[292]).split())[0].split(">")[1])  #17
            try:
                r10=r10+float((str(result10[292]).split())[0].split(">")[1])
            except:
                r10=r10
            rainfall10.append(r10)
            Time10.append('{0}-{1}-{2} 17:00'.format(Yy10,Mm10,Dd10)) 
            HQ1810.append((str(result10[309]).split())[0].split(">")[1])  #18
            try:
                r10=r10+float((str(result10[309]).split())[0].split(">")[1])
            except:
                r10=r10
            rainfall10.append(r10)
            Time10.append('{0}-{1}-{2} 18:00'.format(Yy10,Mm10,Dd10))
            HQ1910.append((str(result10[326]).split())[0].split(">")[1])  #19
            try:
                r10=r10+float((str(result10[326]).split())[0].split(">")[1])
            except:
                r10=r10
            rainfall10.append(r10)
            Time10.append('{0}-{1}-{2} 19:00'.format(Yy10,Mm10,Dd10))
            HQ2010.append((str(result10[343]).split())[0].split(">")[1])  #20
            try:
                r10=r10+float((str(result10[343]).split())[0].split(">")[1])
            except:
                r10=r10
            rainfall10.append(r10)
            Time10.append('{0}-{1}-{2} 20:00'.format(Yy10,Mm10,Dd10))
            HQ2110.append((str(result10[360]).split())[0].split(">")[1])  #21
            try:
                r10=r10+float((str(result10[360]).split())[0].split(">")[1])
            except:
                r10=r10
            rainfall10.append(r10)
            Time10.append('{0}-{1}-{2} 21:00'.format(Yy10,Mm10,Dd10))
            HQ2210.append((str(result10[377]).split())[0].split(">")[1])  #22
            try:
                r10=r10+float((str(result10[377]).split())[0].split(">")[1])
            except:
                r10=r10
            rainfall10.append(r10)
            Time10.append('{0}-{1}-{2} 22:00'.format(Yy10,Mm10,Dd10))
            HQ2310.append((str(result10[394]).split())[0].split(">")[1])  #23
            try:
                r10=r10+float((str(result10[394]).split())[0].split(">")[1])
            except:
                r10=r10
            rainfall10.append(r10)
            Time10.append('{0}-{1}-{2} 23:00'.format(Yy10,Mm10,Dd10))
            HQ2410.append((str(result10[411]).split())[0].split(">")[1])  #24
            try:
                r10=r10+float((str(result10[411]).split())[0].split(">")[1])
            except:
                r10=r10
            rainfall10.append(r10)
            Time10.append('{0}-{1}-{2} 24:00'.format(Yy10,Mm10,Dd10))

            d10 = {
                "st_no":st_no10,   
                "yy":yy10,
                "mm":mm10,
                "dd":dd10,
                "HQ01":HQ0110,
                "HQ02":HQ0210,
                "HQ03":HQ0310,
                "HQ04":HQ0410,
                "HQ05":HQ0510,
                "HQ06":HQ0610,
                "HQ07":HQ0710,
                "HQ08":HQ0810,
                "HQ09":HQ0910,
                "HQ10":HQ1010,
                "HQ11":HQ1110, ##
                "HQ12":HQ1210,
                "HQ13":HQ1310,
                "HQ14":HQ1410,
                "HQ15":HQ1510,
                "HQ16":HQ1610,
                "HQ17":HQ1710,
                "HQ18":HQ1810,
                "HQ19":HQ1910,
                "HQ20":HQ2010,
                "HQ21":HQ2110,
                "HQ22":HQ2210,
                "HQ23":HQ2310,
                "HQ24":HQ2410,
                }
    
            time.sleep(random.uniform(0,0.1))

        START10=("{0} {1}:00".format(s_d10,s_t10))
        END10=("{0} {1}:00".format(e_d10,e_t10))
        for i in range(len(Time10)):
            if START10 == Time10[i]:
                SC10=i    
            if END10 == Time10[i]:
                EC10=i+1 

        del Time10[EC10:]
        del rainfall10[EC10:]
        del Time10[0:SC10]
        del rainfall10[0:SC10]
    
        for i in range(len(Time10)):
            TH10.append(i+1)

        T10=TH10
        RF10=rainfall10

        df10_test=(pd.DataFrame(data = d10))

        print("10-OKKK")
        button_start.configure(bg="Maroon")
        button_plus10.configure(bg="DarkGoldenrod")
    except:
        print("10-NO")
        button_start.configure(bg="Maroon")
        pass
        
    
    plt.figure(figsize=(10,5),dpi=100)
    plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
    plt.rcParams['axes.unicode_minus'] = False
    try:
        L1=plt.plot(T1,RF1,label=('{}'.format(EVENT1)))
        plt.legend()
    except:
        pass
    try:
        L2=plt.plot(T2,RF2,label=('{}'.format(EVENT2)))  
    except:
        pass
    try:
        L3=plt.plot(T3,RF3,label=('{}'.format(EVENT3))) 
    except:
        pass
    try:
        L4=plt.plot(T4,RF4,label=('{}'.format(EVENT4)))  
    except:
        pass
    try:
        L5=plt.plot(T5,RF5,label=('{}'.format(EVENT5)))  
    except:
        pass
    try:
        L6=plt.plot(T6,RF6,label=('{}'.format(EVENT6)))  
    except:
        pass
    try:
        L7=plt.plot(T7,RF7,label=('{}'.format(EVENT7)))  
    except:
        pass
    try:
        L8=plt.plot(T8,RF8,label=('{}'.format(EVENT8)))  
    except:
        pass
    try:
        L9=plt.plot(T9,RF9,label=('{}'.format(EVENT9)))  
    except:
        pass
    try:
        L10=plt.plot(T10,RF10,label=('{}'.format(EVENT10)))  
    except:
        pass
    
    plt.legend()
    plt.ylabel("累積降雨量(mm)")
    plt.xlabel("降雨時序(hr)")
    plt.show()
    
    try:
        df={key: d1[key] + d2[key] + d3[key] + d4[key] + d5[key] + d6[key] + d7[key] + d8[key] + d9[key] + d10[key] for key in d1}
    except:
        try:
            df={key: d1[key] + d2[key] + d3[key] + d4[key] + d5[key] + d6[key] + d7[key] + d8[key] + d9[key] for key in d1}
        except:
            try:
                df={key: d1[key] + d2[key] + d3[key] + d4[key] + d5[key] + d6[key] + d7[key] + d8[key] for key in d1}
            except:
                try:
                    df={key: d1[key] + d2[key] + d3[key] + d4[key] + d5[key] + d6[key] + d7[key] for key in d1}
                except:
                    try:
                        df={key: d1[key] + d2[key] + d3[key] + d4[key] + d5[key] + d6[key] for key in d1}
                    except:
                        try:
                            df={key: d1[key] + d2[key] + d3[key] + d4[key] + d5[key] for key in d1}
                        except:
                            try:
                                df={key: d1[key] + d2[key] + d3[key] + d4[key] for key in d1}
                            except:
                                try:
                                    df={key: d1[key] + d2[key] + d3[key] for key in d1}
                                except:
                                    try:
                                        df={key: d1[key] + d2[key] for key in d1}
                                    except:
                                        df=d1
                                    
    DF=(pd.DataFrame(data = df))

    var1 = tk.StringVar()
    entry1 = tk.Entry(root, width=20, textvariable=var1)
    entry1.insert(0, "格式1-XXX.csv")
    entry1.place(x=350, y=14+50*11)
    Labelf1=tk.Label(root,text='HQ01 | HQ02 | HQ03...')
    Labelf1.place(x=450, y=14+50*10.93, width=138, height=30)

    var2 = tk.StringVar()
    entry2 = tk.Entry(root, width=20, textvariable=var2)
    entry2.insert(0, "格式2-XXX.csv")
    entry2.place(x=350, y=14+50*12.1)
    Labe2f1=tk.Label(root,text='st_no | Time | rain')
    Labe2f1.place(x=450, y=14+50*12.03, width=120, height=30)

    sn=[]
    IDn=[]
    for i in range(len(DF)):
        for j in range(0,24):
            IDn.append(DF['st_no'][i])
            if j<9:
                sn.append("{0}/{1}/{2} 0{3}:00".format(int(DF['yy'][i]),int(DF['mm'][i]),int(DF['dd'][i]),j+1))
            else:
                if (j+1==24 and ( (int(DF['mm'][i])==1) and (int(DF['mm'][i])==3) and (int(DF['mm'][i])==5) and (int(DF['mm'][i])==7) and (int(DF['mm'][i])==8) and (int(DF['mm'][i])==10) and (int(DF['mm'][i])==12)) and (int(DF['dd'][i])==31)):    
                    if (int(DF['mm'][i])+1)==13:
                        sn.append("{0}/{1}/{2} 0{3}:00".format(int(DF['yy'][i])+1,1,1,'00'))
                    else:
                        sn.append("{0}/{1}/{2} {3}:00".format(int(DF['yy'][i]),int(DF['mm'][i])+1,1,'00'))
                    
                elif (j+1==24 and ( (int(DF['mm'][i])==4) and (int(DF['mm'][i])==6) and (int(DF['mm'][i])==9) and (int(DF['mm'][i])==11)) and (int(DF['dd'][i])==30)):                                         
                    sn.append("{0}/{1}/{2} {3}:00".format(int(DF['yy'][i]),int(DF['mm'][i])+1,1,'00'))
                
                elif(j+1==24 and (int(DF['mm'][i])==2) and (int(DF['dd'][i])==29)):
                    sn.append("{0}/{1}/{2} {3}:00".format(int(DF['yy'][i]),int(DF['mm'][i])+1,1,'00'))
                else:
                    if j+1==24:
                        sn.append("{0}/{1}/{2} {3}:00".format(int(DF['yy'][i]),int(DF['mm'][i]),int(DF['dd'][i])+1,'00'))
                    else:
                        sn.append("{0}/{1}/{2} {3}:00".format(int(DF['yy'][i]),int(DF['mm'][i]),int(DF['dd'][i]),j+1))
    



    rn=[]
    for j in range(len(DF)):
        for i in range(4,28):
            if(DF.iat[j,i])=="&amp;":
                rn.append(0.0)
            else:
                rn.append(DF.iat[j,i])

    DF2 = {
        "st_no":IDn,
        "Time":sn,
        "rain":rn
        }

    DF2=(pd.DataFrame(data = DF2))

    def save1():
        var1 = entry1.get()
        spath = filedialog.askdirectory(title='選擇存檔位置')
        DF.to_csv(r'{}'.format(os.path.join(spath,str(var1))),index=False)
        Labels=tk.Label(root,text='以上資料已儲存')
        Labels.place(x=400, y=14+50*11.4, width=100, height=30)    

    def save2():
        var2 = entry2.get()
        spath = filedialog.askdirectory(title='選擇存檔位置')
        DF2.to_csv(r'{}'.format(os.path.join(spath,str(var2))),index=False)
        Labels=tk.Label(root,text='以上資料已儲存')
        Labels.place(x=400, y=14+50*12.5, width=100, height=30)

    bsave1 = tk.Button(root,text='存檔1',bg='DarkGoldenrod',fg='white',command=save1)
    bsave1.place(x=600, y=14+50*11)
    bsave2 = tk.Button(root,text='存檔2',bg='DarkGoldenrod',fg='white',command=save2)
    bsave2.place(x=600, y=14+50*12.1)                        
    

#--------------------------
button_plus1 = tk.Button(root, text='+', bg='FireBrick',fg='white', state=tk.NORMAL, command=b_plus1)  
button_plus1.place(x=775, y=14+50, width=20, height=20)

button_plus2 = tk.Button(root, text='+', bg='FireBrick',fg='white', state=tk.NORMAL, command=b_plus2)  
button_plus2.place(x=775, y=14+50*2, width=20, height=20)

button_plus3 = tk.Button(root, text='+', bg='FireBrick',fg='white', state=tk.NORMAL, command=b_plus3)  
button_plus3.place(x=775, y=14+50*3, width=20, height=20)

button_plus4 = tk.Button(root, text='+', bg='FireBrick',fg='white', state=tk.NORMAL, command=b_plus4)  
button_plus4.place(x=775, y=14+50*4, width=20, height=20)

button_plus5 = tk.Button(root, text='+', bg='FireBrick',fg='white', state=tk.NORMAL, command=b_plus5)  
button_plus5.place(x=775, y=14+50*5, width=20, height=20)

button_plus6 = tk.Button(root, text='+', bg='FireBrick',fg='white', state=tk.NORMAL, command=b_plus6)  
button_plus6.place(x=775, y=14+50*6, width=20, height=20)

button_plus7 = tk.Button(root, text='+', bg='FireBrick',fg='white', state=tk.NORMAL, command=b_plus7)  
button_plus7.place(x=775, y=14+50*7, width=20, height=20)

button_plus8 = tk.Button(root, text='+', bg='FireBrick',fg='white', state=tk.NORMAL, command=b_plus8)  
button_plus8.place(x=775, y=14+50*8, width=20, height=20)

button_plus9 = tk.Button(root, text='+', bg='FireBrick',fg='white', state=tk.NORMAL, command=b_plus9)  
button_plus9.place(x=775, y=14+50*9, width=20, height=20)

button_plus10 = tk.Button(root, text='+', bg='FireBrick',fg='white', state=tk.NORMAL, command=b_plus10)  
button_plus10.place(x=775, y=14+50*10, width=20, height=20)

button_start = tk.Button(root, text='確認', bg='Maroon',fg='white', state=tk.NORMAL, command=b_start)  
button_start.place(x=740, y=14+50*11, width=60, height=30) 
#------------------------------------------------------------------------------------------------------------------------
root.mainloop()