import os
import cv2   #open cv 把影像讀成矩陣
import numpy as np
import pandas as pd 
from os import listdir
import matplotlib.pyplot as plt

from tensorflow.keras.applications.resnet50 import ResNet50   #主角
from keras.preprocessing.image import ImageDataGenerator  #根據原有資料生成假資料 eg旋轉圖片
from sklearn.model_selection import train_test_split  #劃分訓練、測試
from keras.utils import np_utils
import tensorflow as tf
from keras.layers import Dense, Flatten, Conv2D ,MaxPooling2D,Dropout
print("+-+-+-+-+-+-+-+-+-")

# 資料路徑
PATH = r'C:\Users\Tosha.E.T\Desktop\dataset'

# 圖片大小
IMAGE_SIZE = (224,224)

# 辨識類別數
NUM_CLASSES = 3

# 凍結層數
FREEZE_LAYERS = 200

# EPOCH次數
EPOCH = 5

# 批次量
BATCH_SIZE = 32

# 學習率
LEARNING_RATE = 0.001

# 儲存路徑
WEIGHTS_SAVING = 'resnet50-final-8.h5'

dict_hot = {'AesculusCalifornica':0,'ErodiumSp':1,'MagnoliaGrandiflora':2}  #對類別做編碼
label = []
label_hot = []
images = []

for i in listdir(os.path.join(PATH,'Train')):
    # 讀取圖片類別
    class_name = i[:i.index("_")]
    label.append(class_name)
    label_hot.append(dict_hot[class_name])
    
    # 讀取圖片&resize
    img = cv2.imread(os.path.join(PATH,'Train',i))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, IMAGE_SIZE, interpolation=cv2.INTER_LINEAR)
    images.append(np.array(img))
print("Loading Complete\n")
    
images = np.array(images) 
label_hot = np.array(label_hot)

print("images.shape={} , label_hot.shape=={}\n".format(images.shape, label_hot.shape))

# Training Data 80%
(trainData, valiData, trainLabels, valiLabels) = train_test_split(images, label_hot, test_size=0.2, random_state=42)

print("trainData records: {}".format(len(trainData)))
print("valiData records: {}".format(len(valiData)))
print("trainData.shape={} trainLabels.shape={}".format(trainData.shape, trainLabels.shape))
print("valiData.shape={} valiLabels.shape={}\n".format(valiData.shape, valiLabels.shape))

# One hot encoding
trainLabels_hot = np_utils.to_categorical(trainLabels)
valiLabels_hot = np_utils.to_categorical(valiLabels)
print("One hot encoding matrix shape (Train):{}".format(trainLabels_hot.shape))
print("One hot encoding matrix shape (Val):{}\n".format(valiLabels_hot.shape))

print("*************************")

datagen = ImageDataGenerator(
    rescale=1.0/255.0,)

datagen.fit(trainData)
train_generator = datagen.flow(trainData, trainLabels_hot, shuffle=True, batch_size = BATCH_SIZE)
val_generator = datagen.flow(valiData, valiLabels_hot, shuffle=True, batch_size = BATCH_SIZE)

# 獲得Pre-trained model(使用ResNet50)
Pretrained_model = ResNet50(include_top=False, weights='imagenet', input_tensor=None, input_shape=(IMAGE_SIZE[0],IMAGE_SIZE[1],3))

# 最後一層FC層攤平
x = Pretrained_model.layers[-1].output
x = Flatten()(x)