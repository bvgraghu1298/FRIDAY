


#This code is the property of batch 16CSMIN06. ready for licensing and production
#Developed by Raghunath Sharma, Kishan Sai and Nagi Reddy.
import os
import webview
import threading
import nltk
import numpy as np
import aiml
import sys, glob
import json,csv
import random
import pickle
import warnings
import io, random, string
import pyttsx3

# from nltk.corpus import names
from collections import defaultdict
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer,CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
#import gender_guessser.detector as gender




#remove unnecessary words from input
def data_mine_senses(userMessage):
        f = open("un_useful.csv","r")
        data = list(csv.reader(f))[0]
        resultwords  = [word for word in userMessage.split() if word.lower() not in data]
        return resultwords
#this is the intent recognition and classification function
#we need to use this in case of generative model training
#  def intents(self, resultwords):
#         with open('intents/json file/intents.json') as memory:
#             intents = json.load(memory)
#         types = []
#         word  = []
#         docs  = []
#         for intent in intents['intents']:
#             for pattern in intent['patterns']:
#                 token = nltk.word_tokenize(pattern)
#                 word.extend(token)
#                 docs.append((token, intent['tag']))
#                 if intent['tag'] not in types:
#                     types.append(intent['tag'])
#         words = nltk.stemmer.stem(token)
#         words = sorted(list(set(words)))
#         types = sorted(list(set(types)))
#         #implement bow 
#         training =[]
#         response =[]
#         res =[0] *len(types)
#         #initialize bag of words
#         for doc in docs:
#             bags = []
#             patterns = doc[0]



#the retrieval function by calculating term and document frequencies and matching them using cosine similarity
def friday(sentence):
    data = "data.csv"
    tfidf_vect_picklepath = "tfidf_vectorizer.pickle"
    tfidf_matrixpath = "tfidf_matrix_train.pickle"
    i=0
    inp_sentences = []
    test_data_set = (sentence,"")
    try:
        f = open(tfidf_vect_picklepath, 'rb')
        tfidf_vectorizer = pickle.load(f)
        f.close()
        f=open(tfidf_matrixpath,'rb')
        tfidf_matrix = pickle.load(f)
        f.close()
    except:
        with open(data,"r") as sentences:
            reader = csv.reader(sentences, delimiter = ',')
            for row in reader:
                inp_sentences.append(row[0])
                i=i+1
        #initialize the vectorizer object
        tfidf_vectorizer = TfidfVectorizer()
        #find the matrix score by using fit_transform 
        tfidf_matrix_train = tfidf_vectorizer.fit_transform(inp_sentences)
        #here matrix is the input matrix
        
        #dump the data into the  sentence pickle file
        f=open(tfidf_vect_picklepath,'wb')
        pickle.dump(tfidf_vectorizer,f)
        f.close()
    tfidf_matrix_test = tfidf_vectorizer.transform(test_data_set)

    #now initialize the cosine similarity to check similarity between two datasets
    cosine = cosine_similarity(tfidf_matrix_test,tfidf_matrix_train)
    cosine = np.delete(cosine,0)
    max = cosine.max()
    response_index = 0

    if(max>0.7):
        new_max = max-0.01
        list = np.where(cosine>new_max)
        response_index = random.choice(list[0])
    else:
        response_index = np.where(cosine==max)[0][0]+2
    j=0
    with open(data,"r") as sentences:
        reader = csv.reader(sentences, delimiter=',')
        for row in reader:
            j=j+1
            if j==response_index:
                return row[1], response_index
                break
while 1:
    user_input = input("Enter your Message:")
    main_response = friday(user_input)
    print(main_response)
    print

    

    