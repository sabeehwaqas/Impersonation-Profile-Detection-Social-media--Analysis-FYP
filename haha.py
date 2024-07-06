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

cnx = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Jaguar@123",
    database="sql_false_flag")
cursor = cnx.cursor()
#Copy_Table('UsersProfile','UsersProfile_Temp')
query = "SELECT Username FROM Groups1_Info "#where Fullname LIKE '%imran%'"
#query = f"SELECT * FROM UsersProfile where Fullname LIKE '%imran%'"
cursor.execute(query)
rows = list(cursor.fetchall())
Username_List=[]
for usernames in rows:
    usernames=usernames[0][1:]
    Username_List.append("@"+usernames)
print(Username_List)
query = "SELECT  FROM Groups1_Info "#where Fullname LIKE '%imran%'"
#query = f"SELECT * FROM UsersProfile where Fullname LIKE '%imran%'"
cursor.execute(query)
rows = list(cursor.fetchall())

