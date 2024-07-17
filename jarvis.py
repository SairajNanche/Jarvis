
from body.speak import Speak
from body.listen import *
import webbrowser
import pywhatkit
import os
import keyboard
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
import datetime
import shutil
import requests
from twilio.rest import Client
from bs4 import BeautifulSoup
import win32com.client as wincl
from urllib.request import urlopen
import feedparser

def MainExe():

    def Email():
        email_sender = "YOUR EMAIL ADDRESS"
        email_password = 'YOUR GOOGLE MACHINE CODE'
        Speak("say recievers Email id")
        reciever = Listen()
        if 'sairaj' in reciever:
            email_reciever = 'EMAIL ADDRESS'
        else:
            print('reciever id'.format(Text))
            email_reciever=input(Text)
        Speak("say Subject")
        subject = Listen()
        Speak("say body of mail")
        body = Listen()
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.ehlo()
            server.starttls()
            server.login(email_sender, email_password)
            message = f'Subject: {subject}\n\n{body}'
            server.sendmail(email_sender, email_reciever, message)  # type: ignore
            server.close()
            Speak("Email sent successfully")
        except Exception as e:
            print(e)
            Speak("sorry ,I am not able to send email")

   

    def Music():
        Speak("Tell me the name of the song !")
        musicName = Listen()
        if 'name' in musicName:
            os.startfile("path")
        else:
            musicName = musicName.replace("jarvis", "")
            musicName = musicName.replace("play", "")
            pywhatkit.playonyt(musicName)  # type: ignore
        Speak("Your song has been started, enjoy")

    def Whatsapp():
        Speak("Tell me the name of the person !")
        name = Listen()
        if 'Tanmay Patil' in name:
            Speak("Tell me the message")
            msg = Listen()
            ph='NUMBER'
            pywhatkit.sendwhatmsg_instantly(ph, msg, 25)  # type: ignore
            Speak("ok sir,Sending Whatsapp message !")
        elif 'sairaj' in name:
            Speak("Tell me the message")
            msg = Listen()
            ph='NUMBER'
            pywhatkit.sendwhatmsg_instantly(ph, msg, 20, False, 5)  # type: ignore
            Speak("ok sir,Sending Whatsapp message !")
        elif 'Nikhil' in name:
            Speak("Tell me the message")
            msg = Listen()
            ph='NUMBER'
            pywhatkit.sendwhatmsg_instantly(ph, msg, 20, False, 5)  # type: ignore
            Speak("ok sir,Sending Whatsapp message !")
        else:
            Speak("Tell me the Number")
            print('[phone no]'.format(Text))
            phone=input(Text)
            #phone = (Listen())
            ph = '+91' + phone  # type: ignore
            Speak("Tell me the message")
            msg = Listen()

            pywhatkit.sendwhatmsg_instantly(ph, msg, 15, False, 10)  # type: ignore
            Speak("ok sir,Sending Whatsapp message !")

    def Openapp():
        Speak("oh sir!, wait a second")
        if 'word' in query:
            os.startfile('C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE ')
        
        elif 'chrome' in query:
            os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
        Speak("your command has been completed")

    def Closeapp():
        Speak("ok sir,wait a second")

        if 'code' in query:
            os.system("TASKKILL/F /im code.exe")
            Speak("your command has been completed")

        elif 'chrome' in query:
            os.system("TASKKILL/F /im chrome.exe")
            Speak("your command has been completed")
       
        
        



    def Screenshot():
        Speak("ok boss,what should i name the file")
        path = Listen()
        path1name = path+".png"
        path1 = 'C:\\Users\\saira\\Pictures\\Screenshots\\' + path1name
        kk = pyautogui.screenshot()
        kk.save(path1)
        os.startfile('C:\\Users\\saira\\Pictures\\Screenshots')
        Speak("Here is your screenshot")

    while True:

        query = Listen()
        if "hello" in query:

            Speak("Hi I am Jarvis!")
            Speak("Your Personal A I Assistant")
            Speak("How may i help you?")
        elif "bye" in query:

            Speak("Bye sir,you can call me any time.")
            break
        elif 'exit' in query:
            Speak("Thanks for giving me your time")
            exit()
        elif 'youtube search' in query:

            Speak("Ok Sir, This is what i found for your search !")
            query = query.replace("jarvis", "")
            query = query.replace("youtube search", "")
            web = 'https://www.youtube.com/results?search_query=' + query
            webbrowser.open(web)
            Speak("Done Sir")
        elif 'google search' in query:

            Speak("This is what i found for your search !")
            query = query.replace("jarvis", "")
            query = query.replace("google search", "")
            pywhatkit.search(query)  # type: ignore
        elif 'website' in query:

            Speak("Ok Sir,Launching....")
            query = query.replace("jarvis", "")
            query = query.replace("website", "")
            web1 = query.replace("open", "")
            web2 = 'https://www.'+web1+'.com'
            pywhatkit.search(web2) # type: ignore
            #webbrowser.open(web2)
            Speak("Launched!")
        elif 'launch' in query:

            Speak("Tell me the name of the website!")
            name = Listen()
            web = 'https://www.' + name + '.com'
            webbrowser.open(web)
            Speak("Done Sir")
       
        elif 'facebook' in query:

            Speak("ok sir")
            webbrowser.open("https://www.facebook.com")
            Speak("Done sir ...")
        elif 'music' in query:

            Music()
        elif 'whatsapp' in query:

            Whatsapp()
        elif 'screenshot' in query:

            Screenshot()
        elif 'open'and'app' in query:

            Openapp()
        elif 'close'and'app' in query:

            Closeapp()
        elif 'send email' in query:

            Email()
        elif 'how are you' in query:
            Speak("I am fine, Thank you")
            Speak("How are you, ")
        elif "good morning" in query  or "good afternoon" in query or "good evening" in query:
            query = query.replace("jarvis", "")
            Speak("A very " +query)
            Speak("Thank you for wishing me! Hope you are doing well!")
        elif 'fine' in query or "good" in query:
            Speak("It's good to know that your fine")
        elif 'time' in query:
            strTime = datetime.datetime.now()
            curTime=str(strTime.hour)+"hours"+str(strTime.minute)+"minutes"+str(strTime.second)+"seconds"
            
            Speak(f" the time is {curTime}")
            print(curTime)
        elif 'shutdown system' in query:
                Speak("Hold On a Sec ! Your system is on its way to shut down")
                subprocess.call(["shutdown", "/p"])

        elif "restart" in query:
            subprocess.call(["shutdown", "/r"])

        elif "sleep" in query:
            Speak("Setting in sleep mode")
            subprocess.call(["shutdown", "/h"])
        elif "write a note" in query:
            Speak("What should i write, sir")
            note = Listen()
            file = open('jarvis1.txt','a')
            Speak("Sir, Should i include date and time")
            snfm = Listen()
            if 'yes' in snfm:
                strTime = datetime.datetime.now() #.strftime("% H:% M:% S")
                curTime=str(strTime.hour)+" H:"+str(strTime.minute)+" M:"+str(strTime.second)+"S"
                file.write(curTime)
                file.write(" :- ")
                file.write(note)
                file.close()
            else:
                file.write(note)
                file.close()

            Speak("note saved")
        elif'open new tab'in query:
            keyboard.press_and_release('ctrl+t')
        elif 'open new window'in query:
            keyboard.press_and_release('ctrl+n')
        elif 'close this'in query:
            keyboard.press_and_release('ctrl+w')
       
        
        


'''wn = Tk() 
wn.title("DataFlair Voice Assistant")
wn.geometry('700x300')
wn.config(bg='LightBlue1')
  
Label(wn, text='Welcome I am JARVIS', bg='LightBlue1',
      fg='black', font=('Courier', 15)).place(x=50, y=10)
#Button to convert PDF to Audio form
Button(wn, text="Start", bg='gray',font=('Courier', 15),command=MainExe).place(x=290, y=100)
showCommand=StringVar()
cmdLabel=Label(wn, textvariable=showCommand, bg='LightBlue1',
      fg='black', font=('Courier', 15))
cmdLabel.place(x=250, y=150)
#Runs the window till it is closed
wn.mainloop()'''
