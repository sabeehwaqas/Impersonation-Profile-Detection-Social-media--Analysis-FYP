import mysql.connector
from Botometer import botometer_analysis
import time
time.sleep(5)
def Remove_column():
    
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Jaguar@123",
    database="sql_false_flag"
    )

    # Create a cursor object to interact with the database
    mycursor = mydb.cursor()

    # Define the columns to be dropped
    columns_to_drop = ['Bot_Score', 'Echo_Chamber', 'Fake_Followers', 'Financial', 'Self_Declared', 'Spammer', 'Most_Recent_Post', 'Likes_Count', 'Recent_tweets_per_week', 'Retweet_Ratio', 'Tweets_by_day_of_week', 'Sun', 'Mon', 'Tues', 'Wed', 'Thurs', 'Fri', 'Sat', 'Tweets_by_hour_of_day', '12AM', '1AM', '2AM', '3AM', '4AM', '5AM', '6AM', '7AM', '8AM', '9AM', '10AM', '11AM', '12PM', '1PM', '2PM', '3PM', '4PM', '5PM', '6PM', '7PM', '8PM', '9PM', '10PM', '11PM', 'Prediction']

    # Check if each column exists before dropping it
    for column in columns_to_drop:
        query = "SELECT * FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'usersprofile_temp' AND COLUMN_NAME = '" + column + "'"
        mycursor.execute(query)
        result = mycursor.fetchone()
        if result is not None:
            # Define the SQL query to drop the column
            query = "ALTER TABLE usersprofile_temp DROP COLUMN " + column
            # Execute the query
            mycursor.execute(query)
            # Commit the changes to the database
            mydb.commit()
            #print("Column " + column + " has been dropped")
        else:
            a=1
            #print("Column " + column + " does not exist")

    # Close the database connection
    mydb.close()

