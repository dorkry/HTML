import requests, csv

def get_nbp():
    response = requests.get("http://api.nbp.pl/api/exchangerates/tables/C?format=json")
    data = response.json()
    heading = ["currency", "code", "bid", "ask"]
    with open("table.csv", "w") as file:
        w = csv.DictWriter(file, fieldnames = heading)
        w.writeheader()
        for i in data[0]["rates"]:
            w.writerow(i)
    return [i["code"] for i in data[0]["rates"]]
