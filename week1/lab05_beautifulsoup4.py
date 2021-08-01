import bs4
import cloudscraper
import time

url = 'https://www.mobile01.com/forumtopic.php?c=37&s=56'


scraper = cloudscraper.create_scraper()
#response = scraper.get(url)
#print(response.text)

#soup = bs4.BeautifulSoup(response.text, features="html.parser")
#soup = bs4.BeautifulSoup(response.text, 'lxml')
#print(soup.title)

#print(soup.find('div', class_='l-listTable__tbody'))
#print(len(soup.find('div', class_='l-listTable__tbody').find_all('div', class_='l-listTable__tr')))

#print(soup.select('div.l-listTable__tbody div.l-listTable__tr'))

#如果確定 listTable__tbody 只在 div 裡面有，可以省略 div
#len(soup.select('.l-listTable__tbody .l-listTable__tr'))

found = False

while not found:
    response = scraper.get(url)
    soup = bs4.BeautifulSoup(response.text, 'lxml')
    tr_lines = soup.select('div.l-listTable__tbody div.l-listTable__tr')

    if len(tr_lines) == 30:
        found = True
    else:
        time.sleep(5)
        continue

    for row in tr_lines:
        print('==========================')
        print(row)