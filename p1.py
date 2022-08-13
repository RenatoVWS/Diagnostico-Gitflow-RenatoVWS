import json
from operator import itemgetter

data_store = []
#Read JSON data into the datastore variable
with open('farmers-protest-tweets-2021-03-5.json', 'r') as f:
    for line in f:
        json_data = json.loads(line)
        data_store.append(json_data)

# Los 10 tweets más retweeted
newlist = sorted(data_store, key=itemgetter('retweetCount'), reverse=True)
print("Top 10 de los Tweets con más retweets:")
for i in range(10):
    tweet = newlist[i]
    print(f"{i + 1}. Tweet id: {tweet['id']} | Reteewts: {tweet['retweetCount']}")