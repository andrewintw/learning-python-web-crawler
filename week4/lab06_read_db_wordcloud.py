# pip install WordCloud
from models import StockDb
import json
from wordcloud import WordCloud


start_date = input('please input start date(yyyy-mm-dd): ')
end_date   = input('please input end date(yyyy-mm-dd): ')

db_path = 'week4/invest.db3'

db = StockDb()
db.openDB(db_path)

keyword_count = {}

articles = db.searchArticle(start_date, end_date)
for article in articles:
#    print(article)
    keywords = json.loads(article.keywords)
    for keyword in keywords:
        if keyword in keyword_count:
            keyword_count[keyword] += keywords[keyword]
        else:
            keyword_count[keyword] = keywords[keyword]

print(keyword_count)

db.closeDB()

# consola.ttf 不行，因為字體不支援中文編碼
wc = WordCloud(font_path='./msjh.ttf').generate_from_frequencies(keyword_count)
wc.to_file('./week4/stock.png')

# 特殊使用方式
# https://amueller.github.io/word_cloud/auto_examples/parrot.html