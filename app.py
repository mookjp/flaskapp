from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>Hello World!</h1> \
            <p>This is a sample wep application!</p>\
            <strong>This is `development` version.</strong>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

