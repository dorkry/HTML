import requests, csv

response = requests.get("http://api.nbp.pl/api/exchangerates/tables/C?format=json")
data = response.json()
heading = ["currency", "code", "bid", "ask"]
with open("C:\\Users\\Administrator\\Desktop\\Kodilla\\HTML\\kalkulator walut\\table.csv", "w") as file:
    w = csv.DictWriter(file, fieldnames = heading)
    w.writeheader()
    for i in data[0]["rates"]:
        w.writerow(i)
# files = open("C:\\Users\\Administrator\\Desktop\\Kodilla\\HTML\\kalkulator walut\\table.csv", "w")
#files.write(csv)
#files.close()
code_list = [i["code"] for i in data[0]["rates"]]
print(code_list)