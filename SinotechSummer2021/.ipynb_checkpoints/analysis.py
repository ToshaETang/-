from os import listdir
from os.path import isfile, isdir, join
import pandas as pd
import numpy as np
import os
import os.path
import datetime
from os import listdir

def erosion_analysis(folderPath):
    filepath_ero=[]
    filepath_rain=[]
    filepath_stastic=[]
    for i in range(len(listdir(folderPath))):
        fil=folderPath+'\{}/01.filter_data'.format(i+1)
        rain=folderPath+'\{}/02.rain_data'.format(i+1)
        sta=folderPath+'\{}/03.stastic'.format(i+1)
        filepath_ero.append(fil)
        filepath_rain.append(rain)
        filepath_stastic.append(sta)
    rain_data=[]
    for n in range(len(filepath_stastic)):
        for root,dirs,files in os.walk(filepath_rain[n]): 
            for k in files:
                rain_data.append(os.path.join(root,k))
        #print(rain_data)
        #print('==========================')
        ero_data=[]
        for root,dirs,files in os.walk(filepath_ero[n]):
            for k in files:
                ero_data.append(os.path.join(root,k))

        for i in range(len(rain_data)):
            rain = pd.read_excel((rain_data[i]))


            for i in range(len(rain)):
                rain.S_time[i]=datetime.datetime.strptime (rain.S_time[i], "%Y/%m/%d %H:%M")
                rain.E_time[i]=datetime.datetime.strptime (rain.E_time[i], "%Y/%m/%d %H:%M")
            for j in range(len(ero_data)):
                ero= pd.read_csv((ero_data[j]))

                name = os.path.split(ero_data[j])[1][0:-13]
                print('開始分析'+name)
                for i in range(len(ero)):
                    ero.time[i]=datetime.datetime.strptime (ero.time[i], "%Y-%m-%d %H:%M:%S")
                    #%Y-%m-%d %H:%M:%S
                rain=rain.drop(rain.loc[rain.E_time<=ero.time[0]].index).reset_index(drop=True)
                print("監測期間內共有{}場降雨".format(len(rain)))
                Erosion_s = []
                Erosion_e = []
                time_record=[]
                for k in range(len(ero.time)):
                    for w in range(len(rain)):                        
                        k=2
                        while k<len(ero.time):

                            if ero.time[k] > rain.S_time[w]:                       
                                #print("下雨開始時間是 "+str(rain.S_time[w]))
                                #print("地表高程紀錄時間是 "+str(ero.time[k-2]))
                                #print(str(k-1)+' 找到沖蝕開始時間了!'+str(df1.created_at[k-1])+'沖蝕深度為'+str(df1.mean_new[k-1]))                       
                                Erosion_s.append(ero.trend[k-2].round(2))
                                while k<len(ero.time):
                                    if  ero.time[k]> rain.E_time[w]:  
                                        #print("下雨結束時間是 "+str(rain.E_time[w]))
                                        #print("地表高程紀錄時間是 "+str(ero.time[k]))

                                        Erosion_e.append(ero.trend[k].round(2))

                                        time_record.append(rain.E_time[w])
                                        print("第{}場降雨分析完成".format(w+1))
                                        #print(str(k)+' 找到沖蝕結束時間了!'+str(df1.created_at[k])+'沖蝕深度為'+str(df1.mean_new[k]))
                                        #print('我要break囉')                           
                                        break
                                    else:                       
                                        #print('繼續找結束時間....')
                                        k+=1

                                break
                            else:
                                k+=1
                                #print('我要+1囉')
                        #print(str(w)+' is done')

                        continue                       
                    #print("第{}處分析完成".format(name[j]))
                    break
                d= {'Erosion_start':Erosion_s,               
                    'Erosion_end':Erosion_e,
                    'E_time':time_record}
                cc=pd.DataFrame(d)
                cc['E_time']=cc['E_time'].astype('datetime64[ns]')
                rain['E_time']=rain['E_time'].astype('datetime64[ns]')

                rain_all = pd.merge(rain,cc,on='E_time').drop(['index','Unnamed: 0'],axis=1)
                rain_all['Erosion']=rain_all['Erosion_end']-rain_all['Erosion_start']
                rain_all.to_excel(filepath_stastic[n] + "\\"+ name+"_沖蝕分析.xls")
                print('============資料儲存在  '+filepath_stastic[n]+'  ================')
