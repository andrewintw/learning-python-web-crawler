from urllib.request import urlopen

#url='https://www.mobile01.com/'
url = 'https://www.twse.com.tw/zh/'

with urlopen(url) as response:
    print(response.read().decode('utf-8'))