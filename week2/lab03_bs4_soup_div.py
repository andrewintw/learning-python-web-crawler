import requests
import bs4

resp = requests.get('http://18.183.200.66/samples/sample3.html')
#print(resp.text)

soup = bs4.BeautifulSoup(resp.text, 'lxml')
#print(soup.text)

div_list = soup.select('div')[2].select('div')

for div in div_list:
    print(div)