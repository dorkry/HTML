import requests, csv
from flask import Flask, render_template, request, redirect

response = requests.get("http://api.nbp.pl/api/exchangerates/tables/C?format=json")
data = response.json()

code_list = [i["code"] for i in data[0]["rates"]]

app = Flask(__name__)
@app.route('/', methods = ['GET'])
def main():
    res = -1
    return render_template("index.html", items = code_list, result = res)

@app.route('/', methods = ['POST'])
def form():
    currency = request.form.get("waluta")
    try:
        amount = float(request.form.get("wartosc"))
        if amount <= 0:
            res = -1
        else:    
            for i in data[0]["rates"]:
                if i["code"] == currency:
                    res = amount * i["bid"]
    except:
        res = -1
    return render_template("index.html", items = code_list, result = res)



