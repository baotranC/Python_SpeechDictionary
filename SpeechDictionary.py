
from PyDictionary import PyDictionary
import pyttsx3

def convertText2Audio(audioString):
    engine = pyttsx3.init()
    engine.say(audioString)
    engine.runAndWait()
    

convertText2Audio('hi')