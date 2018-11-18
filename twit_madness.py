import tweepy
import re
import csv
from tweepy import OAuthHandler
from datetime import datetime

# example: g_hash  = #bitcoin
def download_tweets(file_name,lag,q_hash):
    
    now = datetime.now()
    # need to fill this things below
    consumer_key = ''
    consumer_secret = ''
    access_token = ''
    access_secret = ''

    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    api = tweepy.API(auth,wait_on_rate_limit=True)

    with open(file_name, 'a') as csvFile:
        #Use csv Writer
        csvWriter = csv.writer(csvFile)

        for tweet in tweepy.Cursor(api.search,
                           q=q_hash,
                           count=100000,
                           lang="en",
                           since=str(now.date())).items():
   
            csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
            if (abs(tweet.created_at.hour - now.hour) > lag) and (abs(tweet.created_at.hour - now.hour) < 23) :
            break
            
    return file_name