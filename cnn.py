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
        batch_size = 128
        num_classes = 8
        epochs = 20
        train_x, train_y, test_x, test_y = self.load_data(num_classes)
        
        model = self.make_model(num_classes)
        self.summary(model)
        
        model, es, csv_logger = compile(model)
        hist = self.learn(model,
                          x_train, y_train,
                          batch_size, epochs,
                          es, csv_logger)
        
    def load_data(self, num_classes):
        print("======= LOAD DATA =======")
        train_x, train_y, test_x, test_y = wav_io.build_source()
        train_x = np.reshape(train_x, (num_classes * 40, -1))
        test_x = np.reshape(test_x, (num_classes * 10, -1))
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
        return model

    def summary(self, model):
        print("======= SUMMARY =======")
        model.summary()

    def compile(self, model):
        print("======= COMPILE =======")
        model.compile(loss='categorical_crossentropy',
                      optimizer=Adam(),
                      metrics=['accuracy'])
        es = EarlyStopping(monitor='val_loss', patience=2)
        csv_logger = CSVLogger('training.log')
        return model, es, csv_logger

    def learn(self, model, x_train, y_train, batch_size, epochs, es, csv_logger):
        print("======= LEARNING =======")
        hist = model.fit(x_train, y_train,
                 batch_size=batch_size,
                 epochs=epochs,
                 verbose=1,
                 validation_split=0.1,
                 callbacks=[es, csv_logger])
        return hist

    def evaluate(self):
        print("======= EVALUATE =======")

    def show_graph(self):
        print("======= SHOW GRAPH =======")

    def predict(self):
        print("======= PREDICT =======")
