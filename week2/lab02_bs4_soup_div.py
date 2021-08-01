# 兩層 div, 真正的資料在第二層 div

import requests
import bs4

resp = requests.get('http://18.183.200.66/samples/sample2.html')
#print(resp.text)

soup = bs4.BeautifulSoup(resp.text, 'lxml')
#print(soup.text)

#div_list = soup.select('div')[0].select('div')
div_list = soup.select_one('div').select('div') # 只拿第一個 div

for div in div_list:
    print(div)