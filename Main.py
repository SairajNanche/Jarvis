import speech_recognition as sr
import os
from body.speak import Speak
from body.listen import *
from jarvis import MainExe


import webbrowser
import pywhatkit
import os
import pyautogui
from email.message import EmailMessage
import ssl
import smtplib
import time
import subprocess
import wolframalpha
import random
import winshell
import json
from tkinter import * #type:ignore
from tkinter import messagebox



"""def Listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")

        r.pause_threshold = 1
        audio = r.listen(source, 0,5)
    try:
        print("Recognising...")
        query = r.recognize_google(audio, language="en-in")
    except:
        return ""
    query = str(query).lower()
    print(query)
    return query
"""
def WakeupDetected():
    queery=Listen().lower()

    if "wake up" in queery:
        Speak("Wake Up Detected.")
        MainExe()
    else:
        pass
def start():
    while True:
        WakeupDetected()

start()
"""
wn = Tk() 
wn.title("JARVIS Voice Assistant")
wn.geometry('700x300')
wn.config(bg='LightBlue1')
  
Label(wn, text='Welcome I am JARVIS', bg='LightBlue1',
      fg='black', font=('Courier', 15)).place(x=50, y=10)
#Button to convert PDF to Audio form
Button(wn, text="Start", bg='gray',font=('Courier', 15),command=start).place(x=290, y=100)
showcommand=StringVar()
cmdLabel=Label(wn, textvariable=showcommand, bg='LightBlue1',
      fg='black', font=('Courier', 15))
cmdLabel.place(x=250, y=150)
#Runs the window till it is closed
wn.mainloop()



"""
