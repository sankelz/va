import webbrowser as w
import datetime
import pyttsx3

engine = pyttsx3.init()

def spotify():
    w.open('https://open.spotify.com/?flow_ctx=aaa0d6de-5fca-4408-be20-ea4670db8813%3A1693622995', new = 1)

def youtube():
    w.open('https://www.youtube.com/', new = 1)

def google():
    w.open('https://www.google.com/', new = 1)

def netflix():
    w.open('https://www.netflix.com/browse', new = 1)

def twitter():
    w.open('https://twitter.com/home?lang=en', new = 1)

def tophat():
    w.open('https://app.tophat.com/e/624716/lecture/', new = 1)

def telldatetime():
    nowrl = datetime.datetime.now()
    nowrlsaid = nowrl.strftime("%B %d %Y %I:%M %p")
    engine.say(f'it is {nowrlsaid}')
    engine.runAndWait()