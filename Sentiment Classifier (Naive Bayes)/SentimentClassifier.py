from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
import sklearn.datasets as skd
from pathlib import Path
import tweepy
import datetime

consumer_key = "F9rQX2nhkKcr7wOzYWncbLz3Y"
consumer_secret = "QQPPsZfssDLSXgm6w4y8I5JbgMonN1fjPdn1LMC6hMK1h0u94q"
access_key = "881673991-QOIo66W7sMhcgNzZRHBZ3X3CIQDDKk2Ci9Qt8Igu"
access_secret = "NQVOvRSycLK252HXvjPpetpRXTwJO4NY5vwu1wq62vtF4"
tag = ''


def trainModel():
    trainModel.categories = ['negative',
                             'positive']
    dataFolder = Path("files/train/")
    trainModel.news_train = skd.load_files(dataFolder,
                                           categories=trainModel.categories, encoding='ISO-8859-1')

    trainModel.text_clf = Pipeline(
        [('vect', TfidfVectorizer()), ('clf', MultinomialNB())])
    # train the model
    trainModel.text_clf.fit(trainModel.news_train.data,
                            trainModel.news_train.target)


def getSentiment():

    documents = []
    global tag
    hashtag = tag + " -filter:retweets"
    tweets = get_tweets(hashtag)
    for tweet in tweets:
        documents.append(tweet.text)

    tweetData = []
    # print(docs_test)
    for doc in documents:
        predicted = trainModel.text_clf.predict([doc])
        tweetData.append([doc, trainModel.categories[predicted[0]]])
        # print(predicted)
        # print(trainModel.categories[predicted[0]])
    print(tweetData)
    tweetDF = {
        "data": tweetData
    }
    if tweetDF:
        return tweetDF
    else:
        return "No tweets found!"
    # return trainModel.categories[predicted[0]]


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


def mainApp(para_tag):
    global tag
    tag = para_tag
    # trainModel()
    tweetDF = getSentiment()
    # print(tweetDF)
    return tweetDF


# mainApp("Air India")
