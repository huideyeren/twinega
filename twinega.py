# -*- coding: utf-8 -*-

import settings
import tweepy
from mlask import MLAsk

TWITTER_CONSUMER_KEY = settings.twi_con_key
TWITTER_CONSUMER_SECRET = settings.twi_con_seq
TWITTER_ACCESS_TOKEN = settings.twi_acc_tkn
TWITTER_ACCESS_SECRET = settings.twi_acc_seq

class twitter():
    def __init__(self):
        print("初期化しています。")

    def login_for_twitter(self):
        """Login to Twitter"""
        auth = tweepy.OAuthHandler(TWITTER_CONSUMER_KEY,
                                   TWITTER_CONSUMER_SECRET)
        auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_SECRET)
        twitter = tweepy.API(auth)
        return twitter


twitter = twitter().login_for_twitter()
emotion_analyzer = MLAsk()

tweets = twitter.user_timeline()

for tweet in tweets:
    print(emotion_analyzer.analyze(tweet.text))
