from selenium import webdriver

login_url = "https://www.facebook.com"

chrome = webdriver.Chrome()
chrome.get(login_url) # 會打開 chrome 並顯示 "chrome 目前受到自動測試軟體控制"