from flask import *
from os import environ
import pybase64 as base64
import numpy as np
import cv2
from PIL import Image
import io
from keras.models import load_model
import re
from resizeimage import resizeimage
from keras.models import Sequential
from keras.models import load_model
from keras.layers import Dense, Conv2D, Flatten,MaxPool2D
from keras.utils.np_utils import to_categorical
import keras

app = Flask(__name__)



@app.route("/")
def hello():
    return render_template('index.html')

@app.route('/find',methods=['POST'])
def hola():
    
    if request.method=='POST':
        data = (request.form['urwa'])
        data = data.replace("data:image/png;base64,", "")
        imgdata = base64.b64decode(data)
        filename = 'canvas_image.png'
        with open(filename, 'wb') as f:
            f.write(imgdata)
        with open(filename, 'r+b') as f:
            with Image.open(f) as image:
                cover=resizeimage.resize_cover(image, [28, 28])
                cover.save('new.jpg', image.format)
                
        open_cv_image  = np.array(Image.open('new.jpg').convert('RGB'))
        open_cv_image = open_cv_image[:, :, ::-1].copy()
        open_cv_image=cv2.cvtColor(open_cv_image,cv2.COLOR_BGR2GRAY)
        data=np.array(open_cv_image)
        img=np.array(data)
        img=img.reshape(1,28,28,1)             
        data=(model.predict(img))
        data=list(data[0])
        ans=data.index(max(data))
        result={}
        result['ans']=str(ans)
        result['data']=data        
        return render_template("result.html",result = result)
       
        
        
    return "ERROR OCCURED..."


model=load_model('my_model.h5')

if __name__ == "__main__":
    app.run(debug=False,host='0.0.0.0',port=environ.get("PORT", 5000),threaded=False)
