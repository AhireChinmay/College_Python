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
intents = json.loads(open('intents.json').read())

for i in intents['intents']:
    for j in i['patterns']:
        print(j)
    
        