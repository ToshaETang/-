#python ap.py
import os
from os import listdir


data_path=r"C:\Users\Tosha.E.T\Documents\ArcGIS\Projects\5.3\5.3data"
output_path=r"C:\Users\Tosha.E.T\Documents\ArcGIS\Projects\5.3"

#input
for i in listdir(data_path):
    path=os.path.join(data_path, i)
    filename = "device_point_{}.shp".format(i[i.index('_') + 1 : i.index('.')])      # _1024.  取 _ 後面一位 到 . 之前的東西
    out_path = os.path.join(output_path, filename)
    arcpy.management.XYTableToPoint(path,                                # a function in arcgis
                                    out_path,
                                    'lon', 'lat',
                                    '#',
                                    arcpy.SpatialReference(4326))
    print("{} complete".format(i))



    #print(out_path)



'''


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
'''
