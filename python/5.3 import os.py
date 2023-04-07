import os
from os import listdir


data_path = r"C:\Users\Tosha.E.T\Documents\ArcGIS\Projects\5.3\5.3data"

for i in listdir(data_path):
    #path = data_path + r"\\" + i
    
    path = os.path.join(data_path, i)   #join: 套件

    #data = pd.read_cvs(path)    panda
    print(path)
