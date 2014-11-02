from flask import Flask
import time
app = Flask(__name__)
time.sleep(5)

@app.route('/')
def hello_world():
    return '<h1>Hello World!</h1> \
            <p>This is a sample wep application!</p>\
            <strong>Can you see some versions of this application?</strong>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

