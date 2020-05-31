
from PyDictionary import PyDictionary
import pyttsx3

def convertText2Audio(audioString):
    engine = pyttsx3.init()
    
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 150)
    
    engine.say(audioString)
    engine.runAndWait()
    
    
searchWord = input('What word do you want to search?')
try:
    count = 1
    
    dictionary = PyDictionary(searchWord)
    meanings = dictionary.getMeanings()
    #print(meanings)
    
    convertText2Audio("The word is "+searchWord)
    
    meanings = meanings[searchWord]
    for wordClass, definitions in meanings.items():
         
        convertText2Audio("word class")
        print(wordClass)
        convertText2Audio(wordClass)
        
        print(definitions) # debug
        for definition in definitions: 
            print(str(count) + ": " + definition)
            convertText2Audio("definition "+str(count))
            convertText2Audio(definition)
            count = count + 1
except:
    convertText2Audio("The word "+searchWord+" is not found")
