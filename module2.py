
import re
import os

def getbook():
    dict1={}
    List1=[]
    bookname = "information.txt"
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
                flag=2
                List1.append(Username1)
                dict1[Username1]=sentence
        if flag==2:
            Username1=Username2
            flag=1
            sentence=''
    #print(List1)            
    return List1,dict1
List1,dict1=getbook()
for i, user in enumerate(List1):
    print(user,'==',dict1[user])
#Username='Ali'
#outer_dict = {
#  Username: {
#    'name': 'hellp Doe',
#    'age': 30,
#    'city': 'New York'
#  },
#  'Username2': {
#    'name': 'Jane Doe',
#    'age': 25,
#    'city': 'London'
#  }
#}

#print(outer_dict[Username]['name'])