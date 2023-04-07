#python youbike2.py
import os
from os import listdir
import numpy as np 
import pandas as pd
import  json, ssl, urllib.request
from os import listdir


url = 'https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json'
context = ssl._create_unverified_context()

with urllib.request.urlopen(url, context=context) as jsondata:
    #將JSON進行UTF-8的BOM解碼，並把解碼後的資料載入JSON陣列中
     data = json.loads(jsondata.read().decode('utf-8-sig')) 


station=[]
for i in data:
    station.append([i["sna"],
                   i["lat"],
                   i["lng"]])

np_station = np.array(station)


data=pd.DataFrame(index=station, columns=["Name", "LAT", "LON"])
data.to_csv("myBike2Data.csv", encoding="utf-8-sig")

film="myBike2Data.csv"



data_path=r"C:\Users\Tosha.E.T\Documents\ArcGIS\Projects\yb2"
output_path=r"C:\Users\Tosha.E.T\Documents\ArcGIS\Projects\yb2"


input_x = 121.5495
input_y = 25.0169
data = pd.DataFrame({
        "lat": [input_y],
        "lon": [input_x]
    })
data.to_csv("my_point.csv")


arcpy.management.XYTableToPoint(r"C:\Users\Tosha.E.T\Documents\ArcGIS\Projects\yb2\myBike2Data.csv",
                                r"C:\Users\Tosha.E.T\Documents\ArcGIS\Projects\yb2\points.shp",
                                'lon', 'lat',
                                '#',
                                arcpy.SpatialReference(4326))


arcpy.management.XYTableToPoint(r"C:\Users\Tosha.E.T\python\my_point.csv",                                # a function in arcgis
                                r"C:\Users\Tosha.E.T\python\my_point.shp",
                                'lon', 'lat',
                                '#',
                                arcpy.SpatialReference(4326))


arcpy.analysis.Buffer(r"C:\Users\Tosha.E.T\python\my_point.shp", 
                      r"C:\Users\Tosha.E.T\Documents\ArcGIS\Projects\yb2\my_point_buffer.shp",
                       "500 Meter",)





arcpy.management.XYTableToPoint(r"C:\Users\Tosha.E.T\Documents\ArcGIS\Projects\水庫krigging\krigging.csv",
                                r"C:\Users\Tosha.E.T\Documents\ArcGIS\Projects\水庫krigging\南化XY.shp",
                                'X', 'Y',
                                '#',
                                arcpy.SpatialReference(4326))