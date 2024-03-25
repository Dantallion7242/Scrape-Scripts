import pandas as pd 
import requests
import urllib3
import csv
from datetime import datetime
twitter_data = []
current_datetime = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

payload = { 
    'api_key' : '' , 
    'query' : 'casino',
    'num' : '10000'
}
response = requests.get(
    'https://api.scraperapi.com/structured/twitter/search' , params=payload)
data = response.json()
print(data)
data.keys()
data['organic_results'][0]['snippet']
all_tweets = data['organic_results']
for tweet in all_tweets:
    twitter_data.append(tweet)
    df = pd.DataFrame(twitter_data)
df.to_json('tweet.json',orient='index')

csv_filename = f'tweet_{current_datetime}.csv'
df.to_csv(csv_filename, index=False)  # Set index=False to exclude row numbers from the CSV
print("file exported")
df
