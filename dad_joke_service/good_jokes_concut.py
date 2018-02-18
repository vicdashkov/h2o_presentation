import csv

myData = [['is_dad_joke', "dad_joke"]]

i = 0
with open('dad_jokes.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if i != 1:
            myData.append([row['\ufeffis_dad_joke'].replace(u'\ufeff', ''), row['dad_joke'].replace(u'\ufeff', '').replace('\n', " ")])
        i += 1


myFile = open('very_clean_jokes.csv', 'w')
with myFile:
    writer = csv.writer(myFile)
    writer.writerows(myData)


# myFile = open('dad_jokes.csv', 'a', encoding='utf-8-sig')
# with myFile:
#     writer = csv.writer(myFile)
#     writer.writerows(myData)