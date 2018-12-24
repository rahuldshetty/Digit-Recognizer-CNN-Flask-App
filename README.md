# Digit Recognition Convolutional Neural Network in Python/Flask App

This is a demo project to show how we can make use of CNN to classify a written digit.

You can test the demo of this project over here: (https://digitcnn.herokuapp.com/)

## Getting Started

1. Clone the repos into your system.
2. Install the dependencies from requirements.txt by using pip
3. Run the server by using "python server.py" command
   Note: You can use a 28x28 samples to train more data by using "train and save.py"
4. By default the host address is set to "0.0.0.0" , change this to any desired in your "server.py" file 
5. Open the browser and go to the desired address.

### Prerequisites

Python 3
Opencv
keras 
tensorflow (backend for keras)
flask
numpy
h5py
Pillow
pybase64
python-resize-image

```
To install a dependency pybase64 , use the following command: "pip install pybase64"
```

## Screenshots
![1](https://raw.githubusercontent.com/rahuldshetty/Digit-Recognizer-CNN-Flask-App/master/snap1.PNG)
![2](https://raw.githubusercontent.com/rahuldshetty/Digit-Recognizer-CNN-Flask-App/master/snap2.PNG)
![3](https://raw.githubusercontent.com/rahuldshetty/Digit-Recognizer-CNN-Flask-App/master/snap3.PNG)
![4](https://raw.githubusercontent.com/rahuldshetty/Digit-Recognizer-CNN-Flask-App/master/snap4.PNG)

## Model Used
Below model design was used to construct the Neural network.
![Model Architechrure](https://cdn-images-1.medium.com/max/1255/1*XbuW8WuRrAY5pC4t-9DZAQ.jpeg)
Picture Reference from:(https://medium.com/@RaghavPrabhu/understanding-of-convolutional-neural-network-cnn-deep-learning-99760835f148)


