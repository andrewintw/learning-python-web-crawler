from selenium import webdriver
import base64

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

