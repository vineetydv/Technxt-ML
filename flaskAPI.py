from flask import Flask
import os
import getErrCatg as errClassFile

app = Flask(__name__)

cf_port = os.getenv("PORT")

count = 0


@app.route('/get/<errText>', methods=['GET'])
def getErrorCatg(errText):
    global count

    if count == 0:
        errClassFile.trainModel()

    errClass = errClassFile.getErrorCatg(errText)
    count = count + 1
    print(count)
    return errClass


if __name__ == '__main__':
    # app.run()
    if cf_port is None:
        app.run(host='0.0.0.0', port=5000, debug=True)
    else:
        app.run(host='0.0.0.0', port=int(cf_port), debug=True)
