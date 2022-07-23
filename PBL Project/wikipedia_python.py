import wikipedia
import pyttsx3

engine =pyttsx3.init()
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voices',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

text = input("Search on wikipedia: ")

result = wikipedia.summary(text, sentences=2)
print(result)
speak(result)


