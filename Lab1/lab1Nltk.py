#!/usr/bin/python3
import nltk
from nltk.corpus import twitter_samples
import matplotlib.pyplot as plt
import random
import re  # library for regular expression operations
import string  # for string operations
from nltk.corpus import stopwords  # module for stop words that come with NLTK
from nltk.stem import PorterStemmer  # module for stemming
from nltk.tokenize import TweetTokenizer  # module for tokenizing strings

nltk.download("twitter_samples")

allPositiveTweets = twitter_samples.strings("positive_tweets.json")
allNegativeTweets = twitter_samples.strings("negative_tweets.json")

print("Number of Positive Tweets", len(allPositiveTweets))
print("Number of Negative Tweets", len(allNegativeTweets))

print('\nThe type of all_positive_tweets is: ', type(allPositiveTweets))
print('The type of a tweet entry is: ', type(allNegativeTweets[0]))

# plot graph of data
# fig = plt.figure(figsize=(5, 5))
# lables = 'Positive', 'Negative'
# sizes = [len(allPositiveTweets), len(allNegativeTweets)]
# plt.pie(sizes, labels=lables, autopct='%1.1f%%', shadow=True, startangle=90)
# plt.axis('equal')
# plt.show()

# print positive in green
print('\033[92m' + allPositiveTweets[random.randint(0, 5000)])
# print negative in red
print('\033[91m' + allNegativeTweets[random.randint(0, 5000)])
tweet = allPositiveTweets[2277]
print(tweet)

# download the stopwords from NLTK
nltk.download('stopwords')
print('\033[92m' + tweet)
print('\033[94m')
# remove hyperlinks
tweet2 = re.sub(r'https?:\/\/.*[\r\n]*', '', tweet)
# remove hashtags
# only removing the hash # sign from the word
tweet2 = re.sub(r'#', '', tweet2)
print(tweet2)

print()
print('\033[92m' + tweet2)
print('\033[94m')
# instantiate tokenizer class
tokenizer = TweetTokenizer(preserve_case=False)
# tokenize tweets
tweet_tokens = tokenizer.tokenize(tweet2)
print()
print('Tokenized string:')
print(tweet_tokens)

# Import the english stop words list from NLTK
stopwords_english = stopwords.words('english')
print('Stop words\n')
print(stopwords_english)
print('\nPunctuation\n')
print(string.punctuation)

print()
print('\033[92m')
print(tweet_tokens)
print('\033[94m')
tweets_clean = []
for word in tweet_tokens:  # Go through every word in your tokens list
    if (word not in stopwords_english and  # remove stopwords
            word not in string.punctuation):  # remove punctuation
        tweets_clean.append(word)
print('removed stop words and punctuation:')
print(tweets_clean)

print()
print('\033[92m')
print(tweets_clean)
print('\033[94m')
# Instantiate stemming class
stemmer = PorterStemmer()
# Create an empty list to store the stems
tweets_stem = []
for word in tweets_clean:
    stem_word = stemmer.stem(word)  # stemming word
    tweets_stem.append(stem_word)  # append to the list
print('stemmed words:')
print(tweets_stem)
