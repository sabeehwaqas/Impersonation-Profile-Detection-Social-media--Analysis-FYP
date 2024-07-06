from strsimpy.cosine import Cosine
from datetime import datetime
#import snscrape
import snscrape.modules.twitter as sntwitter
import pandas as pd
from strsimpy.jaro_winkler import JaroWinkler
import mysql.connector
import snscrape
import json
from CopyingTable import Copy_Table
from CSV_converter import CSV_converter1
import snscrape.modules.twitter as sntwitter
from sqlalchemy import create_engine
import pandas as pd
import datetime
from Clustering import Des_Clustering
from sentiment import sentiment_scores
## This IS BETA Version. may include glitche
def tweet_analysis(Tweet_Limit=100):

        conn = mysql.connector.connect( 
            host="localhost", 
            user="root", 
            password="Jaguar@123", 
            database="sql_false_flag") 
        cursor = conn.cursor()
        #query="SELECT * from UsersProfile where Fullname LIKE '%DGISPR%' "
        query="SELECT * from UsersProfile_Temp "
        cursor.execute(query)
        rows=cursor.fetchall()
        #print(rows[5][0])
        Usernames1=[]
        Main_Dict={}
        tweets_list2=[]
        #print(rows)
        
        for row in rows:
            Usernames1.append(row[0]) 
            #print(Usernames1)
            tweets_list1 = []       
            try: 
                # Creating list to append tweet data to
                tweets_list1 = []
                name=row[0]#.replace('@','')
                print(name)
                for i,tweet in enumerate(sntwitter.TwitterSearchScraper(f'from:{name}').get_items()):
                    if i>Tweet_Limit:          
                        break          
                    tweets_list1=([tweet.date, tweet.id, tweet.content, tweet.user.username])
                    tweets_list2.append(tweet.content)
                
                    query="INSERT INTO UsersTweets_Temp (`Datetime`, `Tweet_Id`, `tweet_text`, `Username`) VALUES (%s,%s,%s,%s) "
                    dt_str =str(tweets_list1[0].date())
                    values=(dt_str,tweets_list1[1],str(tweets_list1[2]),str(tweets_list1[3]))
                    cursor.execute(query,values)
                conn.commit()
                #print(str(tweets_list1[2]))
                
                print("fetched tweets-------------------------")
            except Exception as e:
                        print("-----cannot fetch tweets---")
        Copy_Table("UsersTweets","UsersTweets_Temp")
        #Des_Clustering(tweets_list2,None,5)
        
        
        Tweet_Dict={}
        Final_Tweets=[]
        Sentiment_Scores=[]
        for row in rows:
            row1=row[0].replace('@','')

            query=f"SELECT `tweet_text` from UsersTweets_Temp where Username = '{row1}';"
            cursor.execute(query)
            Tweets1=cursor.fetchall()
            Tweets = [row[0] for row in Tweets1]
            #print(Tweets)
            Tweet_Dict={'Username':row[0],'Tweets':Tweets}
            Final_Tweets.append(Tweet_Dict)
            dict1=sentiment_scores(row[0],Tweets)
            Sentiment_Scores.append(dict1)
            #with open('Tweet_Analysis.json', 'r', encoding='utf-8') as reading:
            #    data=json.load(reading)
            #    data.append(dict1)
            #with open('Tweet_Analysis.json', 'w', encoding='utf-8') as reading1:                    
            #    json.dump(data,reading1)
        for Sentiment_Score in Sentiment_Scores:
            #print(Sentiment_Score)
            query="INSERT INTO Sentiments(Username,Positive,Negative,Neutral,Overall) VALUES(%s,%s,%s,%s,%s)"
            values=(Sentiment_Score['Username'],Sentiment_Score['Positive'],Sentiment_Score['Negative'],Sentiment_Score['Neutral'],Sentiment_Score['Overall'])
            cursor.execute(query,values)
            conn.commit()
        #CSV_converter1('Tweet_Analysis.json','Tweet_Analysis.csv')

        #print(Final_Tweets)
        allTweets=[]
        for twet in Final_Tweets:
            for aa in twet['Tweets']:
                allTweets.append(aa)
        
        #allTweets1= [word.replace("(", "").replace(",)", "") for word in allTweets]
        #print(allTweets1)
        #Fina_Dict=Des_Clustering(allTweets1,None,4)
        #print(Fina_Dict)

        '''
        tweets_similartiy=[]
        fake=user
        print(fake)
        avg=0
        average=0
        
        try:
            fake_users = pd.read_csv(f"Tweets/{fake}.csv")
            date_time2=fake_users['Datetime']
            faketext = fake_users['Text']
            for i, date2 in enumerate(date_time2):
                if len(date_time2[i]) > 10:    
                    date2 = dateissue(date2)
                    date22.append(date2)
                else:
                    date22.append(date2)
            fake_users['Datetime'] = date22
            for i, a1 in enumerate(date11):
                for j, b1 in enumerate(fake_users["Datetime"]):
                    #print('A1: ',a1,' ::B1: ',b1)
                    if a1 <= b1:
                        #print("--------Dates----",a1,"--",b1)
                        #fake_users = fake_users.loc[fake_users['Datetime'] == a1]
                        #print(jarowinkler.similarity(realtext[i], faketext[j]),"---JARO USTAAD---- :D :( ")
                        #print(realtext[i],"-----",faketext[j])
                        tweets_similarity1= jarowinkler.similarity(realtext[i], faketext[j])
                        avg += tweets_similarity1
                        aa=aa+1
                        tweets_similartiy.append(tweets_similarity1)
            average = avg/aa
            similarity_averages.update({f'{fake}': average})

            #print(average)
                
              #  print(fake_users['Datetime'][2])
                
                #print(filtered_df['Datetime'][2])
            #fake_users.to_csv(f'Tweets/{fake}.csv', index=False)
            
        except Exception as e:
            if type(e) == ZeroDivisionError:
                average=0
                similarity_averages.update({f'{fake}': average})
                
                #print("Error : ",e)
    #print (similarity_averages)
        return similarity_averages '''
#tweet_analysis()
def dateissue(datex):
    date_time_str = datex
    datex= date_time_str[:-15]
    date_format = '%Y-%m-%d'
    datex = datetime.strptime(datex, date_format).date()
    #datexx.append(datex)
    #print("I am working")
    print(datex)
    return datex
#fakes =['@loveyouispr',"@asimbajwaispr_","@_dgispr","@ispr_pakistan_","@ispr__","@isprjoker","@officiadgispr","@ispr_isi","@isprunofficial3","@weather4746646","@asimbharwaispr","@dgispr14","@dg_cia","@ispr_unofficial"]
#Tweet_Analysis("@OfficialDGISPR",fakes)

##IGNORE ME PLEASE////////////////
#cosine = Cosine(2)
#s0 = 'I am studying at NUST'
#s1 = 'I am studying in NUST ational University Of Sciences And Technology '
#p0 = cosine.get_profile(s0)
#p1 = cosine.get_profile(s1)
#print(cosine.similarity_profiles(p0, p1))
#from strsimpy.ngram import NGram
#twogram = NGram(2)
#print(twogram.distance('ABCD', 'ABTUIO
#s1 = 'I am studying at NUST'
#s2 = 'I am studying at National University Of Sciences And Technology'
#fourgram = NGram(4)
#print(fourgram.distance(s1, s2))
## IGNORE ME PLEASE///////////