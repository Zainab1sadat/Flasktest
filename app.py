from flask import Flask

app = Flask(__name__)

@app.route('/')

def test():
    return 'Hello flask, I am new Here :)'

if __name__ == '__main__':
    app.run(debug=True)
