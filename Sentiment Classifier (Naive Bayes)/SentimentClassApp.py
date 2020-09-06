from flask import Flask
import os
import SentimentClassifier as sc

app = Flask(__name__)

cf_port = os.getenv("PORT")
count = 0


@app.route('/get/<hashtag>', methods=['GET'])
def getTweetSentiment(hashtag):
    global count
    if count == 0:
        sc.trainModel()
    count = count + 1
    tweetData = sc.mainApp(hashtag)
    print(hashtag)
    return tweetData


if __name__ == '__main__':
    # app.run()
    if cf_port is None:
        app.run(host='0.0.0.0', port=5000, debug=True)
    else:
        app.run(host='0.0.0.0', port=int(cf_port), debug=True)
