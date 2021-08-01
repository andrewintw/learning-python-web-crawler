import requests
import bs4
from models import StockDb, StockHistory

db = StockDb()
db.openDB('week6/invest.db3')

year='110'
month='07'
kind='0050'

url = 'https://stock.wearn.com/cdata.asp?year=' + year + '&month=' + month + '&kind=' + kind
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
    # print(tds)
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
    print(iso_date, openPrice, highPrice, lowPrice, closePrice, volume)

    sObj = StockHistory(kind, iso_date, float(openPrice), float(highPrice), float(lowPrice), float(closePrice), int(volume))
    db.insertStockHistory(sObj)

db.closeDB()



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