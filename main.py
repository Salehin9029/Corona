import os
import tweepy as tw
import pandas as pd

consumer_key= '#PUTYOUROWNKEYS'
consumer_secret= '#PUTYOUROWNKEYS'
access_token= '#PUTYOUROWNKEYS'
access_token_secret= '#PUTYOUROWNKEYS'

auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)

#api.update_status("Look, I just started testing my twitter developer keys")

# Define the search term and the date_since date as variables
search_words = "corona"
date_since = "2018-11-16"

tweets = tw.Cursor(api.search,
              q=search_words,
              lang="en",
              since=date_since).items(2000)
              
tweets

users_locs = [[tweet.user.screen_name, tweet.user.location] for tweet in tweets]
tweet_text = pd.DataFrame(data=users_locs, 
                    columns=['user', "location"])
tweet_text

tweet_text.to_excel(r'corona.xlsx', index=False, header=True)
#print(users_locs)
#print(tweet_text)
for tweet in tweets:
    tweets = tweet.text.encode('UTF-8')

    print(tweets)
    print(users_locs)
