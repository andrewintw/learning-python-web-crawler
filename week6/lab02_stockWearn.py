import requests
import bs4

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
    openPrice  = tds[1].text.strip()
    highPrice  = tds[2].text.strip()
    lowPrice   = tds[3].text.strip()
    closePrice = tds[4].text.strip()
    volume     = tds[5].text.strip()
    # print(date, openPrice, highPrice, lowPrice, closePrice, volume)

    date_year  = int(date.split('/')[0]) + 1911;
    date_month = date.split('/')[1]
    date_day   = date.split('/')[2]
    iso_date = f'{date_year}-{date_month}-{date_day}'
    print(iso_date, openPrice, highPrice, lowPrice, closePrice, volume)


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