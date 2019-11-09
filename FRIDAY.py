#This code is the property of batch 16CSMIN06. ready for licensing and production
#Developed by Raghunath Sharma, Kishan Sai and Nagi Reddy.
import os
import webview
import threading
import nltk
import numpy as np
import aiml
import sys, glob
import json
import warnings
import io, random, string
import pyttsx3
# from nltk.corpus import names
from collections import defaultdict

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
#import gender_guessser.detector as gender



#opening the Friday corpus from text files
#fin       =   open('friday.txt','r',errors='ignore')
#data      =   fin.read().lower()

#opening the corpus from other AIML data files

'''
if os.path.isfile("bot_brain.brn"):
    kernel.bootstrap(brainFile = "bot_brain.brn")
else:
    kernel.bootstrap(learnFiles = "std-startup.xml", commands = "load aiml b")
    kernel.saveBrain("bot_brain.brn")
    '''
    


#initializing the lemmatizer




#lem       =   WordNetLemmatizer()
#javascript to python functions
class Functions:

        
    def sendAIML(self, userMessage):
        flag=0
        kernel=aiml.Kernel()
        kernel.learn("std-startup.xml")
        kernel.respond("load aiml b")
        while True:
            output = kernel.respond(userMessage)
            if output:
                flag = 1
                print(output)
                return output
                kernel.close()
            break
        if(flag==0):
            output = "Sorry Boss!"
           
            
    # def data_mine_senses(userMessage):
    #     f = open("un_useful.csv","r")
    #     data = list(csv.reader(f))[0]
    #     resultwords  = [word for word in userMessage.split() if word.lower() not in data]
    #     return resultwords

     
    
  
fun = Functions()
        

def app_logic() :
   
    # BEGIN APP LOGIC
   
    #webview.evaluate_js("alert('hello world')")
    print("Loading...")
    startup = pyttsx3.init()
    startup.say("Hello Boss! This is FRIDAY. Funny but rather Intelligent dynamic assistant for you!")
    startup.runAndWait()
    # END APP LOGIC


# WARNING : try not to modify the below code
if __name__ == '__main__':


    

    # all your app logic will be run as a seperate thread , this is important
    t = threading.Thread(target=app_logic)
    t.start()
    
    # this should be the last line of your app 
    webview.create_window("FRIDAY", "code.html", js_api=fun)