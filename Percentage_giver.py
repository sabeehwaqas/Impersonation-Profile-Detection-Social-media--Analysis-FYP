from locale import currency
import numpy as np
import pandas as pd
import mysql.connector
from datetime import datetime
import datetime
from scipy import spatial
import ast
import difflib
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import json
import os

# Download required nltk resources
 # Add this line to download the resource

def Jsonmaker(new_data):

    # Define the path and filename of the JSON file
    filename = "dataofprediction.json"
    path = "D:\\twitterprofiles\\"

    # Check if the file exists, if not, create it
    if not os.path.exists(os.path.join(path, filename)):
        with open(os.path.join(path, filename), "w") as f:
            json.dump([], f)

    # Load the existing data from the file
    with open(os.path.join(path, filename), "r") as f:
        data = json.load(f)

    # Clear the data in the file if it contains any
    if data:
        data.clear()

    # Append new data to the list of dictionaries
    #new_data = [{"name": "John", "age": 30}, {"name": "Jane", "age": 25}]
    data += new_data

    # Write the updated data to the file
    with open(os.path.join(path, filename), "w") as f:
        json.dump(data, f)


# A function to extract nouns and important keywords from a string
def extract_nouns_keywords(text):
    # Tokenize the text into words
    words = word_tokenize(text.lower())

    # Remove stop words from the words list
    stop_words = set(stopwords.words('english'))
    words = [w for w in words if not w in stop_words]

    # Lemmatize the words to reduce them to their base form
    lemmatizer = WordNetLemmatizer()
    words = [lemmatizer.lemmatize(w) for w in words]

    # Use part-of-speech tagging to identify nouns and important keywords
    tagged_words = nltk.pos_tag(words)
    nouns_keywords = [word for word, tag in tagged_words if tag.startswith('N') or tag.startswith('J')]

    return nouns_keywords

# A function to give a similarity score between two strings
def similarity_score(str1, str2):
    #Returns a similarity score between two strings
    seq_matcher = difflib.SequenceMatcher(None, str1, str2)
    return seq_matcher.ratio()

# A function 
def weighted_percentage(data, weight):
    for i, d in enumerate(data):
        if d == 'n/a':
            data[i] = 0
            weight[i] = 0
    total_weight = sum(weight)
    weighted_sum = sum([d * w for d, w in zip(data, weight)])
    if total_weight == 0:
        return 0
    else:
        percentage = (weighted_sum / total_weight) * 100
        return percentage
    
def date_diff(date_str):
    month_dict = {
        "January": 1,
        "February": 2,
        "March": 3,
        "April": 4,
        "May": 5,
        "June": 6,
        "July": 7,
        "August": 8,
        "September": 9,
        "October": 10,
        "November": 11,
        "December": 12
    }
    
    current_date = datetime.datetime.now()
    year = current_date.year
    month, joined_month = current_date.month, 0
    date_parts = date_str.split()
    
    if len(date_parts) == 3 and date_parts[0] == "Joined":
        joined_month = month_dict.get(date_parts[1], 0)
        if joined_month == 0:
            return None # invalid month name
        
        year = int(date_parts[2])
        
    else:
        return None # invalid date format
    
    joined_date = datetime.datetime(year=year, month=joined_month, day=1)
    time_diff = current_date - joined_date
    return int(time_diff.total_seconds())

def date_diff1(date_str):
    current_date = datetime.datetime.now()
    joined_date = datetime.datetime.strptime(date_str, '%a %b %d, %Y')
    time_diff = current_date - joined_date
    return int(time_diff.total_seconds())

def fan_detect_words(list):
    fan1 = False
    print('CHECK ',list)
    keywords = ['fan','fc',"parody",'fp']
    for i in range(len(list)):
        for j in range(len(keywords)):  
            keywords[j] = keywords[j].lower() 
            list[i] = list[i].lower()  
            if keywords[j] == list[i]: 
                fan1 =True
    return fan1
def fan_detect_letters(list):
    fan2= False
    group = ['fc','fan','parody','fp']
    for i in range(len(list)):
        for j in range(len(group)):
            if group[j] in list[i]: 
                fan2 =True
    return fan2

def fan_detect_overall(list):
    list1 = list.split()
    result1 = fan_detect_words(list1)
    #print("1 ",result1)

    result2 = fan_detect_letters(list1)
    #print("2 ",result2)
    
    return result1 or result2


