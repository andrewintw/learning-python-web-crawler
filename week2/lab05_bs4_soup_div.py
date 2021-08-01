import requests
import bs4

resp = requests.get('http://18.183.200.66/samples/sample5.html')
#print(resp.text)

soup = bs4.BeautifulSoup(resp.text, 'lxml')
#print(soup.text)


#div_list = soup.select_one('.stock_tbody').select('.stock_tr')
div_list = soup.select('.stock_tbody .stock_tr')

for div in div_list:
    print(div)