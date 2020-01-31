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
        
    def load_data(self):
        print("======= LOAD DATA =======")

    def make_model(self):
        print("======= MAKE MODEL =======")

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
