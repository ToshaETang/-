import arcpy

inTable=arcpy.GetParameterAsText(0)          #第一個欄位
X_coord=arcpy.GetParameterAsText(1)
Y_coord=arcpy.GetParameterAsText(2)
Z_coord=arcpy.GetParameterAsText(3)
coord=arcpy.GetParameterAsText(4)
out_feature_class=arcpy.GetParameterAsText(5)
distence=arcpy.GetParameterAsText(6)
buffer=arcpy.GetParameterAsText(7)


arcpy.management.XYTableToPoint(inTable,out_feature_class,X_coord,Y_coord,Z_coord,coord)
        #arcpy.management.XYTableToPoint(in_table, out_feature_class, x_field, y_field, {z_field}, {coordinate_system})

arcpy.analysis.Buffer(out_feature_class,buffer,distence)
        #arcpy.analysis.Buffer(in_features, out_feature_class, buffer_distance_or_field, {line_side}, {line_end_type}, {dissolve_option}, {dissolve_field}, {method})
