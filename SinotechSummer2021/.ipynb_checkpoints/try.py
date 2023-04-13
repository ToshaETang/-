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
from datetime import datetime, timezone

r = time.localtime()
result = time.strftime("%Y-%m-%d %I:%M:%S", r)
rr = result.replace(tzinfo='UTC')
print(result)
print(rr)




#python 定時抓資料.py

#cd C:\TET\SinotechSummer\.ipynb_checkpoints
#python GUI.py
#python try_篩資料.py
#python GUI_2.py
#python GUI_2_備份.py
#python Untitled-1.py
#python try.py

#python GUI_氣象局.py