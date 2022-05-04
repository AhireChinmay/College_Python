import random
import numpy as np
import json
import pickle

import nltk
from nltk.stem import WordNetLemmatizer


from keras.models import Sequential
from keras.layers import Dense,Activation,Dropout
from keras.optimizer_v1 import SGD
from pyparsing import Word

lemmatizer = WordNetLemmatizer
f = open('intents.json')
intents = json.load(f)

for i in intents['intents']:
    print(i)
    
        