import nltk
from nltk import word_tokenize, pos_tag
import re
import os

def Usernames():
    dict1={}
    List1=[]
    bookname = "new.txt"
    bookFile = open(bookname, 'r',encoding="utf-8")
    bookString = bookFile.read()
    lowerBook = bookString.lower()
    wordList = lowerBook.split()
    flag=0
    sentence=''
    #print(wordList)
    a=2
    for i, word in enumerate(wordList):
        #print(word)
        
        if flag==0:
            if word == "follow":
                Username1=wordList[i-1]
                flag=1
        if flag==1:
            sentence = sentence + " " + word
            if word=="follow":
                
                Description=sentence
                Username2=wordList[i-1]
                words = sentence.split()
                sentence = " ".join(words[:-4])
                sentence1=sentence
                #sentence1=extract_description(sentence)
                flag=2
                List1.append(Username1)
                dict1[Username1]=sentence1
        if flag==2:
            Username1=Username2
            flag=1
            sentence=''
    List1=remove_duplicates(List1)
    #print(List1)            
    List1 = list(reversed(List1))
    

    return List1,dict1
    
def remove_duplicates(input_list):
    return list(set(input_list))

def extract_description(sentence):
    tokens = nltk.word_tokenize(sentence)
    tagged = nltk.pos_tag(tokens)
    nouns = [word for word, pos in tagged if pos in ['NN', 'NNP', 'NNS', 'NNPS']]
    return nouns
#List1,dict1=Usernames()
#print(dict1['@imrankhanworld'])