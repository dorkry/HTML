from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def main():
    return render_template("me.html")

@app.route('/kontakt', methods=['GET'])
def kontakt():
    return render_template("kontakt.html")

@app.route('/kontakt', methods=['POST'])
def form():
    print(request.form)
    return redirect("/kontakt")