import speech_recognition as sr
from googletrans import Translator

#1. Listen:Hindi or English
def Listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")

        r.pause_threshold = 1
        audio = r.listen(source,0, 8)
    try:
        print("Recognising...")
        query = r.recognize_google(audio, language="en=in")
    except:
        return ""
    query = str(query).lower()
    print(f"You : {query}.")
    return query


#2. Translation

def TranslationHinToEng(Text):
    line=str(Text)
    translate=Translator()
    result=translate.translate(line)
    data = result.text # type: ignore
    print(f"You : {data}.")
    return data

#3  connect

def MicExecution():
    query=Listen()
    data =TranslationHinToEng(query)
    return data
MicExecution()


