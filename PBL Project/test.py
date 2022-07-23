
import json

from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer
intents = json.loads(open('intents.json').read())

for i in intents['intents']:
    for j in i['patterns']:
        print(j)
    
        