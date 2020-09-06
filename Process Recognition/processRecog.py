from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
import sklearn.datasets as skd
from pathlib import Path


def trainModel():
    trainModel.categories = ['Over the Counter Sales',
                             'Procure to Pay', 'Production Process', 'Sell from Stock']
    dataFolder = Path("files/train/")
    trainModel.news_train = skd.load_files(dataFolder,
                                           categories=trainModel.categories, encoding='ISO-8859-1')

    trainModel.text_clf = Pipeline(
        [('vect', TfidfVectorizer()), ('clf', MultinomialNB())])
    # train the model
    trainModel.text_clf.fit(trainModel.news_train.data,
                            trainModel.news_train.target)


def getProcessName(File_object):

    # Predict the test cases
    # filePath = Path("files/test/test.txt")
    # File_object = open(filePath, "r")
    docs_test = File_object.readlines()
    print(docs_test)
    predicted = trainModel.text_clf.predict(docs_test)
    print(predicted)
    print(trainModel.categories[predicted[0]])
    return trainModel.categories[predicted[0]]


# trainModel()
# getProcessName()
