import requests
import csv
from models import StockDb, Stock

url = 'https://www.twse.com.tw/exchangeReport/BFT41U?response=csv&date=20210716&selectType=ALLBUT0999'
resp = requests.get(url)
# print(resp.text)

# csv_reader = csv.reader(resp.text)
csv_reader = csv.reader(resp.text.split('\n'), delimiter=',')
lines = list(csv_reader)

db = StockDb()
db.openDB('week5/invest.db3')

for line in lines:
    if len(line) == 9:
        # print(line)
        stock_id   = line[0].strip(' ="')
        stock_name = line[1]

        if stock_id[0].isdigit():
            print(stock_id, stock_name)
            sObj = Stock(stock_id, stock_name)
            db.insertStock(sObj)


db.closeDB()