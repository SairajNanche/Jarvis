from VAssist import Ui_JarvisUI
from PyQt5 import QtCore,QtWidgets,QtGui
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import * #type:ignore
from PyQt5.QtWidgets import * #type:ignore
from PyQt5.QtCore import * #type:ignore
from PyQt5.uic import loadUiType

import speech_recognition as sr
import os
from body.listen import *
from body.speak import Speak
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
import sys
from threading import *  #type:ignore




class MainThread(QThread):







    def __init__(self):
        super(MainThread,self).__init__()


    def Listen1(self):
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

    
    def WakeupDetected(self):
        while True:
            queery=self.Listen1().lower()

            if "wake up" in queery:
                Speak("Wake Up Detected.")
                MainExe()
            else:
                pass

    def s1(self):
        while True:
            self.WakeupDetected()

    def run(self):
        self.s1()
        
        


     
   
startFunctions=MainThread()
startFunctions.start()


class Gui_Start(QMainWindow):
    

    def __init__(self):
        super().__init__()
        self.jarvis_ui = Ui_JarvisUI()
        self.jarvis_ui.setupUi(self)  #type:ignore
        
        #self.jarvis_ui.pushButton_start.clicked.connect(self.startFunc)
        self.jarvis_ui.pushButton_end.clicked.connect(self.close) #type:ignore

    def startFunc(self):
        self.jarvis_ui.movies1 = QtGui.QMovie("B.G/Iron_Template_1.gif") #type:ignore
        self.jarvis_ui.Gif_1.setMovie(self.jarvis_ui.movies1)#type:ignore
        self.jarvis_ui.movies1.start()#type:ignore

        self.jarvis_ui.movies2 = QtGui.QMovie("ExtraGui/live.gif") #type:ignore
        self.jarvis_ui.Gif_2.setMovie(self.jarvis_ui.movies2)#type:ignore
        self.jarvis_ui.movies2.start()#type:ignore

        self.jarvis_ui.movies3 = QtGui.QMovie("VoiceReg/Aqua.gif") #type:ignore
        self.jarvis_ui.Gif_3.setMovie(self.jarvis_ui.movies3)#type:ignore
        self.jarvis_ui.movies3.start()#type:ignore

        self.jarvis_ui.movies4 = QtGui.QMovie("ExtraGui/Earth.gif") #type:ignore
        self.jarvis_ui.Gif_4.setMovie(self.jarvis_ui.movies4)#type:ignore
        self.jarvis_ui.movies4.start()#type:ignore

        '''timer = QTimer(self)
        timer.timeout.connect(self.showTimeLive)
        timer.start(999)

    def showTimeLive(self):
        t_ime=QTime.currentTime()
        time= t_ime.toString()
        d_ate=QDate.currentDate()
        date= d_ate.toString()
        label_time="Time :"+ time
        label_date = "Date :" + date

        self.Text_Time_1.setText(label_time)
        self.Text_Time_2.setText(label_date)'''


Gui_App = QApplication(sys.argv)
Gui_Jarvis = Gui_Start()
Gui_Jarvis.show()
Gui_Jarvis.startFunc()
exit(Gui_App.exec_())