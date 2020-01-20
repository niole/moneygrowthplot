from typing import List, Tuple
from datetime import datetime
import os

Row = Tuple[str, float]
Columns = List[Row]

def parseRow(columns: List[str]) -> Row:
    col1 = columns[0].replace('\t', '')
    col2 = columns[1]
    date = datetime.strptime(col1, '%A, %B %d, %Y')
    money = float(col2.replace('\n', '').replace(',',''))
    return (date, money)

def parseColumnsFromFile() -> Columns:
    f= open("./personalValue.txt","r")
    lines = f.readlines()

    splitColumns = list(map(lambda line: line.split('$'), lines))

    f.close()

    return list(map(parseRow, splitColumns))

def createCSV(columns: Columns) -> None:
    if os.path.exists('./personalValue.csv'):
        print('..removing old csv')
        os.remove('./personalValue.csv')
    print('..writing new csv')
    content = '\n'.join([f'{x[0]},{x[1]}' for x in columns])
    content = 'date,money\n' + content
    newFile = open("./personalValue.csv", "w")
    newFile.write(content)
    newFile.close()
    return

def writeNewCSV() -> None:
    columns = parseColumnsFromFile()
    createCSV(columns)
