import json
import time
import csv


datatime = time.strftime("%Y-%m-%d-%H:%M:%S")

with open('static/data/PowerSubLoop01.json', 'r') as a:
    subpower14 = json.load(a)
    subpower14["datatime"] = str(datatime)
a.close
with open("static/data/"+time.strftime("%Y-%m-%d")+"-SubLoop01.csv", "a", newline="")as csvfile:
    csv.writerow(subpower14)
    #csv.dump(subpower14, csvfile)
csvfile.close