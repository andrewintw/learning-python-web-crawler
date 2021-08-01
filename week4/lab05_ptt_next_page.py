# pip install requests bs4 lxml
# pip install jieba

import requests
import bs4
import jieba
import csv
import json
import re
import time
import random
from models import Topic, StockDb, Article
from datetime import datetime


stock_csv= 'week4/Stock.csv'
db_path = 'week4/invest.db3'

stocks = set()
db = StockDb()

def prepare_stocks():
    with open(stock_csv, encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file)
        stock_list = list(csv_reader)
    for stock in stock_list[2:]:
        stocks.add(stock[1])

def get_text(o):
    return '' if o is None else o.text.strip(' \n')

def read_article(url, topicObj):
    html = requests.get('https://www.ptt.cc' + url)
    soup = bs4.BeautifulSoup(html.text, 'lxml')

    publishList = soup.select('.article-meta-value')

    try: # 可能出現問題的地方做例外處理
        publishDateString = publishList[3].text  # should be "Sat Jul 10 10:53:46 2021"

        # Ref: https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes
        # 為了從標題取得 year
        publishDateTime = datetime.strptime(publishDateString, '%c')
    except:
        return


    rows = soup.select('div.push')
    for row in rows:
        content = get_text(row.select_one('.push-content'))
        issuer  = get_text(row.select_one('.push-userid'))
        created = get_text(row.select_one('.push-ipdatetime'))

        try:
            createdDateTime = datetime.strptime(created, '%m/%d %H:%M')
        except:
            continue # 忽略這一筆，但繼續嘗試下一筆

        new_createdDateTime = datetime(publishDateTime.year, 
                                        createdDateTime.month, 
                                        createdDateTime.day, 
                                        createdDateTime.hour, 
                                        createdDateTime.minute)

        tokens = jieba.lcut(content)
        keywords = {}
        for token in tokens:
            if token in stocks:
                if token in keywords:
                    keywords[token] += 1
                else:
                    keywords[token] = 1

        #print(keywords)

        aObj = Article(0, topicObj.id, content, issuer, 
                        # https://www.sqlite.org/datatype3.html (2.2. Date and Time Datatype)
                        #   TEXT as ISO8601 strings ("YYYY-MM-DD HH:MM:SS.SSS")
                        # 將 python 的 datetime 轉為 sqlite 需要的 iso 格式
                        new_createdDateTime.strftime('%Y-%m-%d %H:%M:%S'), 
                        None if len(keywords) == 0 else json.dumps(keywords, ensure_ascii=False))
        
        aObj_new = db.isExistedArticle(aObj) or db.insertArticle(aObj)


def read_topic():
    html = requests.get('https://www.ptt.cc/bbs/Stock/index.html')
    soup = bs4.BeautifulSoup(html.text, 'lxml')

    paginButtonList = soup.select('.btn.wide')
    if len(paginButtonList) != 4:
        return

    pageLink = paginButtonList[1]['href']
    pageNumberString = re.findall('/bbs/Stock/index(\d*).html', pageLink)[0]
    if not pageNumberString.isdigit():
        return

    pageNumber = int(pageNumberString) + 1

    while True:
        rows = soup.select('div.r-ent')
        for row in rows:
            anchor = row.select_one('.title a')
            if anchor is not None:
                url     = anchor['href']
                title   = anchor.text
                count   = get_text(row.select_one('.nrec'))
                issuer  = get_text(row.select_one('.author'))
                created = get_text(row.select_one('.date'))

                tokens = jieba.lcut(title)
                keywords = {}
                for token in tokens:
                    if token in stocks:
                        if token in keywords:
                            keywords[token] += 1
                        else:
                            keywords[token] = 1

                #print(keywords)

                tObj = Topic(0, 
                            title, 
                            issuer, 
                            created, 
                            None if len(keywords) == 0 else json.dumps(keywords, ensure_ascii=False))

                # tObj_new = db.isExistedTopic(tObj)
                # if tObj_new is None:
                #     tObj_new = db.insertTopic(tObj)
    
                tObj_new = db.isExistedTopic(tObj) or db.insertTopic(tObj)

                read_article(url, tObj_new)

        pageNumber -= 1
        if pageNumber == 0:
            break

        # 避免過於頻繁地爬資料
        time.sleep(random.randint(20, 1000)/1000.0)

        print(pageNumber)
        html = requests.get(f'https://www.ptt.cc/bbs/Stock/index{pageNumber}.html')
        soup = bs4.BeautifulSoup(html.text, 'lxml')


prepare_stocks()
db.openDB(db_path)
read_topic()
db.closeDB()


# 測試時可以先刪除 DB 資料 (記得點 write changes)
# DELETE from topic
# DELETE from article