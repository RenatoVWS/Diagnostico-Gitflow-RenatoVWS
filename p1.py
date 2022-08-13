import json
from operator import itemgetter

# Los 10 tweets más retweeted
def top_tweets(data_store):
    newlist = sorted(data_store, key=itemgetter('retweetCount'), reverse=True)
    print("Top 10 de los Tweets con más retweets:")
    for i in range(10):
        tweet = newlist[i]
        print(f"{i + 1}. Tweet id: {tweet['id']} | Reteewts: {tweet['retweetCount']}")