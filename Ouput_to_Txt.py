import save1
from save1 import enter_user
import sear
from sear import Usernames
import mysql.connector
from Clustering import DB_Clustering
import os
cnx = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Jaguar@123",
    database="sql_false_flag")
cursor = cnx.cursor()
query = "SELECT description FROM UsersProfile where Fullname LIKE '%omar%'"
#user = input("Enter the Name of user :  ")

#enter_user(user,depth=4)
###Usernames1.append(Usernames1)
####print(Descriptions)
Usernames1,Descriptions = Usernames()
#os.remove('new.txt')
#print(Descriptions)
#cursor.execute(query)
#with open('data.txt','w',encoding='utf-8') as f:
##    rows=cursor.fetchall()
#    for row in Usernames1 :
#        if str(Descriptions[row]) != '':
#            f.write('"'+str(Descriptions[row])+'"'+'\n')
DB_Clustering()
#os.remove('data.txt')