import time
from datetime import datetime, timedelta
import webbrowser as w
import tkinter.messagebox as tkMessageBox
import tkinter as tk

def leaveamessage(alert, timegiven):
    x = tkMessageBox.showinfo(title="Reminder", message=(f'You needed this to remind you of {alert}'))
    time.sleep(timegiven)
    return x 

def docs():
    w.open('https://docs.google.com/document/d/1scSaszGMqsG3M9DT-2OfV7U9LDQqttPCRGx6GMkLYo8/edit', new = 1)
    
def brightspace():
    w.open('https://ublearns.buffalo.edu/d2l/home', new = 1)

def gmail():
    w.open('https://mail.google.com/mail/u/0/#inbox', new = 1)
    
def outlookmail():
    w.open('https://outlook.office365.com/mail/', new = 1)



