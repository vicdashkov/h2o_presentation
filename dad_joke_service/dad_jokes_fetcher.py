import json
import csv

import requests

myData = [['is_dad_joke', "dad_joke"]]

myFile = open('dad_jokes.csv', 'w', encoding='utf-8-sig')
with myFile:
    writer = csv.writer(myFile)
    writer.writerows(myData)

i = 0



myFile = open('dad_jokes.csv', 'a', encoding='utf-8-sig')
with myFile:
    writer = csv.writer(myFile)
    writer.writerows(myData)

print("Writing complete: joke:", dad_joke,' i: ', i)
i += 1

