#windows based
import pyttsx3
from time import sleep
def Speak(Text):
    engine=pyttsx3.init("sapi5")
    voices=engine.getProperty('voices')
    engine.setProperty('voices',voices[0].id)
    engine.setProperty('rate',170)
    """
    print("")
    print(f"You : {Text}.")
    print("")
    
    engine.say(Text)
    engine.runAndWait()
    """
    lengthoftext=len(str(Text))
    if lengthoftext==0:
        pass
    else:
        print("")
        print(f"AI : {Text}.")
        print("")
        engine.say(Text)
        engine.runAndWait()
        if lengthoftext>=30:
            sleep(4)
        elif lengthoftext>=40:
            sleep(6)
        elif lengthoftext>=55:
            sleep(8)
        elif lengthoftext>=70:
            sleep(10)
        elif lengthoftext>=100:
            sleep(13)
        elif lengthoftext>=120:
            sleep(14)
        else:
            sleep(2)

        

"""
#chrome based
from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.support.ui import Select # type: ignore
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep

chrome_options=Options()
chrome_options.add_argument('--log-level=3')
chrome_options.headless=True
Path="database\\chromedriver.exe"
#Path=r'C:\\path\to\\chromedriver.exe'
driver=webdriver.Chrome(Path) # type: ignore
#driver = webdriver.Chrome(Path) # type: ignore
#driver.get('http://google.com/')
driver.maximize_window()

website=r"https://ttsmp3.com/text-to-speech/British%20English/"
driver.get(website)
ButtonSelection=Select(driver.find_element(by=By.XPATH,value='/html/body/div[4]/div[2]/form/select'))
ButtonSelection.select_by_visible_text('British English / Brian')

def Speak(Text):
    lengthoftext=len(str(Text))
    if lengthoftext==0:
        pass
    else:
        print("")
        print(f"AI : {Text}.")
        print("")
        Data=str(Text)
        xpathofsec='/html/body/div[4]/div[2]/form/textarea'
        driver.find_element(By.XPATH,value=xpathofsec).send_keys(Data)
        driver.find_element(By.XPATH,value='//*[@id="vorlesenbutton"]').click()
        driver.find_element(By.XPATH,value='/html/body/div[4]/div[2]/form/textarea').clear()

        if lengthoftext>=30:
            sleep(4)
        elif lengthoftext>=40:
            sleep(6)
        elif lengthoftext>=55:
            sleep(8)
        elif lengthoftext>=70:
            sleep(10)
        elif lengthoftext>=100:
            sleep(13)
        elif lengthoftext>=120:
            sleep(14)
        else:
            sleep(2)
"""
