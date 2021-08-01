import bs4
import cloudscraper
import time

url = 'https://www.mobile01.com/forumtopic.php?c=37&s=56'


scraper = cloudscraper.create_scraper()

found = False

while not found:
    response = scraper.get(url)
    soup = bs4.BeautifulSoup(response.text, 'lxml')
    tr_lines = soup.select('div.l-listTable__tbody div.l-listTable__tr')

    if len(tr_lines) == 30:
        found = True
    else:
        print('.')
        time.sleep(5)
        continue

    for row in tr_lines:
        print('===============================')
        #print(row)

        link_a = row.select_one('a')
        #print(link_a['href'], link_a.text)
        url   = link_a['href']
        title = link_a.text

        publish_set      = row.select_one('.l-listTable__td.l-listTable__td--time')
        publish_username = publish_set.select_one('a').text
        publish_time     = publish_set.select_one('.o-fNotes').text
        publish_count    = row.select_one('.o-fMini').text
        print(url, title, publish_username, publish_time, publish_count)