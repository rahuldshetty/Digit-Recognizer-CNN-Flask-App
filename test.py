import numpy as np
import pandas as pd

from keras.models import Sequential
from keras.models import load_model
from keras.layers import Dense, Conv2D, Flatten,MaxPool2D
from keras.utils.np_utils import to_categorical
from keras.models import load_model
import keras

import cv2

df=pd.read_csv('data.csv').values
x=df[0,1:]
img=x.reshape(28,28)

cv2.imwrite('a.jpg',img)

x=x.reshape(1,28,28,1)
model=load_model('my_model.h5')
print(model.predict(x))


