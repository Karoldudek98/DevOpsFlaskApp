from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>DevOps Flask App</title>
        </head>
        <body>
            <h1>Karol Dudek's Flask app</h1>
        </body>
        </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)
