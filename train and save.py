import pandas as pd
import numpy as np

from keras.models import Sequential
from keras.models import load_model
from keras.layers import Dense, Conv2D, Flatten,MaxPool2D

from keras.utils.np_utils import to_categorical
import keras


df=pd.read_csv('data.csv').values

SPLIT=75*len(df)//100 

x=df[0:SPLIT,1:]
yo=df[0:SPLIT,0]
x=x.reshape(x.shape[0],28,28,1)
y=to_categorical(yo)

xtest=df[SPLIT:,1:]
xtest=xtest.reshape(xtest.shape[0],28,28,1)
ytesto=df[SPLIT:,0]
ytest=to_categorical(ytesto)



input_shape=x.shape
num_classes=10

model = Sequential()
model.add(Conv2D(filters = 32,kernel_size = (3,3),input_shape = (28,28,1),activation = 'relu',padding = 'same'))
model.add(MaxPool2D((2,2)))
model.add(Conv2D(filters = 64,kernel_size = (3,3),padding = 'same',activation = 'relu'))
model.add(MaxPool2D(2,2))
model.add(Conv2D(64,kernel_size = (3,3),padding = 'same',activation = 'relu'))

model.add(Flatten())
model.add(Dense(64,activation = 'relu'))

model.add(Dense(10,activation = 'softmax'))

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
model.fit(x, y, validation_data=(xtest, ytest), epochs=3)

model.save('my_model.h5')
