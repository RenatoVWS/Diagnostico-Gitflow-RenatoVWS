import json
import re

# Los Top 10 hashtags mas usados
def top_hashtags(data_store):
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
        print(f"{i + 1}. Hashtag: #{hashtag[0]} | Tweets: {hashtag[1]}")
