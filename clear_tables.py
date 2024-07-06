import mysql.connector
from Botometer_SQL import Remove_column
def clearTables():
    conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Jaguar@123",
    database="sql_false_flag")
    cursor = conn.cursor()
    #try:
    #    query="TRUNCATE TABLE UsersProfile ;"
    #    cursor.execute(query)
    #    conn.commit()    
    #except:
    #    a=1
    #try:    
    #    query="TRUNCATE TABLE UsersTweets ;"
    #    cursor.execute(query)
    #    conn.commit()    
    #except:
    #    a=1
    try:
        Remove_column()
    except :
        a=1
    #try:
    #    query="TRUNCATE TABLE UsersProfile_Temp ;"
    #    cursor.execute(query)
    #    conn.commit()    
    #except:
    #    a=1
    try:    
        query="TRUNCATE TABLE UsersTweets_Temp ;"
        cursor.execute(query)
        conn.commit()    
    except:
        a=1
    try:
        query="TRUNCATE TABLE Groups1_Info ;"
        cursor.execute(query)
        conn.commit()    
    except:
        a=1
    #try:
    #    query="TRUNCATE TABLE Feed_Back_Groups1_Info ;"
    #    cursor.execute(query)
    #    conn.commit()    
    #except:
    #    a=1
    try:
        query="TRUNCATE TABLE After_Feedback_Groups1_Info;"
        cursor.execute(query)
        conn.commit()    
    except:
        a=1
    
    try:
        query="TRUNCATE TABLE Sentiments;"
        cursor.execute(query)
        conn.commit()    
    except:
        a=1
    
    
        
    