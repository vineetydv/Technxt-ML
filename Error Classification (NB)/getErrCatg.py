import numpy as np
from sklearn.metrics import accuracy_score
from sklearn import metrics
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
import sklearn.datasets as skd
from pathlib import Path


def trainModel():
    trainModel.categories = ['Activate LOA', 'Stock management']
    dataFolder = Path("files/train/")
    trainModel.news_train = skd.load_files(dataFolder,
                                           categories=trainModel.categories, encoding='ISO-8859-1')

    trainModel.text_clf = Pipeline(
        [('vect', TfidfVectorizer()), ('clf', MultinomialNB())])
    # train the model
    trainModel.text_clf.fit(trainModel.news_train.data,
                            trainModel.news_train.target)


def getErrorCatg(errText):

    # Predict the test cases
    docs_test = [errText]
    predicted = trainModel.text_clf.predict(docs_test)
    print(predicted)
    print(trainModel.categories[predicted[0]])
    return trainModel.categories[predicted[0]]
