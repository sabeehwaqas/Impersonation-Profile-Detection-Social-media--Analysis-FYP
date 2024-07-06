from cgi import print_environ
from pprint import pprint
import nltk
from namematcher import NameMatcher
from nltk import word_tokenize, pos_tag
import json
from Des import extract_description, Description_Analysis,similarity
import mysql.connector
from Clustering import Des_Clustering
import spacy
import statistics
from CopyingTable import Copy_Table
import re

def Extract_Des(text):
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(text)
    noun_chunks = [chunk.text for chunk in doc.noun_chunks]
    nouns =",".join(noun_chunks )
    nouns = '"'+nouns+'"'
    return nouns
def descr(data1,data2):
    des=data1
    des1=data2
    common=Description_Analysis(des, des1)
    return (common*100)
def group_Description(dict1=[]):
    Feed_Back_Username=[]
    Feed_Back_Descriptions=[]
    Feed_Back_Full_Name=[]
    cnx = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Jaguar@123",
    database="sql_false_flag")
    cursor = cnx.cursor()
    query = f"SELECT * FROM UsersProfile_Temp;"
    cursor.execute(query)
    rows = cursor.fetchall()
    data1=[]
    Usernames1=[]
    Num=0
    tot=0
    tot1=0
    Descriptions=[]
    followers_Count=[]
    USRLST=[]
#------------------------------------------------------------------------------------------------------------------#
    for row in rows:
        if row[0]!=' ':
            if dict1!=[]:
                for aa,aaa in enumerate(dict1):
                    if row[0]==aaa['Twitter_ID']:
                        data1.append({'Full_name':row[1],'User-name':row[0],'verification':row[7],'followers':row[4],'description':(row[3]+' '+aaa['description'])})
                        Descriptions.append({'Username':row[0],'description':(row[3]+' '+aaa['description'])})
                        USRLST.append(aaa['Twitter_ID'])
                        dict1[aa]['Twitter_ID']=''
#------------------------------------------------------------------------------------------------------------------#
    for row in rows:
        if row[0]!=' ':
            if row[0] in USRLST:
                continue
            Descriptions.append({'Username':row[0],'description':row[3]})
            data1.append({'Full_name':row[1],'User-name':row[0],'verification':row[7],'followers':row[4],'description':row[3]})
#------------------------------------------------------------------------------------------------------------------#
    if dict1!=[]:
        Final_Cluster=Des_Clustering(data1,None,1.4)
    else:    
        Final_Cluster=Des_Clustering(data1,None,1.2)
#------------------------------------------------------------------------------------------------------------------#
#---HERE WE ARE GIVING HEADS TO EACH OF GROUPS OF PROFILES
    for aa,dd in enumerate(Final_Cluster):
        max1=0
        for asa,ad in enumerate(dd['List']):
            for bb,cc in enumerate(data1):
                if ad==cc['User-name']:
                    if cc['verification']==1:
                        Final_Cluster[aa]['Cluster# ']=cc['User-name']
                    elif cc['followers']>max1:
                        max1=cc['followers']
                        Final_Cluster[aa]['Cluster# ']=cc['User-name']
    #print(Final_Cluster)
#------------------------------------------------------------------------------------------------------------------#
    for i, user in enumerate(Final_Cluster):
        flag=0
        for a,description1 in enumerate(Descriptions):
            for b,lists in enumerate(user['List']):
                if lists==description1['Username']:
                    description=description1['description']
                    if len(description)<11:
                        results13= str(Extract_Des(description))
                        results13 = results13.split()
                        unique_words = set(results13)
                        Dess= ' '.join(unique_words)
                    elif 'https://' not in description: 
                        results12 = description.split()
                        unique_words = set(results12)            
                        results12= ' '.join(unique_words)
                        Dess=str(Extract_Des(results12))
                    elif 'https://' in description:            
                        results12 = description
                        Dess=str(results12)
                    if flag==0:
                        query=f"select Fullname from UsersProfile_Temp WHERE Username='{user['Cluster# ']}'"
                        cursor.execute(query)
                        results13 =cursor.fetchone()
                        try:
                            fullname= str(results13[0])
                        except Exception :
                            print('OOPS',fullname,'--',user['Cluster# '])
                        flag=1
                        if dict1 != []:
                            query = "INSERT INTO After_Feedback_Groups1_Info (Username,Usernames,Keywords,Fullname) VALUES (%s,%s,%s,%s)"
                            values = (str(user['Cluster# ']),str(user['List']),Dess,fullname)    
                            cursor.execute(query, values)
                            cnx.commit()
                        else:
                            query = "INSERT INTO Groups1_Info (Username,Usernames,Keywords,Fullname) VALUES (%s,%s,%s,%s)"
                            values = (str(user['Cluster# ']),str(user['List']),Dess,fullname)    
                            cursor.execute(query, values)
                            cnx.commit()
#------------------------------------------------------------------------------------------------------------------#
    cursor.close()
    cnx.close()
    #------------------------------------------------------------------------------------------------------------------#