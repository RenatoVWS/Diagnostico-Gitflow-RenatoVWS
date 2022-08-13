import json
import re

data_store = []
#Read JSON data into the datastore variable
with open('farmers-protest-tweets-2021-03-5.json', 'r') as f:
    for line in f:
        json_data = json.loads(line)
        data_store.append(json_data)

# Los Top 10 hashtags mas usados
hashtags = {}
for tweet in data_store:
    content_string = tweet["content"]
    cont_hashtags = re.findall(r"#(\w+)", content_string)
    for hashtag in cont_hashtags:
        if hashtag not in hashtags:
            hashtags[hashtag] = 0
        else:
            hashtags[hashtag] += 1

newlist = sorted(hashtags.items(), key=lambda x:x[1], reverse=True)
print("Top 10 hashtags más usados")
for i in range(10):
    hashtag = newlist[i]
    print(f"{i + 1}. Día: {hashtag[0]} | Tweets: {hashtag[1]}")
