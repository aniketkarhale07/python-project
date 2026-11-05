from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Flask Application</title>
    </head>
    <body>
        <h1>Welcome to Flask Application</h1>
        <h2>Version 2.0.0</h2>
        <p>Application deployed successfully using Jenkins!</p>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7000)
