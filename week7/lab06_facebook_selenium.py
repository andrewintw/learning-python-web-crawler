from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import base64
import time


login_url = "https://www.facebook.com"
my_email  = "YOUR_EMAIL"
my_passws = "YOUR_PASSWD"



chrome = webdriver.Chrome()
# chrome.implicitly_wait(5) # 這招好像沒用
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


# 概念: 送出 ctrl+END 按鍵
body = chrome.find_element_by_tag_name('body')

for i in range(10):
    # 進入頁面後，按 10 下 ctrl+END
    body.send_keys(Keys.CONTROL, Keys.END)
    time.sleep(5)
    print(i)

# 然後才抓 xpath
articles = chrome.find_elements_by_xpath('//div[@data-ad-comet-preview="message"]')

for article in articles:
    print(article.text)
