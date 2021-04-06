from flask import Flask

app = Flask(__name__)

@app.route('/')

def main():
    html = open("index.html", "r")
    return html.read()