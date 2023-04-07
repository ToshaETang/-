# python INSGPU.py
import numpy as np
from keras.layers import Dense, Input
from keras import Model
from keras.utils import plot_model
from keras.optimizers import adam



inputs = Input(shape=(784,))
x = Dense(64, activation="relu")(inputs)
x1 = Dense(64, activation="relu")(x)
outputs = Dense(10, activation="softmax")(x1)
model = Model(inputs=inputs, outputs=outputs, name="mnist_model")


model.compile(optimizer = adam(lr=0.001), loss='categorical_crossentropy', metrics=['accuracy'])


model.summary()
model.save("AAA.h5")








