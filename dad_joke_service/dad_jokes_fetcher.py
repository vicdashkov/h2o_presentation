import json
import csv

import requests

myData = [['is_dad_joke', "dad_joke"]]

myFile = open('dad_jokes.csv', 'w', encoding='utf-8-sig')
with myFile:
    writer = csv.writer(myFile)
    writer.writerows(myData)

i = 0

while i <= 10000:
    try:
        response = requests.get("https://icanhazdadjoke.com/", headers={"Accept":"application/json"})
        response_dict = json.loads(response.text)
        dad_joke = response_dict['joke'].strip()

        myData = [['1', dad_joke]]

        myFile = open('dad_jokes.csv', 'a', encoding='utf-8-sig')
        with myFile:
            writer = csv.writer(myFile)
            writer.writerows(myData)

        print("Writing complete: joke:", dad_joke,' i: ', i)
        i += 1
    except Exception as e:
        print(e)


