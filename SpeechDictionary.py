
from PyDictionary import PyDictionary
from bs4 import BeautifulSoup
import pyttsx3

def convertText2Audio(audioString):
    engine = pyttsx3.init()
    
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 150)
    
    engine.say(audioString)
    engine.runAndWait()
    
    
def findDefintions(word):
    try:
        count = 1
        dictionary = PyDictionary(searchWord)
        meanings = dictionary.getMeanings()
        
        print("The word is: "+searchWord)
        convertText2Audio("The word is "+searchWord)
        
        meanings = meanings[searchWord]
        for wordClass, definitions in meanings.items():
            
            print("\tClass: "+wordClass)
            convertText2Audio("\tClass: "+wordClass)
            
            #print(definitions) # debug
            for definition in definitions: 
                print("\t\tDefinition "+str(count) + ": " + definition)
                convertText2Audio("\t\tDefinition "+str(count) + ": " + definition)
                count = count + 1
    except:
        print("The word "+searchWord+" is not found")
        convertText2Audio("The word "+searchWord+" is not found")


searchWord = input('What word do you want to search? ')
print('')
print('1: Find definitions')
print('2: Find synonyms')
print('3: Find antonyms')
print('4: Translate')
print('')
option = input('What do you want to do: ')

if option == '1': 
    findDefintions(searchWord)
else: 
    print("Option "+option+" does not exist")
    convertText2Audio("Option "+option+" does not exist")

