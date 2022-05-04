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
words = []
classes = []
documents = []
ignore_letters = ['!', ',', '?', '.', '$']

for intent in intents['intents'] :
    for pattern in intents['patterns']:
        word_list = nltk.tokenize(pattern)
        words.append(word_list)
        documents.append((word_list, intents['tag']))
        if intents['tag'] not in classes:
            classes.append(intents['tag'])
        
print(documents)

