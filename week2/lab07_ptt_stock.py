import requests
import bs4

host_site = 'https://www.ptt.cc'

def get_topics():
    resp = requests.get(host_site + '/bbs/Stock/index.html')
    soup = bs4.BeautifulSoup(resp.text, 'lxml')
    rows = soup.select('.r-list-container .r-ent')
    for row in rows:
        link   = row.select_one('.title a')
        if link is not None:
            url    = link['href']
            title  = get_text(link) 
            author = get_text(row.select_one('.meta .author'))
            date   = get_text(row.select_one('.meta .date'))
            print(url, title, author, date)
            get_articles(url)

def get_text(obj):
    return '' if obj is None else obj.text.rstrip('\n')

def get_articles(url):
    resp = requests.get(host_site + url)
    soup = bs4.BeautifulSoup(resp.text, 'lxml')
    push_rows = soup.select('div.push')
    for push in push_rows:
        if push is not None:
            # 方法一
            # if len(push.select('span')) == 4:
            #     push_userid   = push.select_one('.push-userid').text
            #     push_content  = push.select_one('.push-content').text
            #     push_datetime = push.select_one('.push-ipdatetime').text.rstrip('\n')
            #     print(push_userid, push_content, push_datetime)

            # 方法二
            #push_userid   = '' if (x:=push.select_one('.push-userid')) is None else x.text
            push_userid = get_text(push.select_one('.push-userid'))
            push_content  = get_text(push.select_one('.push-content'))
            push_datetime = get_text(push.select_one('.push-ipdatetime'))
            print(push_userid, push_content, push_datetime)


get_topics()