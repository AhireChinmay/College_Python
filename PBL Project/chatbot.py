import random
import numpy as np
import pickle
import json
import speech_recognition
import pyttsx3
import nltk
from nltk.stem import WordNetLemmatizer

import tensorflow as tf
tf.compat.v1.disable_eager_execution()
from keras.models import load_model

lemmatizer = WordNetLemmatizer()
intents = json.loads(open('intents.json').read())
words = pickle.load(open('words.pkl','rb'))
classes = pickle.load(open('classes.pkl','rb'))
model = load_model('chatbot_model.h5')

engine = pyttsx3.init()
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voices',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    

def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word) for word in sentence_words]
    return sentence_words 

def bag_of_words(sentence):
    sentence_words = clean_up_sentence(sentence)
    bag = [0]*len(words)
    for w in sentence_words:
        for i, word in enumerate(words):
            if word==w:
                bag[i]=1
    return np.array(bag)

def predict_class(sentence):
    bow = bag_of_words(sentence)
    res = model.predict(np.array([bow]))[0]
    ERROR_THRESHOLD =0.25
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]
    
    results.sort(key= lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({'intent': classes[r[0]], 'probability': str(r[1])})
        return return_list

def get_resonse(intents_list, intents_json):
    tag = intents_list[0]['intent']
    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if i['tag']==tag:
            result = random.choice(i['responses'])
            break
    return result

print('This chatbot is running')
speak('Chatbot is running')

# THIS IS THE SPPEECH RECOGNITION CODE 
# recognizer = speech_recognition.Recognizer()
# for i in range(10):
#     try:
#         with speech_recognition.Microphone() as mic:
#             recognizer.adjust_for_ambient_noise(mic,duration=0.1)
#             audio = recognizer.listen(mic)

#             text = recognizer.recognize_google(audio)
#             text = text.lower()
#             print(f"Recognised:- {text}")

#     except speech_recognition.UnknownValueError():
#         recognizer = speech_recognition.Recognizer()
        


while True:
    message = input("-->>")
    ints = predict_class(message)
    # ints = predict_class(text)
    res = get_resonse(ints, intents)
    print(res)
    speak(res)    
    