def Rater(real,real_df,fake_df):
      
    # Connect to the MySQL Server
    host = 'localhost'
    database = 'sql_false_flag'
    user = 'root'
    password = 'Jaguar@123'
    cnxn = mysql.connector.connect(host=host, database=database, user=user, password=password)
    
        # Check if the "Prediction" column exists in the "usersprofile_temp" table
    cursor3 = cnxn.cursor()
    Q = "SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME='usersprofile_temp' AND COLUMN_NAME='Prediction'"
    cursor3.execute(Q)
    result = cursor3.fetchone()
    #print("result is :",result)
    # if yes then drop the prediction column from table
    if result == None :
        cursor3.execute("ALTER TABLE usersprofile_temp ADD COLUMN Prediction VARCHAR(255)")
    cnxn.commit()
    
    
    # add 100% to real profile Predition Column
    #print('I AM REAL: ',real)
    query3 = f"UPDATE usersprofile_temp SET Prediction = '100%' WHERE Username = '{real}'"
    cursor3 = cnxn.cursor()
    cursor3.execute(query3)
    cnxn.commit()

    #current_group_json = {"Username":real_df.iloc[0]['Username'],"Fullname":real_df.iloc[0]['Fullname'],"Location":real_df.iloc[0]['Location'],"Description":real_df.iloc[0]['Description'],"Followers":real_df.iloc[0]['Followers'],"Following":real_df.iloc[0]['Following'],"Join_Date":real_df.iloc[0]['Join_Date'],"Verfication_status":real_df.iloc[0]['Verfication_status'],"Lists":real_df.iloc[0]['Lists']}
    excluded_columns = ["Likes",'Sun', 'Mon', 'Tues', 'Wed', 'Thurs', 'Fri', 'Sat',
                    '12AM', '1AM', '2AM', '3AM', '4AM', '5AM', '6AM', '7AM',
                    '8AM', '9AM', '10AM', '11AM', '12PM', '1PM', '2PM', '3PM',
                    '4PM', '5PM', '6PM', '7PM', '8PM', '9PM', '10PM', '11PM']
    df = real_df.drop(excluded_columns, axis=1)

    # Convert the remaining dataframe to a dictionary
    Current_group_dict = df.to_dict('records')
    print("DICTIONARY HERE: ",Current_group_dict)
    print('REAL DF AFTER DICTIONARY ',real_df)
    #adding groups real user info into dictionary
    Current_group_dict = Current_group_dict[0]
    
    list_of_group_dict = []

    
    for z in range(len(fake_df)):
        SCORE = []
        # dict of current fake user details
        fake_user_dict = {}
        print('________________________________________________')
        
        name_fake = str(fake_df.iloc[z]['Fullname'])
        username_fake = str(fake_df.iloc[z]['Username']) 
        description_fake = str(fake_df.iloc[z]['Description'])
        fake_str_data = name_fake +" " + username_fake + " " + description_fake
        #print("THIS IS THE FAKE DATA",type(fake_str_data),fake_str_data)
        fan_flag = fan_detect_overall(fake_str_data)
        #print(f"FAN FLAG for {fake_df.iloc[z]['Username']} is: ",fan_flag)
        

        print("FAKE DF: ",fake_df)
        print("REal DF: ",real_df)
        

        #adding username of fake user details
        fake_data_columns = ['Username','Fullname','Location','Description','Followers','Following','Join_Date','Verification_status','Lists','Birthday','Profession','Tweets','Website','Bot_Score','Echo_Chamber','Fake_Followers','Financial','Self_Declared','Spammer','Most_Recent_Post','Likes_Count','Recent_tweets_per_week','Retweet_Ratio','Tweets_by_day_of_week','Tweets_by_hour_of_day']
        
        for i in fake_data_columns:
            print("#############################################")
            print(fake_df.iloc[z][i])

            print("#############################################")
    


            fake_user_dict[i]=str(fake_df.iloc[z][i])
         

        



    
    ########## Username Score ############
        print('***** ***** NOW Username')
        UName1 = real_df.iloc[0]['Username']
        #print("UNAME1 : ",UName1)
        
        UName2 = fake_df.iloc[z]['Username']
        #print("UNAME2 : ",UName2)
        
        #handling NA,n/a,null
        if (UName1 == 'NA' or UName1 =='n/a' or UName1 == 'null') and (UName2 != 'NA' and UName2 !='n/a' and UName2 != 'null'):
            print('Not Possible')
            score = 'n/a'
        elif (UName1 != 'NA' and UName1 !='n/a' and UName1 != 'null') and (UName2 == 'NA' or UName2 =='n/a' or UName2 == 'null'):
            print('Bad Fake Account')
            score = 0
        elif (UName1 == 'NA' or UName1 =='n/a' or UName1 == 'null') and (UName2 == 'NA' or UName2 =='n/a' or UName2 == 'null'):
            score = 'n/a'
        else:
            score = similarity_score(UName1, UName2)
        print("UserName Similarity: ",score)
        SCORE.append(score)
        fake_user_dict['Username_Similarity']=score


        
    ########## Name Score ################
        print("***** NOW NAME")
        Name1 = real_df.iloc[0]['Fullname']
        #print("NAME1 : ",Name1)
        
        Name2 = fake_df.iloc[z]['Fullname']
        #print("NAME2 : ",Name2)
        
        #handling NA,n/a,null
        if (Name1 == 'NA' or Name1 =='n/a' or Name1 == 'null') and (Name2 != 'NA' and Name2 !='n/a' and Name2 != 'null'):
            print('Not Possible')
            score = 'n/a'
        elif (Name1 != 'NA' and Name1 !='n/a' and Name1 != 'null') and (Name2 == 'NA' or Name2 =='n/a' or Name2 == 'null'):
            print('Bad Fake Account')
            score = 0
        elif (Name1 == 'NA' or Name1 =='n/a' or Name1 == 'null') and (Name2 == 'NA' or Name2 =='n/a' or Name2 == 'null'):
            score = 'n/a'
        else:
            score = similarity_score(Name1,Name2)
        print('Name Similarity: ',score)
        SCORE.append(score)
        fake_user_dict['Name_Similarity']=score
        
        
    ########## Location ##################
    
        
        print("***** NOW Location")
        Loc1 = real_df.iloc[0]['Location']
        #print("Loc1 : ",Loc1)
        
        Loc2 = fake_df.iloc[z]['Location']
        #print("Loc2 : ",Loc2)
        
        #handling NA,n/a,null
        if (Loc1 == 'NA' or Loc1 =='n/a' or Loc1 == 'null') and (Loc2 != 'NA' and Loc2 !='n/a' and Loc2 != 'null'):
            print('Not Possible')
            score = 'n/a'
        elif (Loc1 != 'NA' and Loc1 !='n/a' and Loc1 != 'null') and (Loc2 == 'NA' or Loc2 =='n/a' or Loc2 == 'null'):
            print('Bad Fake Account')
            score = 0
        elif (Loc1 == 'NA' or Loc1 =='n/a' or Loc1 == 'null') and (Loc2 == 'NA' or Loc2 =='n/a' or Loc2 == 'null'):
            score = 'n/a'
            
        else:          
            score = similarity_score(Loc1,Loc2)
        print('Location Similarity: ',score)
        SCORE.append(score)
        fake_user_dict['Location_Similarity']=score
            
    ############# Description Score ###############
        print("***** NOW Description")
        Des1 = real_df.iloc[0]['Description']
        #print("Des1 : ",Des1)
        
        Des2 = fake_df.iloc[z]['Description']
        #print("Des2 : ",Des2)
        
        #handling NA,n/a,null
        if (Des1 == 'NA' or Des1 =='n/a' or Des1 == 'null') and (Des2 != 'NA' and Des2 !='n/a' and Des2 != 'null'):
            print('Not Possible')
            count = 'n/a'
        elif (Des1 != 'NA' and Des1 !='n/a' and Des1 != 'null') and (Des2 == 'NA' or Des2 =='n/a' or Des2 == 'null'):
            print('Bad Fake Account')
            count = 0
        elif (Des1 == 'NA' or Des1 =='n/a' or Des1 == 'null') and (Des2 == 'NA' or Des2 =='n/a' or Des2 == 'null'):
            count = 'n/a'
        else:          
        
            Des1 = extract_nouns_keywords(Des1)
            Des2 = extract_nouns_keywords(Des2)
            
            count = 0
            for p in range(len(Des1)):
                for q in range(len(Des2)):
                    if Des1[p] == Des2[q]:
                        count = count + 1
            count = count/len(Des1)
        print('COUNT: ',count)
        SCORE.append(count)
        fake_user_dict['Description_Similarity']=score
        
                    
    ############# Followers Score ################    
        print("***** NOW Followers")
        F1 = real_df.iloc[0]['Followers']
        #print("Followers1 : ",F1)
        
        F2 = fake_df.iloc[z]['Followers']
        #print("Followers2 : ",F2)
        
        #handling NA,n/a,null
        MF = False
        if (F1 == 'NA' or F1 =='n/a' or F1 == 'null') and (F2 != 'NA' and F2 !='n/a' and F2 != 'null'):
            print('Not Possible')
            score = 'n/a'
        elif (F1 != 'NA' and F1 !='n/a' and F1 != 'null') and (F2 == 'NA' or F2 =='n/a' or F2 == 'null'):
            print('Bad Fake Account')
            score = 0
        elif (F1 == 'NA' or F1 =='n/a' or F1 == 'null') and (F2 == 'NA' or F2 =='n/a' or F2 == 'null'):
            score = 'n/a'
        else:
                    
            if F1 == F2:
                score = 1.0
            elif F1 > F2:
                score = float(F2) / float(F1)
            else:
                score = float(F1) / float(F2) * 10   # multipyong iwth 10 because if fake has more followers than real account than it is more mimicing the real
                MF = True
                diff_followers = F2 - F1
                
        print('Followers count = ',score)
        SCORE.append(score)
        fake_user_dict['Followers_Count_Similarity']=score
        
        
        ############# Following Score ################    
        print("***** NOW Following")
        FF1 = real_df.iloc[0]['Following']
        #print("Following1 : ",FF1)
        
        FF2 = fake_df.iloc[z]['Following']
        #print("Following2 : ",FF2)
        
        #handling NA,n/a,null
        if (FF1 == 'NA' or FF1 =='n/a' or FF1 == 'null') and (FF2 != 'NA' and FF2 !='n/a' and FF2 != 'null'):
            print('Not Possible')
            score = 'n/a'
        elif (FF1 != 'NA' and FF1 !='n/a' and FF1 != 'null') and (FF2 == 'NA' or FF2 =='n/a' or FF2 == 'null'):
            print('Bad Fake Account')
            score = 0
        elif (FF1 == 'NA' or FF1 =='n/a' or FF1 == 'null') and (FF2 == 'NA' or FF2 =='n/a' or FF2 == 'null'):
            score = 'n/a'
        
        else:
                    
            if FF1 == FF2:
                score = 1.0
            elif FF1 > FF2:
                score = float(FF2) / float(FF1)
            else:
                score = float(FF1) / float(FF2)
                
        print('Following count = ',score)
        SCORE.append(score)
        fake_user_dict['Following_Count_Similarity']=score
        
        ############# Following / Followers ratio Score ################    
        print("***** NOW Following")
        
        F1 = real_df.iloc[0]['Followers']
        #print("Following1 : ",F1)
        #print("***** NOW Following")
        FF1 = real_df.iloc[0]['Following']
        #print("Followers1 : ",FF1)
        
        F2 = fake_df.iloc[z]['Followers']
        #print("Followers2 : ",F2)
        FF2 = fake_df.iloc[z]['Following']
        #print("Following2 : ",FF2)
        
        if (FF1 == 'NA' or FF1 =='n/a' or FF1 == 'null') and (FF2 != 'NA' and FF2 !='n/a' and FF2 != 'null'):
            print('Not Possible')
            score = 'n/a'
        elif (FF1 != 'NA' and FF1 !='n/a' and FF1 != 'null') and (FF2 == 'NA' or FF2 =='n/a' or FF2 == 'null'):
            print('Bad Fake Account')
            score = 0
        elif (FF1 == 'NA' or FF1 =='n/a' or FF1 == 'null') and (FF2 == 'NA' or FF2 =='n/a' or FF2 == 'null'):
            score = 'n/a'
        elif (F1 == 'NA' or F1 =='n/a' or F1 == 'null') and (F2 != 'NA' and F2 !='n/a' and F2 != 'null'):
            print('Not Possible')
            score = 'n/a'
        elif (F1 != 'NA' and F1 !='n/a' and F1 != 'null') and (F2 == 'NA' or F2 =='n/a' or F2 == 'null'):
            print('Bad Fake Account')
            score = 0
        elif (F1 == 'NA' or F1 =='n/a' or F1 == 'null') and (F2 == 'NA' or F2 =='n/a' or F2 == 'null'):
            score = 'n/a'
        else:            
        
            ratio1 = float(FF1)/float(F1)
            #print("Ratio1: ",ratio1)
            
            ratio2 = float(FF2)/float(F2)
            #print("Ratio2: ",ratio2)           

            if ratio1 == ratio2:
                score = 1.0
            elif ratio1 > ratio2:
                score = float(ratio2) / float(ratio1)
            else:
                score = float(ratio1) / float(ratio2)
            
        print('RATIO count = ',score)
        SCORE.append(score)
        fake_user_dict['Following/Followers_Ratio_Similarity']=score
        
    ############# Join DAte #####################3
    
        print("***** NOW joining date")
        Join1 = real_df.iloc[0]['Join_Date']
        print("Date1 : ",Join1)
        
        Join2 = fake_df.iloc[z]['Join_Date']
        print("Date2 : ",Join2)
        
        #Handling NA,n/a,null
        if (Join1 == 'NA' or Join1 =='n/a' or Join1 == 'null') and (Join2 != 'NA' and Join2 !='n/a' and Join2 != 'null'):
            print('Not Possible')
            score = 'n/a'
        elif (Join1 != 'NA' and Join1 !='n/a' and Join1 != 'null') and (Join2 == 'NA' or Join2 =='n/a' or Join2 == 'null'):
            print('Bad Fake Account')
            score = 0
        elif (Join1 == 'NA' or Join1 =='n/a' or Join1 == 'null') and (Join2 == 'NA' or Join2 =='n/a' or Join2 == 'null'):
            score = 'n/a'
        else:
            # Example usage:
            date1 = Join1
            date2 = Join2

            seconds_diff1 = date_diff(date1)
            seconds_diff2 = date_diff(date2)

            print(f"Seconds difference1: {seconds_diff1}")

            print(f"Seconds difference2: {seconds_diff2}")

            if seconds_diff1 == seconds_diff2:
                score = 1
            elif seconds_diff2 > seconds_diff1:
                score = 1.5
            elif seconds_diff1 > seconds_diff2:
                score =1- (seconds_diff1-seconds_diff2)/seconds_diff1
                
        print('Date Difference = ',score)
        SCORE.append(score)
        fake_user_dict['Join_Date_Similarity']=score
        
        
        ########## Verification ##############
        print("***** ***** NOW Birthday")
        vs1 = real_df.iloc[0]['Verification_status']
        #print("Loc1 : ",Loc1)
        
        vs2 = fake_df.iloc[z]['Verification_status']
        #print("Loc2 : ",Loc2)
        
        # proceed only if we have verified fake account
        if vs2 == 1 and vs1 == 1:
            score = 5
            V = True
        if vs2 == 1 and vs1 != 1:
            score = 100
            V = True
        if vs2 != 1 and vs1 != 1:
            score = 'n/a'
            V = False
        if vs2 !=1 and vs1 == 1:
            score = 0
            V = False
        print('Verification = ',score)
        SCORE.append(score)
        fake_user_dict['Verfication_Score']=score
            
        
        
        
       
                    
        
        ########## Birthday ##################
    
        
        print("***** ***** NOW Birthday")
        Bd1 = real_df.iloc[0]['Birthday']
        #print("Loc1 : ",Loc1)
        
        Bd2 = fake_df.iloc[z]['Birthday']
        #print("Loc2 : ",Loc2)
        
        #Handling NA,n/a,null
        if (Bd1 == 'NA' or Bd1 =='n/a' or Bd1 == 'null') and (Bd2 != 'NA' and Bd2 !='n/a' and Bd2 != 'null'):
            print('Not Possible')
            score = 'n/a'
        elif (Bd1 != 'NA' and Bd1 !='n/a' and Bd1 != 'null') and (Bd2 == 'NA' or Bd2 =='n/a' or Bd2 == 'null'):
            print('Bad Fake Account')
            score = 0
        elif (Bd1 == 'NA' or Bd1 =='n/a' or Bd1 == 'null') and (Bd2 == 'NA' or Bd2 =='n/a' or Bd2 == 'null'):
            score = 'n/a'
        else:
        
            if Bd1 == 'n/a':
                score = 'n/a'    
            elif Bd1 != 'n/a' and Bd2 == 'n/a':
                score = 0
            elif Bd1 != 'n/a' and Bd2 !='n/a':            
                score = similarity_score(Bd1,Bd2)
        print('Birthday Similarity: ',score)
        SCORE.append(score)
        fake_user_dict['Birthday_Similarity']=score
        
        
        ########## Profession ##################
    
        
        print("***** ***** NOW Profession")
        Pf1 = real_df.iloc[0]['Profession']
        #print("Loc1 : ",Loc1)
        
        Pf2 = fake_df.iloc[z]['Profession']
        #print("Loc2 : ",Loc2)
        
        #Handling NA,n/a,null
        if (Pf1 == 'NA' or Pf1 =='n/a' or Pf1 == 'null') and (Pf2 != 'NA' and Pf2 !='n/a' and Pf2 != 'null'):
            print('Not Possible')
            score = 'n/a'
        elif (Pf1 != 'NA' and Pf1 !='n/a' and Pf1 != 'null') and (Pf2 == 'NA' or Pf2 =='n/a' or Pf2 == 'null'):
            print('Bad Fake Account')
            score = 0
        elif (Pf1 == 'NA' or Pf1 =='n/a' or Pf1 == 'null') and (Pf2 == 'NA' or Pf2 =='n/a' or Pf2 == 'null'):
            score = 'n/a'
        else:
        
            if Pf1 == 'n/a':
                score = 'n/a'

            elif Pf1 != 'n/a' and Pf2 == 'n/a':
                score = 0
            elif Pf1 != 'n/a' and Pf2 !='n/a':            
                score = similarity_score(Pf1,Pf2)
        print('Profession Similarity: ',score)
        SCORE.append(score)
        fake_user_dict['Profession_Similarity']=score
        
        
        
        ############# List Score ################    
        print("***** NOW List")
        list1 = real_df.iloc[0]['Lists']
        #print("Followers1 : ",F1)
        
        list2 = fake_df.iloc[z]['Lists']
        #print("Followers2 : ",F2)
        
        #Handling NA,n/a,null
        if (list1 == 'NA' or list1 =='n/a' or list1 == 'null') and (list2 != 'NA' and list2 !='n/a' and list2 != 'null'):
            print('Not Possible')
            score = 'n/a'
        elif (list1 != 'NA' and list1 !='n/a' and list1 != 'null') and (list2 == 'NA' or list2 =='n/a' or list2 == 'null'):
            print('Bad Fake Account')
            score = 0
        elif (list1 == 'NA' or list1 =='n/a' or list1 == 'null') and (list2 == 'NA' or list2 =='n/a' or list2 == 'null'):
            score = 'n/a'
        else:
                    
            if list1 == list2:
                score = 1.0
            elif list1 > list2:
                score = float(list2) / float(list1)
            else:
                score = float(list1) / float(list2)
            
        print('List = ',score)
        SCORE.append(score)
        fake_user_dict['List_Similarity']=score
        
        ############# Likes Score ################    
        print("***** NOW Likes")
        likes1 = real_df.iloc[0]['Likes_Count']
        #print("Followers1 : ",F1)


        
        likes2 = fake_df.iloc[z]['Likes_Count']
        #print("Followers2 : ",F2)

        
        
        #handling NA,n/a,null
        if (likes1 == 'NA' or likes1 =='n/a' or likes1 == 'null') and (likes2 != 'NA' and likes2 !='n/a' and likes2 != 'null'):
            print('Not Possible')
            score = 'n/a'
        elif (likes1 != 'NA' and likes1 !='n/a' and likes1 != 'null') and (likes2 == 'NA' or likes2 =='n/a' or likes2 == 'null'):
            print('Bad Fake Account')
            score = 0
        elif (likes1 == 'NA' or likes1 =='n/a' or likes1 == 'null') and (likes2 == 'NA' or likes2 =='n/a' or likes2 == 'null'):
            score = 'n/a'
        else:

            likes1 = likes1.replace(',', '')
            # Convert the string to a float
            likes1 = float(likes1)

            likes2 = likes2.replace(',', '')
            # Convert the string to a float
            likes2 = float(likes2)
                    
            if likes1 == likes2:
                score = 1.0
            elif likes1 > likes2:
                score = float(likes2) / float(likes1)
            else:
                score = float(likes1) / float(likes2)
            
        print('Likes = ',score)
        SCORE.append(score)
        fake_user_dict['Likes_Similarity']=score


        ############# Tweets Score ################    
        print("***** ***** NOW Tweets")
        Tw1 = real_df.iloc[0]['Tweets']
        print("Tweets1 : ",Tw1)
        
        Tw2 = fake_df.iloc[z]['Tweets']
        print("Tweets2 : ",Tw2)
        
        #handling NA,n/a,null
        if (Tw1 == 'NA' or Tw1 =='n/a' or Tw1 == 'null') and (Tw2 != 'NA' and Tw2 !='n/a' and Tw2 != 'null'):
            print('Not Possible')
            score = 'n/a'
        elif (Tw1 != 'NA' and Tw1 !='n/a' and Tw1 != 'null') and (Tw2 == 'NA' or Tw2 =='n/a' or Tw2 == 'null'):
            print('Bad Fake Account')
            score = 0
        elif (Tw1 == 'NA' or Tw1 =='n/a' or Tw1 == 'null') and (Tw2 == 'NA' or Tw2 =='n/a' or Tw2 == 'null'):
            score = 'n/a'
        else:
                    
            if Tw1 == Tw2:
                score = 1.0
            elif Tw1 > Tw2:
                score = float(Tw2) / float(Tw1)
            else:
                score = float(Tw1) / float(Tw2)
            
        print('Tweets count = ',score)
        SCORE.append(score)
        fake_user_dict['Tweets_Count_Similarity']=score
        
        
        
        
        ########## Website ##################
    
        
        print("***** ***** NOW Website")
        Wb1 = real_df.iloc[0]['Website']
        #print("Loc1 : ",Loc1)
        
        Wb2 = fake_df.iloc[z]['Website']
        #print("Loc2 : ",Loc2)
        
        #handling NA,n/a,null
        if (Wb1 == 'NA' or Wb1 =='n/a' or Wb1 == 'null') and (Wb2 != 'NA' and Wb2 !='n/a' and Wb2 != 'null'):
            print('Not Possible')
            score = 'n/a'
        elif (Wb1 != 'NA' and Wb1 !='n/a' and Wb1 != 'null') and (Wb2 == 'NA' or Wb2 =='n/a' or Wb2 == 'null'):
            print('Bad Fake Account')
            score = 0
        elif (Wb1 == 'NA' or Wb1 =='n/a' or Wb1 == 'null') and (Wb2 == 'NA' or Wb2 =='n/a' or Wb2 == 'null'):
            score = 'n/a'
        else:
        
            if Wb1 == 'n/a':
                score = 'n/a'
            elif Wb1 != 'n/a' and Wb2 == 'n/a':
                score = 0
            elif Wb1 != 'n/a' and Wb2 !='n/a':            
                score = similarity_score(Wb1,Wb2)
                
        print('Website Similarity: ',score)
        SCORE.append(score)
        fake_user_dict['Website_Link_Similarity']=score
        
        
        BOTO = ['Bot_Score','Echo_Chamber','Fake_Followers','Financial','Self_Declared','Spammer']
        for bot in range(len(BOTO)):
        ################### Bot SCore ###################3
            print(f"***** ***** NOW {BOTO[bot]}")
            BS1 = real_df.iloc[0][BOTO[bot]]
            print(f"{BOTO[bot]}1 : ",BS1)
            
            BS2 = fake_df.iloc[z][BOTO[bot]]
            print(f"{BOTO[bot]}2 : ",BS2)
            
            #handling NA,n/a,null
            if (BS1 == 'NA' or BS1 =='n/a' or BS1 == 'null') and (BS2 != 'NA' and BS2 !='n/a' and BS2 != 'null'):
                print('Not Possible')
                score = 'n/a'
            elif (BS1 != 'NA' and BS1 !='n/a' and BS1 != 'null') and (BS2 == 'NA' or BS2 =='n/a' or BS2 == 'null'):
                print('Bad Fake Account')
                score = 0
            elif (BS1 == 'NA' or BS1 =='n/a' or BS1 == 'null') and (BS2 == 'NA' or BS2 =='n/a' or BS2 == 'null'):
                score = 'n/a'
            else:
                                
                Cal1 = (float(BS1) - 0) / (5 - 0)
                #print("CAL1 : ",Cal1)
                Cal2 = (float(BS2) - 0) / (5 - 0)
                
            print("CAL2 : ",Cal2)
            SCORE.append(Cal2)
            fake_user_dict[f"{BOTO[bot]}_Similarity"]=score
            
            ########## ratio of bot score ###########
            
            #handling NA,n/a,null
            if (BS1 == 'NA' or BS1 =='n/a' or BS1 == 'null') and (BS2 != 'NA' and BS2 !='n/a' and BS2 != 'null'):
                print('Not Possible')
                score = 'n/a'
            elif (BS1 != 'NA' and BS1 !='n/a' and BS1 != 'null') and (BS2 == 'NA' or BS2 =='n/a' or BS2 == 'null'):
                print('Bad Fake Account')
                score = 0
            elif (BS1 == 'NA' or BS1 =='n/a' or BS1 == 'null') and (BS2 == 'NA' or BS2 =='n/a' or BS2 == 'null'):
                score = 'n/a'
            else:
            
                if Cal1 == Cal2:
                    score = 1.0
                elif Cal1 > Cal2:
                    if Cal1 != 0:                        
                        score = float(Cal2) / float(Cal1)
                    else:
                        score = 'n/a'
                else:
                    if Cal2 != 0:                        
                        score = float(Cal1) / float(Cal2)
                    else:
                        score = 'n/a'
                
            print(f'Ratio_{BOTO[bot]}', score)
            SCORE.append(score)
            fake_user_dict[f"{BOTO[bot]}_Ratio_Similarity"]=score
            
            
            
        ##################'Most_Recent_Post'######################

    
        print("***** NOW Most recent post")
        post1 = real_df.iloc[0]['Most_Recent_Post']
        print("Recent post1 : ",post1)
        
        post2 = fake_df.iloc[z]['Most_Recent_Post']
        print("Recent post2 : ",post2)
        
        #handling NA,n/a,null
        if (post1 == 'NA' or post1 =='n/a' or post1 == 'null') and (post2 != 'NA' and post2 !='n/a' and post2 != 'null'):
            print('Not Possible')
            score = 'n/a'
        elif (post1 != 'NA' and post1 !='n/a' and post1 != 'null') and (post2 == 'NA' or post2 =='n/a' or post2 == 'null'):
            print('Bad Fake Account')
            score = 0
        elif (post1 == 'NA' or post1 =='n/a' or post1 == 'null') and (post2 == 'NA' or post2 =='n/a' or post2 == 'null'):
            score = 'n/a'
        else:
                        
            date1 = post1
            date2 = post2
            seconds_diff1 = date_diff1(date1)
            seconds_diff2 = date_diff1(date2)
            print(f"Seconds difference1: {seconds_diff1}")
            print(f"Seconds difference2: {seconds_diff2}")

            if seconds_diff1 == seconds_diff2:
                score = 1
            elif seconds_diff1 > seconds_diff2:
                score = 1.5
            elif seconds_diff2 > seconds_diff1:
                score = 1 -((seconds_diff2 -seconds_diff1)/seconds_diff2)

        print('Recent post Difference = ',score)
        SCORE.append(score)
        fake_user_dict['Recent_Post_Similarity']=score

                    
        #####3333
        #############33'Recent_tweets_per_week'############33
        print("***** ***** NOW Recent_tweets_per_week")
        Tw1 = real_df.iloc[0]['Recent_tweets_per_week']
        print("Recent_tweets_per_week1 : ",Tw1)
        
        Tw2 = fake_df.iloc[z]['Recent_tweets_per_week']
        print("Recent_tweets_per_week2 : ",Tw2)
        
        #handling NA,n/a,null
        if (Tw1 == 'NA' or Tw1 =='n/a' or Tw1 == 'null') and (Tw2 != 'NA' and Tw2 !='n/a' and Tw2 != 'null'):
            print('Not Possible')
            score = 'n/a'
        elif (Tw1 != 'NA' and Tw1 !='n/a' and Tw1 != 'null') and (Tw2 == 'NA' or Tw2 =='n/a' or Tw2 == 'null'):
            print('Bad Fake Account')
            score = 0
        elif (Tw1 == 'NA' or Tw1 =='n/a' or Tw1 == 'null') and (Tw2 == 'NA' or Tw2 =='n/a' or Tw2 == 'null'):
            score = 'n/a'
        else:
                    
            if Tw1 == Tw2:
                score = 1.0
            elif Tw1 > Tw2:
                score = float(Tw2) / float(Tw1)
            else:
                score = float(Tw1) / float(Tw2)
                
        print('Recent_tweets_per_week count = ',score)
        SCORE.append(score)
        fake_user_dict['Recent_Tweets_per_week_count_Similarity']=score
        
        #'Retweet_Ratio'
        print("***** ***** NOW Retweet_Ratio")
        Tw1 = real_df.iloc[0]['Retweet_Ratio']
        print("Retweet_Ratio1 : ",Tw1)
        
        Tw2 = fake_df.iloc[z]['Retweet_Ratio']
        print("Retweet_Ratio2 : ",Tw2)
        
        #handling NA,n/a,null
        if (Tw1 == 'NA' or Tw1 =='n/a' or Tw1 == 'null') and (Tw2 != 'NA' and Tw2 !='n/a' and Tw2 != 'null'):
            print('Not Possible')
            score = 'n/a'
        elif (Tw1 != 'NA' and Tw1 !='n/a' and Tw1 != 'null') and (Tw2 == 'NA' or Tw2 =='n/a' or Tw2 == 'null'):
            print('Bad Fake Account')
            score = 0
        elif (Tw1 == 'NA' or Tw1 =='n/a' or Tw1 == 'null') and (Tw2 == 'NA' or Tw2 =='n/a' or Tw2 == 'null'):
            score = 'n/a'
        else:
                    
            if Tw1 == Tw2:
                score = 1.0
            elif Tw1 > Tw2:
                score = float(Tw2) / float(Tw1)
            else:
                score = float(Tw1) / float(Tw2)
            
        print('Retweet_Ratio count = ',score)
        SCORE.append(score)
        fake_user_dict['Retweet_Ratio_Similarity']=score
            
        ##################### 'Tweets_by_day_of_week' ##########33
        
        print("***** ***** NOW 'Tweets_by_day_of_week'")
        week1 = real_df.iloc[0]['Tweets_by_day_of_week']
       

        #print("week1 : ",week1)

        week2 = fake_df.iloc[z]['Tweets_by_day_of_week']
        

        #handling NA,n/a,null
        if (week1 == 'NA' or week1 =='n/a' or week1 == 'null') and (week2 != 'NA' and week2 !='n/a' and week2 != 'null'):
            print('Not Possible')
            score = 'n/a'
        elif (week1 != 'NA' and week1 !='n/a' and week1 != 'null') and (week2 == 'NA' or week2 =='n/a' or week2 == 'null'):
            print('Bad Fake Account')
            score = 0
        elif (week1 == 'NA' or week1 =='n/a' or week1 == 'null') and (week2 == 'NA' or week2 =='n/a' or week2 == 'null'):
            score = 'n/a'
        else:
            week1 = my_list = ast.literal_eval(week1)
            week2 = my_list = ast.literal_eval(week2)
            
            # calculate cosine similarity between the two users' tweet activity
            cosine_sim = 1 - spatial.distance.cosine(week1, week2)

        # print the cosine similarity score
        print("Tweets_by_day_of_week similarity score: ", cosine_sim)
        SCORE.append(cosine_sim)
        fake_user_dict['Tweets_by_day_of_week_Similarity']=cosine_sim
        
        
        ##################### 'Tweets_by_hour_of_day' ##########33
        
        print("***** ***** NOW 'Tweets_by_hour_of_day'")
        day1 = real_df.iloc[0]['Tweets_by_hour_of_day']
        

        #print("week1 : ",week1)

        day2 = fake_df.iloc[z]['Tweets_by_hour_of_day']
        

        #handling NA,n/a,null
        if (day1 == 'NA' or day1 =='n/a' or day1 == 'null') and (day2 != 'NA' and day2 !='n/a' and day2 != 'null'):
            print('Not Possible')
            score = 'n/a'
        elif (day1 != 'NA' and day1 !='n/a' and day1 != 'null') and (day2 == 'NA' or day2 =='n/a' or day2 == 'null'):
            print('Bad Fake Account')
            score = 0
        elif (day1 == 'NA' or day1 =='n/a' or day1 == 'null') and (day2 == 'NA' or day2 =='n/a' or day2 == 'null'):
            score = 'n/a'
        else: 
            day1 = my_list = ast.literal_eval(day1)
            day2 = my_list = ast.literal_eval(day2)
            # calculate cosine similarity between the two users' tweet activity
            cosine_sim = 1 - spatial.distance.cosine(day1, day2)

        # print the cosine similarity score
        print("Tweets_by_hour_of_day similarity score: ", cosine_sim)
        SCORE.append(cosine_sim)
        fake_user_dict['Tweets_by_hour_of_day_Similarity']=cosine_sim
    
    
        #Final list of campared values
        #print('SCORE IS :',SCORE)
        #print('LEN :',len(SCORE))
        data = SCORE
        
        #'Username','Fullname','Location','Description','Followers','Following','F F ratio,'Profession','Lists','Likes','Tweets','Website','Bot_Score',ratio,'Echo_Chamber',ratio,'Fake_Followers',ratio,'Financial',ratio,'Self_Declared',ratio,'Spammer',ratio,'Recent_tweets_per_week','Retweet_Ratio','Tweets_by_day_of_week','Tweets_by_hour_of_day'
        #weight = [10,1, 1, 0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1]
        
        if fan_flag == True:
            not_fan = 0
        else:
            not_fan = 1
        SCORE.append(not_fan)
        
        Username = 2.0
        Fullname = 2.0
        Location = 0.2
        Description = 1.0
        Followers = 1.0
        Following = 1.0
        F_F_ratio = 1.0
        joindate = 1.0
        verified = 10.0
        Birthday = 0.5
        Profession = 0.2
        Lists = 1.0
        Likes = 1.0
        Tweets = 0.7
        Website = 0.2
        Bot_Score = 2.0
        ratio1 = 0.5
        Echo_Chamber = 0.5
        ratio2 = 0.2
        Fake_Followers = 0.5
        ratio3 = 0.2
        Financial = 0.5
        ratio4 = 0.2
        Self_Declared = 0.5
        ratio5 = 0.2
        Spammer = 0.2
        ratio6 = 0.2
        MRT = 1.0
        Recent_tweets_per_week = 0.5
        Retweet_Ratio = 0.5
        Tweets_by_day_of_week = 1.0
        Tweets_by_hour_of_day = 1.0
        fan = 10
        
        weight = [Username,Fullname,Location,Description,Followers,Following,F_F_ratio,joindate,verified,Birthday,Profession,Lists,Likes,Tweets,Website,Bot_Score,ratio1,Echo_Chamber,ratio2,Fake_Followers,ratio3,Financial,ratio4,Self_Declared,ratio5,Spammer,ratio6,MRT,Recent_tweets_per_week,Retweet_Ratio,Tweets_by_day_of_week,Tweets_by_hour_of_day,fan]

        #print('LEN :',len(weight))
        percentage = weighted_percentage(data, weight)
        #message list to display on website
        MSG_list =[]
        print('.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-..-.-.-.-.-.-.-.-.-.-.-.-.-.-.-..-.-.-.-.-.-.-.')
        print(f"for ",fake_df.iloc[z]['Username']," the Score is :",percentage, " %")
        if fan_flag:
            print('')
            print("- Its a decalred Fan or parody account")
            MSG_list.append("- Its a decalred Fan or parody account")
        if V == True:
            print('- This account if verified')
            MSG_list.append("- This account if verified")
        if MF == True:
            print(f'- This account has {diff_followers} more followers than the real account')
            MSG_list.append(f'- This account has {diff_followers} more followers than the real account')
        print('.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-..-.-.-.-.-.-.-.-.-.-.-.-.-.-.-..-.-.-.-.-.-.-.')
        fake_user_dict['Percentage']=percentage
        
        fake_user_dict['Details']=MSG_list
        print('CURRENT FAKE USER DICTIONARY: ',fake_user_dict)
        #adding the dictionary in the "LIST" key of current group 
        list_of_group_dict.append(fake_user_dict)

        

        #print("EFB3eyorfbqeofoqfybqerufb")
        query11 = f"UPDATE usersprofile_temp SET Prediction = {percentage} WHERE username = '{fake_df.iloc[z]['Username']}'"
        # Execute the query and fetch the results
        cursor11 = cnxn.cursor()
        cursor11.execute(query11)
        cnxn.commit()
        #print("EFB3eyorfbqeofoqfybqerufb")
    print("THIS IS THE LIST OF GROUP DICT: ",list_of_group_dict)
    print('Current group dic ',Current_group_dict)
    Current_group_dict['List1']=list_of_group_dict
    return Current_group_dict
    cnxn.commit()

    
    
    

