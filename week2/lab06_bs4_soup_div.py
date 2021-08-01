import requests
import bs4

resp = requests.get('http://18.183.200.66/samples/sample6.html')
#print(resp.text)

soup = bs4.BeautifulSoup(resp.text, 'lxml')
#print(soup.text)


#div_list = soup.select_one('.stock_tbody').select('.stock_tr')
div_list = soup.select('.stock_tbody .stock_tr')


# 注意 select() 和 select_one() 的回傳差異
for div in div_list:
    #title = div.select('div')[0].text
    #title = div.select('.title')[0].text # 物件才有 .text() 可以操作, select 會回傳 list, 所以需要用 [0] 取出第一個
    title = div.select_one('.title').text # 但如果是 select_one() 就可以直接取出物件
    time  = div.select_one('.time').text
    #name  = div.select('div')[2].text
    name  = div.select_one('.name').text
    count = div.select_one('.count').text
    print(title, time, name, count)