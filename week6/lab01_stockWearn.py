import requests
import bs4
from datetime import datetime

year='110'
month='07'
kind='0050'

url = 'https://stock.wearn.com/cdata.asp?year=' + year + '&month=' + month + '&kind=' + kind
response = requests.get(url)
response.encoding = 'big5'
# print(response.text)
soup = bs4.BeautifulSoup(response.text, 'lxml')

tr_lines = soup.select('div.stockalllist tr')

print(tr_lines)
for row in tr_lines:
    tds = row.select('td')
    if len(tds) == 6:
        date       = tds[0].text.strip()
        openPrice  = tds[1].text.strip()
        highPrice  = tds[2].text.strip()
        lowPrice   = tds[3].text.strip()
        closePrice = tds[4].text.strip()
        volume     = tds[5].text.strip()
        # print(date+openPrice+highPrice+lowPrice+closePrice+volume) # 我用這個來檢查 tds[].text 之後有沒有空白 XD
        print(date, openPrice, highPrice, lowPrice, closePrice, volume)