import tweepy

access_token = ""
access_token_secret = ""
api_key = ""
api_key_secret = ""

auth = tweepy.OAuthHandler(consumer_key=api_key, consumer_secret=api_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# Define the WOEID for the desired location
chosen_woeid = 1  # Worldwide

try:
    # Get trending topics for the chosen location
    trends_result = api.trends_place(chosen_woeid)
    trends = trends_result[0]["trends"]

    if trends:
        print("\nTop trending topics:")
        for trend in trends:
            print(trend["name"])
            if "tweet_volume" in trend:
                print(f"Tweet volume: {trend['tweet_volume']}")
            else:
                print("Tweet volume not available")
    else:
        print("No trends available for the chosen location.")
except Exception as e:
    print("An error occurred:", e)
