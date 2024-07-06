

# A simple and unlimited Twitter scraper with python.
Requirements : 

`pip install -r requirements.txt`

Note : You must have Chrome installed on your system. 
Then you have to give path of chromedriver in file Example.py and save1.py 
## Results :

### Tweets :
We can get tweets of specified keywords. and in a limited time duration
tweets are being saved for each user in Tweets folder
### Following / Followers :

Too much.. like Imran_Khan having followers in Millions its not possible to collect their names.

## Usage :
run final.py
### Library :

I will shorlty introduce its library



After the installation, you can import and use the functions as follows:
 
no. of following","no. of followers", "join date", "date of birth", "location", "website", "description"]**

```
users_info = get_user_information(users, headless=True)
```

**Get followers and following of a given list of users**
**Enter your username and password in .env file. I recommend you do not use your main account.**  
**Increase wait argument to avoid banning your account and maximize the crawling process if the internet is slow. I used 1 and it's safe.**  

**Set your .env file with `SCWEET_EMAIL` , `SCWEET_USERNAME`  and `SCWEET_PASSWORD` variables and provide its path**  

```
env_path = ".env"

following = get_users_following(users=users, env=env_path, verbose=0, headless=True, wait=2, limit=50, file_path=None)

followers = get_users_followers(users=users, env=env_path, verbose=0, headless=True, wait=2, limit=50, file_path=None)
```

### Terminal :

```
Scrape tweets.

optional arguments:
  -h, --help            show this help message and exit
  --words WORDS         Words to search for. they should be separated by "//" : Cat//Dog.
  --from_account FROM_ACCOUNT
                        Tweets posted by "from_account" account.
  --to_account TO_ACCOUNT
                        Tweets posted in response to "to_account" account.
  --mention_account MENTION_ACCOUNT
                        Tweets that mention "mention_account" account.         
  --hashtag HASHTAG
                        Tweets containing #hashtag
  --until UNTIL         End date for search query. example : %Y-%m-%d.
  --since SINCE
                        Start date for search query. example : %Y-%m-%d.
  --interval INTERVAL   Interval days between each start date and end date for
                        search queries. example : 5.
  --lang LANG           Tweets language. Example : "en" for english and "fr"
                        for french.
  --headless HEADLESS   Headless webdrives or not. True or False
  --limit LIMIT         Limit tweets to be scraped.
  --display_type DISPLAY_TYPE
                        Display type of Twitter page : Latest or Top tweets
  --resume RESUME       Resume the last scraping. specify the csv file path.
  --proxy PROXY         Proxy server
  --proximity PROXIMITY Proximity
  --geocode GEOCODE     Geographical location coordinates to center the
                        search (), radius. No compatible with proximity
  --minreplies MINREPLIES
                        Min. number of replies to the tweet
  --minlikes MINLIKES   Min. number of likes to the tweet
  --minretweets MINRETWEETS
                        Min. number of retweets to the tweet
```

