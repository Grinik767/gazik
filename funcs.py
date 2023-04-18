from keras import utils
import keras.utils as image
import numpy as np

img_height = 128
img_width = 4096
num_classes = 5
num_classes_def = 2


def okrugl(x):
    return int(x + 0.5)


def color2index(color):
    index = -1
    if 0 <= color[0] <= 50 and 100 <= color[1] <= 159 and 0 <= color[2] <= 50:
        index = 0
    elif 0 <= color[0] <= 50 and 0 <= color[1] <= 50 and 160 <= color[2] <= 255:
        index = 1
    elif 160 <= color[0] <= 255 and 160 <= color[1] <= 255 and 0 <= color[2] <= 50:
        index = 2
    elif 0 <= color[0] <= 50 and 0 <= color[1] <= 50 and 0 <= color[2] <= 50:
        index = 3
    elif 0 <= color[0] <= 50 and 160 <= color[1] <= 255 and 160 <= color[2] <= 255:
        index = 4
    return index


def index2color(index2):
    index = np.argmax(index2)
    color = []
    if index == 0:
        color = [0, 128, 0]
    elif index == 1:
        color = [0, 0, 255]
    elif index == 2:
        color = [255, 255, 0]
    elif index == 3:
        color = [0, 0, 0]
    elif index == 4:
        color = [0, 255, 255]
    return color


def rgbToohe(y, num_classes):
    y2 = y.copy()
    y = y.reshape(y.shape[0] * y.shape[1], 3)
    yt = []
    for i in range(len(y)):
        yt.append(utils.to_categorical(color2index(y[i]), num_classes=num_classes))
    yt = np.array(yt)
    yt = yt.reshape(y2.shape[0], y2.shape[1], num_classes)
    return yt


def yt_prep(data, num_classes):
    yTrain = []
    for seg in data:
        y = image.img_to_array(seg)
        y = rgbToohe(y, num_classes)
        yTrain.append(y)
    return np.array(yTrain)


def color2index_def(color):
    index = 0
    if 200 <= color[0] <= 255 and 0 <= color[1] <= 50 and 0 <= color[2] <= 50: index = 1
    return index


def index2color_def(index2):
    index = np.argmax(index2)
    color = []
    if index == 0:
        color = [0, 128, 0]
    elif index == 1:
        color = [255, 0, 0]
    return color


def rgbToohe_def(y, num_classes):
    y2 = y.copy()
    y = y.reshape(y.shape[0] * y.shape[1], 3)
    yt = []
    for i in range(len(y)):
        yt.append(utils.to_categorical(color2index_def(y[i]), num_classes=num_classes))
    yt = np.array(yt)
    yt = yt.reshape(y2.shape[0], y2.shape[1], num_classes)
    return yt


def yt_prep_def(data, num_classes):
    yTrain = []
    for seg in data:
        y = image.img_to_array(seg)
        y = rgbToohe_def(y, num_classes)
        yTrain.append(y)
    return np.array(yTrain)
