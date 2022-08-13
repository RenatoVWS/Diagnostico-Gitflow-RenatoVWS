import json
from operator import itemgetter

data_store = []
#Read JSON data into the datastore variable
with open('farmers-protest-tweets-2021-03-5.json', 'r') as f:
    for line in f:
        json_data = json.loads(line)
        data_store.append(json_data)

# Los Top 10 usuarios con más tweets
newlist = sorted(data_store, key=lambda d: d.get('user', {}).get('mediaCount'), reverse=True)
print("Top 10 usuarios con más tweets")
users = set()
i=0
j=1
while len(users) < 10:
    tweet = newlist[i]
    if tweet['user']['username'] not in users:
        print(f"{j}. Username: {tweet['user']['username']} | Teewts: {tweet['user']['mediaCount']}")
        j+=1
    users.add(tweet['user']['username'])
    i+=1