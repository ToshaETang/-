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

import matplotlib.pyplot as plt#@@@@@@@@@@@@@@@@@@2
from matplotlib.backend_bases import key_press_handler#@@@@@@@@@@@@@@@@@@22
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk#@@@@@@@@@@@@@@
from matplotlib.figure import Figure
 
#----去掉紅色警告-------
from sklearn import metrics
import warnings
warnings.filterwarnings("ignore")

root0 = Tk()
root0.minsize(1300, 700)
root0.title('try')
#-----------------------------------

# cv = Canvas(root0,bg = 'white')
# cv.place(x=0,y=0, width=1300, height=400)

File = filedialog.askopenfilename(title='選擇原始檔案', filetypes=[('csv', '*.csv')])
df = pd.read_csv(r'{}'.format(File))
df=df[df['distance1']>25]
df=df[df['distance1']<45]
df=df.reset_index()

i = 1
while i<(len(df["distance1"])-1):
    a = df["distance1"][i-1]
    b = df["distance1"][i]
    c = df["distance1"][i+1]
    if (abs(b-c)+abs(a-b))/2>abs(c-a)*1.5:
        df["distance1"][i] = (a+c)/2
        i=i+1
    else:
        i=i+1

plt.figure(figsize=(10,5),dpi=100)
T = df.datetime
D = df.distance1
plt.plot(T,D)
plt.show()

# ##########

# df01.to_csv(r'C:\Users\Tosha.E.T\Desktop\Sinotech\816\濾過\{0}-{1}-{2}-d1_clean.csv'.format(m,n,s),index=False)
# print("SAVE!!!")

# # fig = px.line(df01, y='distance1', x=df01.datetime)
# # fig.add_scatter(y=df02['distance1'], x=df02.datetime)
           
# # fig.show()
# # print("{0}-{1}-{2}-d1".format(m,n,s))
# ################################################
# df001 = df12  #改過
# df002 = df12

# # df1 = df1.loc[df1['distance{}'.format(s)]!=20]


# df001=df001[df001['distance2']>20]
# df001=df001[df001['distance2']<100]
# df001 = df001.reset_index()
# i = 1
# while i<(len(df001["distance2"])-1):
#     a = df001["distance2"][i-1]
#     b = df001["distance2"][i]
#     c = df001["distance2"][i+1]
#     if (abs(b-c)+abs(a-b))/2>abs(c-a)*1.5:
#         df001["distance2"][i] = (a+c)/2
#         i=i+1
#     else:
#         i=i+1

# df001.to_csv(r'C:\Users\Tosha.E.T\Desktop\Sinotech\816\濾過\{0}-{1}-{2}-d2_clean.csv'.format(m,n,s),index=False)
# print("SAVE!!!")

# # fig2 = px.line(df001, y='distance2', x=df001.datetime)
# # fig2.add_scatter(y=df002['distance2'], x=df002.datetime)
           
# # fig2.show()
# # print("{0}-{1}-{2}-d2".format(m,n,s))
# ##########3


#----------------------------
root0.mainloop()