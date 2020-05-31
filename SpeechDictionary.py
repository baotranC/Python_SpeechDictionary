
from PyDictionary import PyDictionary
from bs4 import BeautifulSoup
import pyttsx3
import requests

activateSpeech = True 

def convertText2Audio(audioString):
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
            
        print('\tClass: '+wordClass)
        convertText2Audio('\tClass: '+wordClass)
            
        #print(definitions) # debug
        for definition in definitions: 
            print('\t\tDefinition '+str(count) + ': ' + definition)
            convertText2Audio('\t\tDefinition '+str(count) + ': ' + definition)
            count = count + 1

convertText2Audio('What word do you want to search? ') 
searchWord = input('What word do you want to search? ')

print('The word is: '+searchWord)
convertText2Audio('The word is '+searchWord)   

try:
    dictionaryy = PyDictionary(searchWord) 
    findDefintions(dictionaryy)
except:
        print('The word '+searchWord+' is not found')
        convertText2Audio('The word '+searchWord+' is not found')