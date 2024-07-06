import snscrape.modules.twitter as sntwitter



name='elonmusk'#,'imrankhanworld']
Tweet_Limit=10
tweets_list2=[]
for i,tweet in enumerate(sntwitter.TwitterSearchScraper(f'from:{name}').get_items()):
    if i>Tweet_Limit:          
        break          
    tweets_list1=([tweet.date, tweet.id, tweet.content, tweet.user.username])
    tweets_list2.append(tweet.content)
print(tweets_list2)
                
