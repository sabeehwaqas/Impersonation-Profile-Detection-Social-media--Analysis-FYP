from strsimpy.cosine import Cosine
from datetime import datetime
import pandas as pd
from fuzzywuzzy import fuzz
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
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

import pandas as pd
from strsimpy.jaro_winkler import JaroWinkler
def Tweet_Analysis(real,fake):
    real_tweets = pd.read_csv(f'tweets/{real}.csv')
    print(real)
    jarowinkler = JaroWinkler()
    fake =['@loveyouispr',"@asimbajwaispr_","@_dgispr","@professorali13","@ispr_pakistan_","@isprtv","@ispr__","@isprjoker","@officiadgispr","@ispr_isi","@isprunofficial3","@weather4746646","@asimbharwaispr","@dgispr14","@dg_cia","@ispr_unofficial"]
    username = real_tweets['Username']
    realtext = real_tweets['Text']
    date_time1=real_tweets['Datetime']
    date11=[]
    for i, date1 in enumerate(date_time1):
        if len(date_time1[i])>10:    
            date111=dateissue(date1,date11)
            date11.append(date111)
        else:
            date11.append(date_time1[i])
    real_tweets['Datetime'] = date11
    #real_tweets.to_csv(f'Tweets/{real}.csv', index=False)
    
    date_time1=0
    ## Algorithm for sorting out the date time issue in tweets
    for i, user in enumerate(fake):        
        date_time2=0
        date22=[]
        fake=user
        print(fake)
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
                    if a1 == b1:
                        #fake_users = fake_users.loc[fake_users['Datetime'] == a1]
                        print(jarowinkler.similarity(realtext[i], faketext[j]),"---JARO USTAAD---- :D :( ")
                        print(realtext[i],"-----",faketext[j])
                        jarowinkler.similarity(realtext[i], faketext[j])
                        
              #  print(fake_users['Datetime'][2])
                
                #print(filtered_df['Datetime'][2])
            #fake_users.to_csv(f'Tweets/{fake}.csv', index=False)
            
        except Exception as e:
            print("Error : ",e)
    

def dateissue(datex):
    date_time_str = datex
    datex= date_time_str[:-15]
    date_format = '%Y-%m-%d'
    datex = datetime.strptime(datex, date_format).date()
    #datexx.append(datex)
    #print("I am working")
    print(datex)
    return datex
def similarity1(string1,string2):
    #Levenshtein.distance("measuring with Levenshtein", 
     #                    "measuring differently")
    print(fuzz.ratio(string1, string2))
#Tweet_Analysis("@OfficialDGISPR",'fakes')
similarity1("hello world","not hello world")
analyzer = SentimentIntensityAnalyzer()

def sentiment_scores():
	Real_Tweets = pd.read_csv("Tweets/@_dgispr.csv")
#	Fake_Tweets = pd.read_csv("Tweets/ID")
	saved_column = Real_Tweets['Username']
	text = Real_Tweets['Text']
	print(text[1:len(text)])
	# Create a SentimentIntensityAnalyzer object.
	sid_obj = SentimentIntensityAnalyzer()
	sentiment_dict = sid_obj.polarity_scores(text)	
	print("Overall sentiment dictionary is : ", sentiment_dict)
	print("sentence was rated as ", sentiment_dict['neg']*100, "% Negative")
	print("sentence was rated as ", sentiment_dict['neu']*100, "% Neutral")
	print("sentence was rated as ", sentiment_dict['pos']*100, "% Positive")
	print("Sentence Overall Rated As", end = " ")
	if sentiment_dict['compound'] >= 0.05 :
		print("Positive")
	elif sentiment_dict['compound'] <= - 0.05 :
		print("Negative")
	else :
		print("Neutral")
if __name__ == "__main__" :
	sentiment_scores()
