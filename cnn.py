import keras
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation
from keras.optimizers import Adam
from keras.callbacks import EarlyStopping, CSVLogger

import matplotlib.pyplot as plt
from tqdm import tqdm
import numpy as np
import librosa

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
    
    def add_white_noise(self, x, rate=0.002):

        add = rate*np.random.randn(len(x))
        for i in x:
            i += add;
        return x

    def add_shift_sound(self, x, rate=2):
        rate = 2 * np.random.rand() + 1
        return np.roll(x, int(len(x)//rate))

    def add_stretch_sound(self, x, rate=1.1):
        rate = (1.3 - 0.7) * np.random.rand() + 0.7
        input_length = len(x)
        x = librosa.effects.time_stretch(x, rate)
        if len(x)>input_length:
            return x[:input_length]
        else:
            return np.pad(x, (0, max(0, input_length - len(x))), 'constant')
    
    def load_data(self, num_classes):
        print("======= LOAD DATA =======")
        train_x, train_y, test_x, test_y, data = wav_io.build_source()
        train_x = np.reshape(train_x, (num_classes * int(data * 0.8), -1)).astype('float32')
        test_x = np.reshape(test_x, (num_classes * int(data * 0.2), -1)).astype('float32')

        double = 5; # ノイズのかさ増し量
        noises = np.empty(0)

        for d in tqdm(range(0,double)):
            # ノイズを追加
            for n, (i, j) in enumerate(zip(train_x,train_y)):
                if False:
                    noises = self.add_white_noise(i)
                else:
                    noises = np.concatenate([noises,self.add_white_noise(i)])
                train_y.append(j)
                noises = np.concatenate([noises,self.add_shift_sound(i)])
                train_y.append(j)
                noises = np.concatenate([noises,self.add_stretch_sound(i)])
                train_y.append(j)

        noises = np.reshape(noises, (3 * double * num_classes * int(data * 0.8), -1)).astype('float32')
        train_y = keras.utils.to_categorical(train_y, num_classes)
        test_y = keras.utils.to_categorical(test_y, num_classes)
        print(noises.size)
        train_x = np.concatenate([train_x,noises])
        return train_x, train_y, test_x, test_y, data

    

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
