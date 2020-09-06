from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
# import pandas
import tweepy
import datetime

# Fill the X's with the credentials obtained by
# following the above mentioned procedure.
consumer_key = "F9rQX2nhkKcr7wOzYWncbLz3Y"
consumer_secret = "QQPPsZfssDLSXgm6w4y8I5JbgMonN1fjPdn1LMC6hMK1h0u94q"
access_key = "881673991-QOIo66W7sMhcgNzZRHBZ3X3CIQDDKk2Ci9Qt8Igu"
access_secret = "NQVOvRSycLK252HXvjPpetpRXTwJO4NY5vwu1wq62vtF4"

tag = ''

# Function to extract tweets


def get_tweets(hashtag):

    # Authorization to consumer key and consumer secret
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

    # Access to user's access key and access secret
    auth.set_access_token(access_key, access_secret)

    # Calling api
    api = tweepy.API(auth, wait_on_rate_limit=True)

    date_since = datetime.date.today() - datetime.timedelta(days=7)
    tweets = tweepy.Cursor(
        api.search,
        result_type='Popular',
        q=hashtag,
        lang="en",
        since=date_since).items(5)
    return tweets


def authenticate_client():
    ta_credential = AzureKeyCredential('c54e01481751449b91a5c923a16ba086')
    text_analytics_client = TextAnalyticsClient(
        endpoint='https://vineet.cognitiveservices.azure.com/', credential=ta_credential)
    return text_analytics_client


def sentiment_analysis_example(client):
    documents = []
    global tag
    hashtag = tag + " -filter:retweets"
    tweets = get_tweets(hashtag)
    for tweet in tweets:
        documents.append(tweet.text)

    if documents:
        response = client.analyze_sentiment(documents=documents)

        tweetData = []
        for res in response:
            tweetData.append([res.sentences[0].text, res.sentiment])

        # tweetDF = pandas.DataFrame(
        #     tweetData, columns=['Tweet', 'Sentiment'])
        # pandas.set_option('display.max_colwidth', None)

        # print(" Here are some tweets about the hashtag "+hashtag)
        # print(tweetDF)

        tweetDF = {
            "data": tweetData
        }
        return tweetDF
    else:
        return "No tweets found!"


def mainApp(para_tag):
    global tag
    tag = para_tag
    client = authenticate_client()
    tweetDF = sentiment_analysis_example(client)
    return tweetDF
