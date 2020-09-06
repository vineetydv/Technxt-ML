from flask import Flask, request
import os
import processRecog as pr

app = Flask(__name__)

cf_port = os.getenv("PORT")

count = 0


@app.route('/getProcess', methods=['GET'])
def getProcess():
    global count

    if count == 0:
        pr.trainModel()

    fileObject = request.files['file']
    processName = pr.getProcessName(fileObject)
    count = count + 1
    print(count)
    return processName


if __name__ == '__main__':
    # app.run()
    if cf_port is None:
        app.run(host='0.0.0.0', port=5000, debug=True)
    else:
        app.run(host='0.0.0.0', port=int(cf_port), debug=True)
