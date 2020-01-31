import keras
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation
from keras.optimizers import Adam
from keras.callbacks import EarlyStopping, CSVLogger

import matplotlib.pyplot as plt
import numpy as np

import wav_io

class CNN():
    def __init__(self):
        print("======= START CNN =======")
        train_x, train_y, test_x, test_y = self.load_data(num_classes)
        batch_size = 128
        num_classes = 8
        epochs = 20
        
    def load_data(self, num_classes):
        print("======= LOAD DATA =======")
        train_x, train_y, test_x, test_y = wav_io.build_source()

        train_x = np.reshape(320, -1)
        test_x = np.reshape(80, -1)
        train_y = keras.utils.to_categorical(train_y, num_classes)
        test_y = keras.utils.to_categorical(test_y, num_classes)

        return train_x, train_y, test_x, test_y

    def make_model(self, num_classes):
        print("======= MAKE MODEL =======")
        model = Sequential()
        model.add(Dense(512, input_shape=(36, )))
        model.add(Activation('relu'))
        model.add(Dropout(0.4))
        model.add(Dense(512))
        model.add(Activation('relu'))
        model.add(Dropout(0.4))
        model.add(Dense(num_classes))
        model.add(Activation('softmax'))

    def summary(self):
        print("======= SUMMARY =======")

    def compile(self):
        print("======= COMPILE =======")

    def learn(self):
        print("======= LEARNING =======")

    def evaluate(self):
        print("======= EVALUATE =======")

    def show_graph(self):
        print("======= SHOW GRAPH =======")

    def predict(self):
        print("======= PREDICT =======")
