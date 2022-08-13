import json

# Los Top 10 días con más tweets
def top_dias(data_store):
    dias = {}
    for tweet in data_store:
        date_string = tweet["date"]
        date = date_string.split("T")[0]
        if date not in dias:
            dias[date] = 0
        else:
            dias[date] += 1

    newlist = sorted(dias.items(), key=lambda x:x[1], reverse=True)
    print("Top 10 días con más tweets")
    for i in range(10):
        dia = newlist[i]
        print(f"{i + 1}. Día: {dia[0]} | Tweets: {dia[1]}")
