#!/usr/bin/python3
import nltk
from nltk.corpus import twitter_samples

nltk.download("twitter_samples")

allPositiveTweets = twitter_samples.strings("positive_tweets.json")
allNegativeTweets = twitter_samples.strings("negative_tweets.json")

print("Number of Positive Tweets", len(allPositiveTweets))
print("Number of Negative Tweets", len(allNegativeTweets))

print('\nThe type of all_positive_tweets is: ', type(allPositiveTweets))
print('The type of a tweet entry is: ', type(allNegativeTweets[0]))
