import requests
import bs4
import time
import random
from models import StockDb, StockValue

db = StockDb()
db.Open()

stocks = db.search_stock()
for stock in stocks:
    print(stock.stock_id,stock.stock_name)
    response = requests.get(f'https://stock.wearn.com/cdata.asp?year=110&month=07&kind={stock.stock_id}')
    response.encoding = 'big5'
    soup = bs4.BeautifulSoup(response.text, 'lxml')
    tables = soup.select('table')
    stock_table = tables[0]
    rows = stock_table.select('tr')

    for row in rows[2:]:
        cols = row.select('td')
        date = cols[0].text.split('/')
        try:
            new_date = f'{int(date[0]) + 1911}-{date[1]}-{date[2]}'
            v = StockValue(stock.stock_id,
                            new_date,
                            float(cols[1].text.replace(',', '')),
                            float(cols[2].text.replace(',', '')),
                            float(cols[3].text.replace(',', '')),
                            float(cols[4].text.replace(',', '')),
                            int(cols[5].text.replace(',','')))
            db.insert_stockvalue(v)
        except:
            pass

    time.sleep(random.randint(500, 1000) / 1000.0)

db.Close()
