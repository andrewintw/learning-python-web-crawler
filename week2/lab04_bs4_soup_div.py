import requests
import bs4

resp = requests.get('http://18.183.200.66/samples/sample4.html')
#print(resp.text)

soup = bs4.BeautifulSoup(resp.text, 'lxml')
#print(soup.text)

#div_list = soup.select('.stock_table .stock_tr')
#div_list = soup.select('div.stock_tr')
div_list = soup.select('.stock_tr') # 如果 .stock_tr 只有 div 有

for div in div_list:
    print(div)