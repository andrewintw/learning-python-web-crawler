import requests

#url = 'https://www.twse.com.tw/zh/'
url = 'https://www.mobile01.com/'

sen_headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
}


response = requests.get(url, headers=sen_headers)

# if response.status_code == 200:
#     print(response.text)

print(response.text)
