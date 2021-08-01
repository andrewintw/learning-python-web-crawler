from selenium import webdriver
import base64
import time

login_url = "https://www.facebook.com"
my_email  = "YOUR_EMAIL"
my_passws = "YOUR_PASSWD"


chrome = webdriver.Chrome()
chrome.get(login_url)

# print(chrome.name)
# print(chrome.title)
# print(chrome.session_id)
# print(chrome.find_elements_by_name("email"))

email = chrome.find_element_by_id('email')
email.send_keys(my_email)

password = chrome.find_element_by_id('pass')
password.send_keys(my_passws)
password.submit() # 也可以用 email  呼叫，似乎只要是 form 裡面的元素都可以呼叫 submit()。
time.sleep(5)


chrome.get("https://www.facebook.com/groups/170367376462405")
time.sleep(5)

# articles = chrome.find_elements_by_css_selector('div.qzhwtbm6.knvmm38d')
# print(len(articles))

# for article in articles:
#     print(article)


articles = chrome.find_elements_by_xpath('//div[@data-ad-comet-preview="message"]')

# $x('//div[@data-ad-comet-preview="message"]')

'''
<div class="ecm0bbzt hv4rvrfc e5nlhep0 dati1w0a" data-ad-comet-preview="message" data-ad-preview="message" id="jsc_c_b">
'''

for article in articles:
    print(article.text)

# 輸出可能只會有一筆，原因是 SPA 的網頁是要往下捲才會再載入
# 拿到貼文後，可以再用前面教的東西做聲量分析

