import csv

myData = [['is_dad_joke', "dad_joke"]]


with open('good_jokes.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print('______________')
        print(row['title'], row['selftext'])
        myData.append(["0", row['title'] + " " + row['selftext']])


myFile = open('good_jokes_clean.csv', 'w', encoding='utf-8-sig')
with myFile:
    writer = csv.writer(myFile)
    writer.writerows(myData)