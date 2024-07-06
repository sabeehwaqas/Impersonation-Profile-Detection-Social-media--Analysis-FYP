
import save1
from save1 import enter_user
import re

def getbook(name):
    bookname = name
    bookFile = open(bookname, 'r',encoding="utf-8")
    bookString = bookFile.read()
    lowerBook = bookString.lower()
    wordList = lowerBook.split()
    return wordList

import string

def listAllThe(longString):
    theList = []
    for i in longString:
        if i.startswith('@'):
            theList.append(i)
        else:    
            theList.append(i)
    return theList

def Usernames(name):
    book = getbook(name)
    getList = listAllThe(book)
    getList = list(set(getList))

    #print (getList)
    return getList
