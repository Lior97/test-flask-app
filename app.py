from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return '<h1>Hello from DevPush Test App!</h1><p>Deployed via git push. Timestamp: ' + str(datetime.now()) + '</p>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
