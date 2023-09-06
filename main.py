import speech_recognition as sr
import pyttsx3
import time
import tkinter.messagebox as tkMessageBox
import tkinter as tk

import partymode 
from partymode import *

import arduinostuff
from arduinostuff import *

import datetime

import reminders 
from reminders import *

import talkecho
from talkecho import *

r = sr.Recognizer()
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) 

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

def partymoder(words):
            if words == "spotify" or words == "open spotify":
                spotify()
            elif words == "youtube" or words == "open youtube":
                youtube()
            elif words == "netflix" or words == "open netflix":
                netflix()
            elif words == "google" or words == "open google":
                google()
            elif words == "twitter" or words == "open twitter":
                 twitter()
            elif words == "tell the time" or words == "tell the date":
                telldatetime()
            elif words == "gmail" or words == "open gmail":
                 gmail()
            elif words == "docs" or words == "open docs":
                 docs()
            elif words == "outlook" or words == "mail" or words == "open outlook mail":
                 outlookmail()
            elif words == "brightspace" or words == "U.B. Learns" or words == "open brightspace":
                 brightspace()
            elif words == "arduino" or words == "open arduino":
                 arduino()
            elif words == "reminder" or words == "set up a reminder" or words == "leave a reminder":
                spokenword("so in how much time do you want this reminder? give me a number.")
                inq1 = "so in how much time do you want this reminder? give me a number. "
                var1 = int(input(inq1))
                time.sleep(1)
                spokenword("in hours, minutes, or seconds?")
                var2 = transact()
                if var2 == "hours":
                    timegiven = int(var1) * 3600
                elif var2 == "minutes":
                    timegiven = int(var1) * 60
                elif var2 == "seconds":
                    timegiven = int(var1)
                time.sleep(1)
                spokenword("and why do you need the reminder?")
                inq3 = "and why do you need the reminder? "
                var3 = input(inq3)
                time.sleep(1)
                spokenword("ok, give me a second.")
                leaveamessage(alert=var3,timegiven=timegiven)
            elif words == "talk" or words == "echo":
                 talking(words)
            elif words == "stats" or words == "top hat" or words == "stats attendance":
                 tophat()
            
def commanding(words):
    while True:
        try:
            spokenword("You want me to..." + str(words) + "right? Give me a second.")
            partymoder(words)  
            return  
        except sr.RequestError as error:
            print("I can't do that right now, sorry".format(error))

engine.say("hi dude what's up?")
engine.runAndWait()
command = transact()
commanding(words=command)
exit()