def Botometer_SQL():
    
    #removing columns if present
    Remove_column()
    
    try:
        # Connect to the MySQL Server
        host = 'localhost'
        database = 'sql_false_flag'
        user = 'root'
        password = 'Jaguar@123'
        cnxn = mysql.connector.connect(host=host, database=database, user=user, password=password)

        # make new botometer columns
        try:
            query1 = "SELECT COUNT(*) FROM information_schema.columns WHERE table_name = 'usersprofile_temp' AND column_name IN ('Bot_Score', 'Echo_Chamber','Fake_Followers','Financial','Self_Declared','Spammer','Most_Recent_Post','Likes_Count','Recent_tweets_per_week','Retweet_Ratio','Tweets_by_day_of_week','Sun','Mon','Tues','Wed','Thurs','Fri','Sat','Tweets_by_hour_of_day','12AM','1AM','2AM','3AM','4AM','5AM','6AM','7AM','8AM','9AM','10AM','11AM','12PM','1PM','2PM','3PM','4PM','5PM','6PM','7PM','8PM','9PM','10PM','11PM') AND table_schema = 'sql_false_flag'"
            #query1 = "SELECT * FROM sql_false_flag.columns WHERE table_name = 'usersprofile_temp' AND column_name IN ('Bot Score', 'Echo Chamber','Fake Followers','Financial','Self Declared','Spammer','Most Recent Post','Likes','Recent tweets per week','Retweet Ratio','Tweets by day of week','Sun','Mon','Tues','Wed','Thurs','Fri','Sat','Tweets by hour of day','12AM','1AM','2AM','3AM','4AM','5AM','6AM','7AM','8AM','9AM','10AM','11AM','12PM','1PM','2PM','3PM','4PM','5PM','6PM','7PM','8PM','9PM','10PM','11PM')"
            cursor1 = cnxn.cursor()

            cursor1.execute(query1)
            print("wefwefwef till here ------------------------------")
            results = cursor1.fetchall()
            print('results',results[0][0])
            if results[0][0]==0:

                # ADDIng the coloumbs 
                query2 = 'ALTER TABLE usersprofile_temp ADD COLUMN Bot_Score VARCHAR(255),ADD COLUMN Echo_Chamber VARCHAR(255), ADD COLUMN Fake_Followers VARCHAR(255),ADD COLUMN Financial VARCHAR(255),ADD COLUMN Self_Declared VARCHAR(255),ADD COLUMN Spammer VARCHAR(255),ADD COLUMN Most_Recent_Post VARCHAR(255),ADD COLUMN Likes_Count VARCHAR(255),ADD COLUMN Recent_tweets_per_week VARCHAR(255),ADD COLUMN Retweet_Ratio VARCHAR(255),ADD COLUMN Tweets_by_day_of_week VARCHAR(255),ADD COLUMN Sun VARCHAR(255),ADD COLUMN Mon VARCHAR(255),ADD COLUMN Tues VARCHAR(255),ADD COLUMN Wed VARCHAR(255),ADD COLUMN Thurs VARCHAR(255),ADD COLUMN Fri VARCHAR(255),ADD COLUMN Sat VARCHAR(255),ADD COLUMN Tweets_by_hour_of_day VARCHAR(255),ADD COLUMN 12AM VARCHAR(255),ADD COLUMN 1AM VARCHAR(255),ADD COLUMN 2AM VARCHAR(255),ADD COLUMN 3AM VARCHAR(255),ADD COLUMN 4AM VARCHAR(255),ADD COLUMN 5AM VARCHAR(255),ADD COLUMN 6AM VARCHAR(255),ADD COLUMN 7AM VARCHAR(255),ADD COLUMN 8AM VARCHAR(255),ADD COLUMN 9AM VARCHAR(255),ADD COLUMN 10AM VARCHAR(255),ADD COLUMN 11AM VARCHAR(255),ADD COLUMN 12PM VARCHAR(255),ADD COLUMN 1PM VARCHAR(255),ADD COLUMN 2PM VARCHAR(255),ADD COLUMN 3PM VARCHAR(255),ADD COLUMN 4PM VARCHAR(255),ADD COLUMN 5PM VARCHAR(255),ADD COLUMN 6PM VARCHAR(255),ADD COLUMN 7PM VARCHAR(255),ADD COLUMN 8PM VARCHAR(255),ADD COLUMN 9PM VARCHAR(255),ADD COLUMN 10PM VARCHAR(255),ADD COLUMN 11PM VARCHAR(255)'
                cursor2 = cnxn.cursor()
                cursor2.execute(query2)
                print("executed ------------------------------------")
                cnxn.commit()
                # Fetch all rows to avoid "Unread result found" error
                cursor2.fetchall() 
                results = [] 
        except Exception as e:
            print('ERROR',e)

        # Now getting the info
        # Define a SQL query to extract the "Usernames" column from the "groups1_info" table
        query3 = 'SELECT Username FROM after_feedback_groups1_info'

        # Execute the query and fetch the results
        cursor3 = cnxn.cursor()
        cursor3.execute(query3)
        usernames1 = [row[0] for row in cursor3.fetchall()]

        # Print the results
        print('Username from after_feedback_groups1_info:', usernames1)
        print("No. of Groups: ")
        print(len(usernames1))

        print('--------------------------')
        #############################
        list_of_columns = ['Bot_Score', 'Echo_Chamber','Fake_Followers','Financial','Self_Declared','Spammer','Most_Recent_Post','Likes_Count','Recent_tweets_per_week','Retweet_Ratio','Tweets_by_day_of_week','Sun','Mon','Tues','Wed','Thurs','Fri','Sat','Tweets_by_hour_of_day','12AM','1AM','2AM','3AM','4AM','5AM','6AM','7AM','8AM','9AM','10AM','11AM','12PM','1PM','2PM','3PM','4PM','5PM','6PM','7PM','8PM','9PM','10PM','11PM']
        
        for i ,ada in enumerate(usernames1):
            final_users=[]
            print('username1 ',usernames1[i])
            query4 = f"SELECT Usernames FROM after_feedback_groups1_info WHERE Username = '{usernames1[i]}'"

            # Execute the query and fetch the results
            cursor4 = cnxn.cursor()
            cursor4.execute(query4)
            usernames2 = list(cursor4.fetchall())
            final_users.append(usernames1[i])
            final_users.append(usernames2)
            print(final_users)
            # Print the results
            ##########################                                                          
            # making a list
            usernames_str = final_users[1][0][0]
            usernames_list = usernames_str.strip('"').split(',')
            usernames = [final_users[0]] + [username.strip('@') for username in usernames_list]
            new_final_users = usernames
            print(new_final_users)

            ###################33333
            bot_values = botometer_analysis(new_final_users,0,1,0,1)
            print('GOT THE RETURBN')
            print(bot_values)
            for j ,eee in enumerate(bot_values):
                if bot_values[j][0][0] != '@':
                    bot_values[j][0] = '@' + bot_values[j][0]

                #print("c[j] : ",bot_values[j][0])
                print("LENGHT OG Bot_values:",len(bot_values))
                print("LENGHT OG Bot_values[j]:",len(bot_values[j]))
                print("LENGHT OG Cloumns:",len(list_of_columns))
                
                for k in range(len(list_of_columns)):
                    print('I AM HERE SUCCESSFULLY')
                    query5 = f"UPDATE usersprofile_temp SET {list_of_columns[k]} = '{bot_values[j][k+1]}' WHERE Username = '{bot_values[j][0]}'"
                    cursor5 = cnxn.cursor()
                    cursor5.execute(query5)
                    cnxn.commit()      
        # Close the database connection
        print("Botometer Values Placed in SQL Successfully")

        cnxn.close()
    except Exception as e:
        print("!!! COULD NOT place Botometer Values in SQL, error : ",e)
        
