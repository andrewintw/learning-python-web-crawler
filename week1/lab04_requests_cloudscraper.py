import cloudscraper

#url = 'https://www.twse.com.tw/zh/'
url = 'https://www.mobile01.com/'

scraper = cloudscraper.create_scraper()
response = scraper.get(url)

# if response.status_code == 200:
#     print(response.text)

print(response.text)
