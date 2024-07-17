import pyaudio
import struct
import math

from body.speak import Speak
from body.listen import Listen
import webbrowser
import pywhatkit

def MainExe():

    while True:
        query=Listen()
        if "hello" in query:
            Speak("Hi I am Jarvis!")
            Speak("Your Personal A I Assistant")
            Speak("How may i help you?")
        elif "bye" in query:
            Speak("Bye sir,you can call me any time.")
            break
        elif'youtube search' in query:
            Speak("Ok Sir, This is what i found for your search !")
            query=query.replace("jarvis","")
            query=query.replace("youtube search","")
            web='https://www.youtube.com/results?search_query='+ query
            webbrowser.open(web)
            Speak("Done Sir")
        elif'google search' in query:
            Speak("This is what i found for your search !")
            query=query.replace("jarvis","")
            query=query.replace("google search","")
            pywhatkit.search(query) # type: ignore
        elif'website' in query:
            Speak("Ok Sir,Launching....")
            query=query.replace("jarvis","")
            query=query.replace("website","")
            web1=query.replace("open","")
            web2='https://www.'+web1+'.com'
            webbrowser.open(web2)
            Speak("Launched")



INITIAL_TAP_THRESHOLD = 0.1
FORMAT = pyaudio.paInt16 
SHORT_NORMALIZE = (1.0/32768.0)
CHANNELS = 2
RATE = 44100  
INPUT_BLOCK_TIME = 0.05
INPUT_FRAMES_PER_BLOCK = int(RATE*INPUT_BLOCK_TIME)
OVERSENSITIVE = 15.0/INPUT_BLOCK_TIME                    
UNDERSENSITIVE = 120.0/INPUT_BLOCK_TIME 
MAX_TAP_BLOCKS = 0.15/INPUT_BLOCK_TIME

def get_rms( block ):
    count = len(block)/2
    format = "%dh"%(count)
    shorts = struct.unpack( format, block )
    sum_squares = 0.0
    for sample in shorts:
        n = sample * SHORT_NORMALIZE
        sum_squares += n*n

    return math.sqrt( sum_squares / count )

class TapTester(object):

    def __init__(self):
        self.pa = pyaudio.PyAudio()
        self.stream = self.open_mic_stream()
        self.tap_threshold = INITIAL_TAP_THRESHOLD
        self.noisycount = MAX_TAP_BLOCKS+1 
        self.quietcount = 0 
        self.errorcount = 0

    def stop(self):
        self.stream.close()

    def find_input_device(self):
        device_index = None            
        for i in range( self.pa.get_device_count() ):     
            devinfo = self.pa.get_device_info_by_index(i)   
            # print( "Device %d: %s"%(i,devinfo["name"]) )

            for keyword in ["mic","input"]:
                if keyword in devinfo["name"].lower(): # type: ignore
                    # print( "Found an input: device %d - %s"%(i,devinfo["name"]) )
                    device_index = i
                    return device_index

        if device_index == None:
            print( "No preferred input found; using default input device." )

        return device_index

    def open_mic_stream( self ):
        device_index = self.find_input_device()

        stream = self.pa.open(   format = FORMAT,
                                 channels = CHANNELS,
                                 rate = RATE,
                                 input = True,
                                 input_device_index = device_index,
                                 frames_per_buffer = INPUT_FRAMES_PER_BLOCK)

        return stream
    
    def listen(self):
        
        try:
            block = self.stream.read(INPUT_FRAMES_PER_BLOCK)

        except IOError as e:
            self.errorcount += 1
            print( "(%d) Error recording: %s"%(self.errorcount,e) )
            self.noisycount = 1
            return

        amplitude = get_rms( block )
        
        if amplitude > self.tap_threshold:
            self.quietcount = 0
            self.noisycount += 1
            if self.noisycount > OVERSENSITIVE:

                self.tap_threshold *= 1.1
        else:            

            if 1 <= self.noisycount <= MAX_TAP_BLOCKS:
                return "True-Mic"
            self.noisycount = 0
            self.quietcount += 1
            if self.quietcount > UNDERSENSITIVE:
                self.tap_threshold *= 2

def Tester():

    tt = TapTester()

    while True:
        kk = tt.listen()
        if "True-Mic" == kk:
            print("")
            print(">Clap Detected: Starting the Jarvis")
            print("")
            MainExe()
        else:
            pass

while True:
    Tester()

    
