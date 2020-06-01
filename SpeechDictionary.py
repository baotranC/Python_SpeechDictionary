
from PyDictionary import PyDictionary
import pyttsx3
import requests
import speech_recognition as sr

activateSpeech = True 

def convertText2Audio(audioString):
    print(audioString)
    
    if activateSpeech: 
        engine = pyttsx3.init()
        
        rate = engine.getProperty('rate')
        engine.setProperty('rate', 150)
        
        engine.say(audioString)
        engine.runAndWait()
    
def findDefintions(dictionary):
    count = 1
    meanings = dictionary.getMeanings()
    meanings = meanings[searchWord]
    
    for wordClass, definitions in meanings.items():
        convertText2Audio('\tClass: '+wordClass)
        #print(definitions) # debug
        for definition in definitions: 
            convertText2Audio('\t\tDefinition '+str(count) + ': ' + definition)
            count = count + 1

def record_audio(ask = False):
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        if ask: 
            convertText2Audio(ask)
        audio = r.listen(source)
        
        voiceData = ''
        try:
            voiceData = r.recognize_google(audio)
        except sr.UnknownValueError:
            convertText2Audio('Error: unrecognizable word')
            voiceData = ''
        except sr.RequestError:
            convertText2Audio('Error: the speech service is down')
            voiceData = ''
        return voiceData 
    
convertText2Audio('What word do you want to search? ')
record = record_audio()

if record != '': 
    words = record.split(' ')
    if len(words) == 1: 
        searchWord = words[0]
        convertText2Audio('The word is '+searchWord)   

        try:
            dictionaryy = PyDictionary(searchWord) 
            findDefintions(dictionaryy)
        except:
            convertText2Audio('The word '+searchWord+' is not found')         
    else: 
        convertText2Audio('Can not define more than one word')     
convertText2Audio('End of definition')