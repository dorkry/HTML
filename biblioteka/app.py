import csv
from flask import Flask, render_template, request, redirect

heading = ["author", "title", "format", "descr"]

def save(data):
    with open("C:\\Users\\Administrator\\Desktop\\Kodilla\\HTML\\biblioteka\\base.csv", "w") as file:
        w = csv.DictWriter(file, fieldnames = heading)
        w.writeheader()
        for i in data:
            w.writerow(i) 

def read():
    base_list = []
    try: 
        with open("C:\\Users\\Administrator\\Desktop\\Kodilla\\HTML\\biblioteka\\base.csv", "r") as file:
            base = csv.DictReader(file)
            for row in base:
                base_list.append(row)
    except IOError:
        with open("C:\\Users\\Administrator\\Desktop\\Kodilla\\HTML\\biblioteka\\base.csv", "w") as file:
            w = csv.DictWriter(file, fieldnames = heading)
            w.writeheader()
    return base_list

app = Flask(__name__)

base = read()

@app.route('/')
def main():   
    return render_template("index.html")

@app.route('/add', methods=['GET'])
def add():
    return render_template("add.html")

@app.route('/add', methods = ['POST'])
def add_post():
    author = request.form.get("author")
    title = request.form.get("title")
    form = request.form.get("format")
    descr = request.form.get("descr")
    temp = {
        "author": author,
        "title": title,
        "format": form,
        "descr": descr
    }
    base.append(temp)
    save(base)
    return redirect("/")
 
@app.route('/find', methods=['GET'])
def find():
    return render_template("find.html")
    
@app.route('/find', methods=['POST'])
def find_out():
    new_list = []
    option = request.form.get("option")
    value = request.form.get("value")
    for i in base:
        if i[option] == value:
            new_list.append(i)
    print(new_list)
    return render_template("find.html", result = new_list)

@app.route('/delete', methods=['GET'])
def delete():
    return render_template("delete.html")

@app.route('/delete', methods=['POST'])
def delete_out():
    out = False
    author = request.form.get("author")
    title = request.form.get("title")
    for i in base:
        if i["author"] == author and i["title"] == title:
            base.remove(i)
            out = True
    save(base)
    if out:
        message = "Plik usunięto"
    else:
        message = "Nie znalezono pasujących elementów"
    return render_template("delete.html", msg = message)

    
@app.route('/all', methods=['GET'])
def show_all():
    return render_template("all.html", result = base)