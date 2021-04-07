from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main():
    return render_template("index.html")

@app.route('/kontakt')
def kontakt():
    return render_template("kontakt.html")