import csv

startNumber = 0
endNumber = 255
number = startNumber

while startNumber < endNumber:
    print(number +1)
    with open('0to255.csv', 'w') as csvfile:
        writeCSV = csv.write(csvfile, delimiter=',')
