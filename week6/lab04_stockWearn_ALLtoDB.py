import requests
import bs4
import time
import random

from models import StockDb, StockHistory

# CREATE TABLE "stock_history" (
# 	"stock_id"	TEXT NOT NULL,
# 	"trad_date"	TEXT NOT NULL,
# 	"open_price"	REAL NOT NULL,
# 	"high_price"	REAL NOT NULL,
# 	"low_price"	REAL NOT NULL,
# 	"close_price"	REAL NOT NULL,
# 	"total_volume"	INTEGER NOT NULL,
# 	PRIMARY KEY("trad_date","stock_id")
# );

def openMyDB(db_path):
    dbObj = StockDb()
    dbObj.openDB(db_path)
    return dbObj


def closeMyDB(dbObj):
    dbObj.closeDB()


def crawlStockToDB(year, month, stockObj):
    url = 'https://stock.wearn.com/cdata.asp?year=' + year + '&month=' + month + '&kind=' + stockObj.stock_id
    response = requests.get(url)
    response.encoding = 'big5'
    # print(response.text)
    soup = bs4.BeautifulSoup(response.text, 'lxml')

    tables = soup.select('table')
    stock_table = tables[0]
    rows = stock_table.select('tr')

    for row in rows[2:]:
        # print(row)
        tds = row.select('td')
        if len(tds) == 6:
            date       = tds[0].text.strip()
            openPrice  = tds[1].text.strip().replace(',', '')
            highPrice  = tds[2].text.strip().replace(',', '')
            lowPrice   = tds[3].text.strip().replace(',', '')
            closePrice = tds[4].text.strip().replace(',', '')
            volume     = tds[5].text.strip().replace(',', '')
            # print(date, openPrice, highPrice, lowPrice, closePrice, volume)

            date_year  = int(date.split('/')[0]) + 1911;
            date_month = date.split('/')[1]
            date_day   = date.split('/')[2]
            iso_date = f'{date_year}-{date_month}-{date_day}'
            print(stockObj.stock_id, iso_date, openPrice, highPrice, lowPrice, closePrice, volume)

            sObj = StockHistory(stockObj.stock_id, iso_date, float(openPrice), float(highPrice), float(lowPrice), float(closePrice), int(volume))
            db.insertStockHistory(sObj)
            # print('save2db> ' + stockObj.stock_id, stockObj.stock_name)
        else:
            print("ignore> " + stockObj.stock_id, stockObj.stock_name)

    time.sleep(random.randint(500, 1000)/1000.0) # dealy 0.5 ~ 1sec

#### main ####

db = openMyDB('week6/invest.db3')

stocks = db.getAllStockList()
for stock in stocks:
    # print(stock)
    crawlStockToDB('110', '07', stock)

closeMyDB(db)