#import csv
import mysql.connector

b=0
'''
def cSV_cSV:
    with open('Profiles.csv', newline='',encoding="utf-8" ) as csvfile:
     data = csv.DictReader(csvfile)
     print("User Name")
     print("---------------------------------")
     for b in range(z):

      for row in data:
        if Lines[b] in csvfile:
          print(row['User_Name'])
      b+=1
      '''
conn = mysql.connector.connect(
host="localhost",
    user="root",
password="Jaguar@123",
database="sql_false_flag")
cursor = conn.cursor()
query="SELECT * from Sentiments "
cursor.execute(query)
profiles=cursor.fetchall()
print(profiles)

'''
for profile in profiles:
    user=profile[0]
    Full_name=profile[1]
    location=profile[2]
    desc=profile[3]
    followers=profile[4]
    following=profile[5]
    join_date=profile[6]
    verification=profile[7]
    list_count=profile[8]
    favourite_counts=profile[9]
    birthday=profile[10]
    profession=profile[11]
    tweetno=profile[12]
    website=profile[13]
values = (user,Full_name,location,desc,followers,following,join_date,verification,list_count,favourite_counts,birthday,profession,tweetno,website)
#print(values)
cursor.execute('SELECT Username COUNT(*) FROM UsersProfile GROUP BY Username HAVING COUNT(*) > 1')
'''
# Get the list of duplicate rows
#duplicate_rows = cursor.fetchall()

# Loop through the duplicate rows and delete all but one of them
#for row in duplicate_rows:
 #   cursor.execute('DELETE FROM UsersProfile WHERE Username = %s AND rowid NOT IN (SELECT MIN(rowid) FROM UsersProfile WHERE Username = %s )', (row[0], row[0]))

# Commit the changes
conn.commit()