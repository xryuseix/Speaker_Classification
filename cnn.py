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
        epochs = 50
        train_x, train_y, test_x, test_y, data = self.load_data(num_classes)
        model = self.make_model(num_classes)
        self.summary(model)
        
        model, csv_logger, es = self.compile(model)
        hist = self.learn(model,
                          train_x, train_y,
                          batch_size, epochs,
                          es, csv_logger)
        self.evaluate(model, test_x, test_y)
        self.show_graph(hist)
        
    def load_data(self, num_classes):
        print("======= LOAD DATA =======")
        train_x, train_y, test_x, test_y, data = wav_io.build_source()
        train_x = np.reshape(train_x, (num_classes * int(data * 0.8), -1)).astype('float32')
        test_x = np.reshape(test_x, (num_classes * int(data * 0.2), -1)).astype('float32')
        train_y = keras.utils.to_categorical(train_y, num_classes)
        test_y = keras.utils.to_categorical(test_y, num_classes)
        return train_x, train_y, test_x, test_y, data

    def add_white_noise(self, x, rate=0.002):
        return x + rate*np.random.randn(len(x))

    def shift_sound(self, x, rate=2):
        return np.roll(x, int(len(x)//rate))

    def stretch_sound(self, x, rate=1.1):
        input_length = len(x)
        x = librosa.effects.time_stretch(x, rate)
        if len(x)>input_length:
            return x[:input_length]
        else:
            return np.pad(x, (0, max(0, input_length - len(x))), 'constant')

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

    def learn(self, model, train_x, train_y, batch_size, epochs, es, csv_logger):
        print("======= LEARNING =======")
        hist = model.fit(train_x, train_y,
                 batch_size=batch_size,
                 epochs=epochs,
                 verbose=1,
                 validation_split=0.1,
                 callbacks=[es, csv_logger])
        return hist

    def evaluate(self, model, test_x, test_y):
        print("======= EVALUATE =======")
        score = model.evaluate(test_x, test_y, verbose=0)
        print('test loss:', score[0])
        print('test acc:', score[1])

    def show_graph(self, hist):
        print("======= SHOW GRAPH =======")
        loss = hist.history['loss']
        val_loss = hist.history['val_loss']
        epochs = len(loss)
        plt.plot(range(epochs), loss, marker='.', label='loss(training data)')
        plt.plot(range(epochs), val_loss, marker='.', label='val_loss(evalution data)')
        plt.legend(loc='best')
        plt.grid()
        plt.xlabel('epoch')
        plt.ylabel('loss')
        plt.show()

    def predict(self):
        print("======= PREDICT =======")
        # arr = np.reshape([[0, 0],[0, 1],[1, 0],[1, 1]], (4, -1))
        # print(model.predict(arr))
