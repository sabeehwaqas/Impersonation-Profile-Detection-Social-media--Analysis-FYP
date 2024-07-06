import mysql.connector

def Copy_Table(Table_Name,Temp_Table_Name):
    conn = mysql.connector.connect(
    host="localhost",
     user="root",
    password="Jaguar@123",
    database="sql_false_flag")
    cursor = conn.cursor()
    #query= f"DROP TABLE IF EXISTS `{Temp_Table_Name}` ;"
    #cursor.execute(query)
    #conn.commit()
    query= f"INSERT INTO `{Table_Name}` SELECT * FROM `{Temp_Table_Name}`;"
    #query= f"CREATE TABLE `{New_Table_Name}` AS SELECT * FROM `{Table_Name}`;"
    cursor.execute(query)
    conn.commit()
    cursor.close()
    conn.close()
    