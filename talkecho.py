import speech_recognition as sr
import pyttsx3

r = sr.Recognizer()
engine = pyttsx3.init()

def spokenword(dialogue):
    engine.say(dialogue)
    engine.runAndWait()

def transact():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=0.2)
        audio = r.listen(source)
        try:
            words = r.recognize_google(audio)
            words = words.lower()
            return words 
        except sr.UnknownValueError:
            engine.say("I didn't catch that")
            engine.runAndWait()

def commandhere(words):
    while True:
        try:
            spokenword("Someone wants to tell you that..." + str(words))
            return  
        except sr.RequestError as error:
            spokenword("I wasn't able to translate that bit of the dialogue, sorry.")

def talking(words):
    engine.say("say what you wanna say!")
    engine.runAndWait()
    command = transact()
    commandhere(words=command)
    exit()