def Percentage_giver():
    nltk.download('punkt')
    nltk.download('stopwords')
    nltk.download('wordnet')
    nltk.download('averaged_perceptron_tagger') 
    # Connect to the MySQL Server
    host = 'localhost'
    database = 'sql_false_flag'
    user = 'root'
    password = 'Jaguar@123'
    cnxn = mysql.connector.connect(host=host, database=database, user=user, password=password)

    # Execute the query and fetch the results
    query3 = 'SELECT Username FROM after_feedback_groups1_info'
    cursor3 = cnxn.cursor()
    cursor3.execute(query3)
    usernames1 = [row[0] for row in cursor3.fetchall()]

    #### print("USERNAME1: ",usernames1)
    #### USERNAME1:  ['@omarcheemapti', '@ocheema1231', '@vivantive', '@ocheema1231', '@omarcheema35', '@momarcheema', '@omarcheema1996', '@1231umar']


    # Check if the "Prediction" column exists in the "usersprofile_temp" table
    cursor3 = cnxn.cursor()
    Q = "SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME='usersprofile_temp' AND COLUMN_NAME='Prediction'"
    cursor3.execute(Q)
    result = cursor3.fetchone()
    #print('RESULT !',result)
    # if yes then drop the prediction column from table
    if result:
        cursor3.execute("ALTER TABLE usersprofile_temp DROP COLUMN Prediction")
    cnxn.commit()


    #all group list of result
    all_group_json = []

    # taking each @username from the username1 list
    final_json=[]
    for i in range(len(usernames1)):
    #for i in range(2):

        final_users=[]
        #print('username1 ',usernames1[i])
        #### username1[0] : @omarcheemapti

        # fetch group @usernames
        query1 = f"SELECT Usernames FROM after_feedback_groups1_info WHERE Username = '{usernames1[i]}'"
        cursor1 = cnxn.cursor()
        cursor1.execute(query1)
        usernames2 = list(cursor1.fetchall())
        #### print("username2 :",usernames2)
        #### username2 : [('"@omercheemapti,@omarsarfarazpti,@omarsarfarzpti,@omercheemaptl,@omarcheemapti,@amuhammadk,@omarcheemafc"',)]
        
        # making a single list for all usernames in a group.
        final_users.append(usernames1[i])
        final_users.append(usernames2)
        
        #### print("Final_users: ",final_users)
        #### final_users = ['@omarcheemapti', [('"@omercheemapti,@omarsarfarazpti,@omarsarfarzpti,@omercheemaptl,@omarcheemapti,@amuhammadk,@omarcheemafc"',)]]

        # Make a single list
        usernames_str = final_users[1][0][0]
        usernames_list = usernames_str.strip('"').split(',')
        usernames = [final_users[0]] + [username.strip('@') for username in usernames_list]
        new_final_users = usernames
        #### print("FINAL USERS",new_final_users)
        #### new_final_users = ['@omarcheemapti', 'omercheemapti', 'omarsarfarazpti', 'omarsarfarzpti', 'omercheemaptl', 'omarcheemapti', 'amuhammadk', 'omarcheemafc']

        # adding @ with username is not already
        for z in range(len(new_final_users)):

            


            if new_final_users[z][0] != '@':
                new_final_users[z] = '@' + new_final_users[z]   
        #### print("new_final_users: ",new_final_users)
        #### new_final_users = ['@omarcheemapti', '@omercheemapti', '@omarsarfarazpti', '@omarsarfarzpti', '@omercheemaptl', '@omarcheemapti', '@amuhammadk', '@omarcheemafc']
            
        
        


    
        # create a list of lists with the first list containing the column names
        list_of_columns = ['Username','Fullname','Location','Description','Followers','Following','Join_Date','Verification_status','Lists','Likes','Birthday','Profession','Tweets','Website','Bot_Score','Echo_Chamber','Fake_Followers','Financial','Self_Declared','Spammer','Most_Recent_Post','Likes_Count','Recent_tweets_per_week','Retweet_Ratio','Tweets_by_day_of_week','Sun','Mon','Tues','Wed','Thurs','Fri','Sat','Tweets_by_hour_of_day','12AM','1AM','2AM','3AM','4AM','5AM','6AM','7AM','8AM','9AM','10AM','11AM','12PM','1PM','2PM','3PM','4PM','5PM','6PM','7PM','8PM','9PM','10PM','11PM']
        #my_df = pd.DataFrame(columns=['Username','Fullname','Location','Description','Followers','Following','Join_Date','Verificaion_status','Lists','Likes','Birthday','Profession','Tweets','Website','Bot_Score','Echo_Chamber','Fake_Followers','Financial','Self_Declared','Spammer','Most_Recent_Post','Likes_Count','Recent_tweets_per_week','Retweet_Ratio','Tweets_by_day_of_week','Sun','Mon','Tues','Wed','Thurs','Fri','Sat','Tweets_by_hour_of_day','12AM','1AM','2AM','3AM','4AM','5AM','6AM','7AM','8AM','9AM','10AM','11AM','12PM','1PM','2PM','3PM','4PM','5PM','6PM','7PM','8PM','9PM','10PM','11PM'])
        
    
        # create an empty DataFrame with the correct number of columns
        my_df = pd.DataFrame(columns=list_of_columns)
        #### print("starting df for each group: ",my_df)
        #### my_df:   Empty DataFrame
        #### Columns: [Username, Fullname, Location, Description, Followers, Following, Join_Date, Verificaion_status, Lists, Likes, Birthday, Profession, Tweets, Website, Bot_Score, Echo_Chamber, Fake_Followers, Financial, Self_Declared, Spammer, Most_Recent_Post, Likes_Count, Recent_tweets_per_week, Retweet_Ratio, Tweets_by_day_of_week, Sun, Mon, Tues, 
        #### Wed, Thurs, Fri, Sat, Tweets_by_hour_of_day, 12AM, 1AM, 2AM, 3AM, 4AM, 5AM, 6AM, 7AM, 8AM, 9AM, 10AM, 11AM, 12PM, 1PM, 2PM, 3PM, 4PM, 5PM, 6PM, 7PM, 8PM, 9PM, 10PM, 11PM] 

        # LOOP for each element in list of groups username
        final_final_json = []
        
        for j in range(len(new_final_users)):
            #### len(new_final_user) = 8
            
            # getting data of each @username of the group
            check_in_sql = new_final_users[j]   
            print('Check in sql ',check_in_sql)

            #check if new_final_users exist in the list or not
            cursor = cnxn.cursor()
            select_query = "SELECT * FROM usersprofile_temp WHERE Username = %s"
            cursor.execute(select_query, (check_in_sql,))

            # Check if any rows are returned from the query
            if cursor.fetchone():
                print("User exists!")
                check = True
            else:
                print("User doesn't exist, skipping loop...")
                check = False

            if check == False:
                print("User not found")
                continue




            query2 = f"SELECT * FROM usersprofile_temp WHERE Username = '{check_in_sql}'"
            cursor2 = cnxn.cursor()
            cursor2.execute(query2)
            data= list(cursor2.fetchall())        
            print('DATA ',data)
            print("DATA[0]",data[0])
            print('LEN DATA ',len(data[0]))

            # removing Prediction null value 
            if len(data[0]) != 57:
                data[0] = data[0][:-1]   
            #print("DATA: ",data)        

            # appending each username data in dataframe
            for row in data:
                my_df.loc[len(my_df)] = row
            #print('dataframe after groups data: ',my_df)

            
            #CHECK FOR THE REAL ACCOUNT @username
            query3 = 'SELECT ID_twitter FROM feed_back_groups1_info'
            cursor3 = cnxn.cursor()
            cursor3.execute(query3)
            True_twitter = False
            real_username= list(cursor3.fetchall()) 
        
       
        #final_json=[]
        # if found a real account then raise flag TRUE for real,     
        for k in range(len(real_username)):
            
            
            good_real_username= real_username[k][0].lower()
            
            good_real_username = '@'+ good_real_username
            #print("goog_real_username: ",good_real_username)
            #print("username idn my df ",my_df['Username'].values)
            dd = my_df['Username'].values
            for jj in range(len(dd)):
            # print("dd",dd)
                #print('dd[jj]',dd[jj])
                if good_real_username == dd[jj]:
                    #print("goog_real_username: ",good_real_username)
                    True_twitter = True
                    True_username = good_real_username
                    k = len(real_username)
            
            #print('flag',True_twitter)
                    
        ########################## CODE FOR FOUND REAL AND FAKE ONLY GIVE PERCENTAGE ################################
            
        if True_twitter == True:
            real = True_username      

            # separate datafranme for fake and real users
            real_df = my_df[my_df['Username'].str.contains(True_username)]
            
            real_df = real_df.drop_duplicates()


            my_df = my_df[my_df['Username'] != True_username]
            fake_df = my_df.drop_duplicates()


            # check fan or parody in fake_df
            print("FAKE DF", fake_df)
            cnxn.commit()
            current_session_list = Rater(real,real_df,fake_df)
            final_json.append(current_session_list)

                
        ###################################################### CODE FOR NOT REAL BUT VERIFIED ############################################
        else:
            print('NO REAL account found Now Checking for Verified accounts')
            #print("MY DF: ",my_df)
            
            flag_verified_account_found =False
            
            #look for verified account
            #print("BFWEUFBWUIB",my_df['Username'][0])
            for s in range(len(my_df)):
                query22 = f"SELECT Verification_status FROM usersprofile_temp WHERE Username = '{my_df['Username'][s]}'"
                cursor22 = cnxn.cursor()
                cursor22.execute(query22)
                data= cursor22.fetchall()
                data = data[0][0]
                #print('data:',data)
                if data == 1:
                    real = my_df['Username'][s]
                    #print(real)
                    flag_verified_account_found =True
                    
            if flag_verified_account_found == True:
                True_username = real     
    # separate datafranme for fake and real users
                real_df = my_df[my_df['Username'].str.contains(True_username)]
                
                real_df = real_df.drop_duplicates()


                my_df = my_df[my_df['Username'] != True_username]
                fake_df = my_df.drop_duplicates()


                # check fan or parody in fake_df
                #print("FAKE DF", fake_df)
                cnxn.commit()

                #adding the real account in json

                




                current_session_list = Rater(True_username,real_df,fake_df)
                final_json.append(current_session_list)
                    
                    
            ######################################################## CODE FOR NOT REAL NO VERIFIED NOW LIKEHOOD ##############################
            
            else:
                print("PURE ML MODEL needed")

    print("MY FINAL DICTIONARY BEFORE THE JSON ",final_json)
    Jsonmaker(final_json)
    print('Results added in Json : dataofprediction.json')




    
### RUN THE CODE ###
    
    
#Percentage_giver()
        
        