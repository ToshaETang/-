import os
from os import listdir
#import arcpy

data_path = r"C:\Users\Tosha.E.T\Documents\ArcGIS\Projects\5.3\5.3data"
output_path = r"C:\Users\Tosha.E.T\Documents\ArcGIS\Projects\5.3"

for i in listdir(data_path):
    #path = data_path + r"\\" + i
    start = i.index('_') + 1
    end = i.index('.')


    path = os.path.join(data_path, i)   #join: 套件
    filename = "device_point_{}.shp".format(528)
    output_path2 = os.path.join(output_path, filename)

    #data = pd.read_cvs(path)    panda


    arcpy.management.XYTableToPoint(path,
                                    output_path,
                                    'lon', 'lat',
                                    '#',
                                    arcpy.SpatialReference(4326))


    print("{} compelet".format(i))


my_list = []
for i in listdir(output_path):
    suffix = ".shp"
    if i.endswith(suffix):
        my_path = os.path.join(output_path, i)
        my_list.append(i)



# my_list = [i for i in listdir(output_path) if i.endswith(".shp")]


arcpy.management.Merge(my_list, os.path.join(output_path, total_device_point.shp))



import pandas as pd

input_x = 121.5
input_y = 25

data = pd.DateFrame({
            "lat": [input_y],
            "lon": [input_x]
        })


data.to_cvs("my_point.cvs")

arcpy.management.XYTableToPoint(path,
                                os.path.join(output_path, "my_pnt.shp"),
                                'lon', 'lat',
                                '#',
                                arcpy.SpatialReference(4326))


arcpy.analysis.Buffer(in_features, 
                      out_feature_class, 
                      "10000 Meters")

arcpy.analysis.Clip(in_features, 
                    clip_features, 
                    out_feature_class)


#用pandas把結果轉換csv   .dbf --> .csv 可直接用
