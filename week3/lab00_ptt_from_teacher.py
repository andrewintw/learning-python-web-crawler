# pip install requests bs4 lxml
# pip install jieba

import requests
import bs4
import jieba
import csv

stocks = set()
def prepare_stocks():
    with open('week3/Stock.csv', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file)
        stock_list = list(csv_reader)
    for stock in stock_list[2:]:
        stocks.add(stock[1])

def get_text(o):
    return '' if o is None else o.text

def read_article(url):
    html = requests.get('https://www.ptt.cc' + url)
    soup = bs4.BeautifulSoup(html.text, 'lxml')

    rows = soup.select('div.push')
    for row in rows:
        content = get_text(row.select_one('.push-content'))
        issuer = get_text(row.select_one('.push-userid'))
        created = get_text(row.select_one('.push-ipdatetime'))

        tokens = jieba.lcut(content)
        keywords = {}
        for token in tokens:
            if token in stocks:
                if token in keywords:
                    keywords[token] += 1
                else:
                    keywords[token] = 1

        print(keywords)

def read_topic():
    html = requests.get('https://www.ptt.cc/bbs/Stock/index.html')
    soup = bs4.BeautifulSoup(html.text, 'lxml')

    rows = soup.select('div.r-ent')
    for row in rows:
        anchor = row.select_one('.title a')
        if anchor is not None:
            url = anchor['href']
            title = anchor.text
            count = get_text(row.select_one('.nrec'))
            issuer = get_text(row.select_one('.author'))
            created = get_text(row.select_one('.date'))

            tokens = jieba.lcut(title)
            keywords = {}
            for token in tokens:
                if token in stocks:
                    if token in keywords:
                        keywords[token] += 1
                    else:
                        keywords[token] = 1

            print(keywords)
            read_article(url)

prepare_stocks()
read_topic()