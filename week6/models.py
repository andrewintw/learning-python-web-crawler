import sqlite3

# db table 用的
class Topic:
    def __init__(self, id, title, issuer, created, keywords) -> None:
        # self.欄位 = 上面傳進來的
        self.id       = id
        self.title    = title
        self.issuer   = issuer
        self.created  = created
        self.keywords = keywords

    def __str__(self) -> str:
        return f'{self.id} {self.title}'

# 測試 Topic 物件程式
# tObj = Topic(1, 'Title', 'Issuer', 'Created', 'Keywords')
# print(tObj) # 比較 class 有加 __str__() 和沒加的結果
              # 不加顯示: <__main__.Topic object at 0x0047E490>


class Article:
    def __init__(self, id, topic_id, content, issuer, created, keywords) -> None:
        # self.欄位 = 上面傳進來的
        self.id       = id
        self.topic_id = topic_id
        self.content  = content
        self.issuer   = issuer
        self.created  = created
        self.keywords = keywords

    def __str__(self) -> str:
        return f'{self.id} {self.content}'


class Stock:
    def __init__(self, sid, sname) -> None:
        # self.欄位 = 上面傳進來的
        self.stock_id   = sid
        self.stock_name = sname

    def __str__(self) -> str:
        return f'{self.stock_id} {self.stock_name}'


# CREATE TABLE "stock_history" (
# 	"stock_id"	TEXT NOT NULL,
# 	"trad_date"	TEXT NOT NULL,
# 	"open_price"	REAL NOT NULL,
# 	"high_price"	REAL NOT NULL,
# 	"low_price"	REAL NOT NULL,
# 	"close_price"	REAL NOT NULL,
# 	"total_volume"	INTEGER NOT NULL,
# 	PRIMARY KEY("trad_date","stock_id")
# );

class StockHistory:
    def __init__(self, stockid, traddate, openprice, highprice, lowprice, closeprice, totalvolume, stockname=None) -> None:
        # self.欄位 = 上面傳進來的
        self.stock_id     = stockid
        self.trad_date    = traddate
        self.open_price   = openprice
        self.high_price   = highprice
        self.low_price    = lowprice
        self.close_price  = closeprice
        self.total_volume = totalvolume
        self.stock_name   = stockname

    def __str__(self) -> str:
        return f'{self.stock_id}'


class StockDb:
    def openDB(self, db_path):
        self.connection = sqlite3.connect(db_path)

    def closeDB(self):
        self.connection.close()

    def insertTopic(self, topicObj):
        sql = "INSERT INTO topic(title, issuer, created, keywords) VALUES (:sql_title, :sql_issuer, :sql_created, :sql_keywords)"
        val = { 'sql_title':    topicObj.title,
                'sql_issuer':   topicObj.issuer,
                'sql_created':  topicObj.created,
                'sql_keywords': topicObj.keywords }
        cur = self.connection.cursor()
        cur.execute(sql, val)
        topicObj.id = cur.lastrowid # 拿出 db insert 時的 id, 因為 id 是 db 自動產生的。
                                    # 其他 table 需要參照寫 FK 的時候需要先知道 id
        self.connection.commit()
        cur.close()
        return topicObj
    
# 需要關閉 cursor 嗎?
# https://stackoverflow.com/questions/2330344/in-python-with-sqlite-is-it-necessary-to-close-a-cursor
# python 3.0 會自動關閉。舊版本的文件並沒有提到有沒有自動關。但為了程式的可移植性，應該要習慣關閉。 

    def insertArticle(self, articleObj):
        sql = "INSERT INTO article(topic_id, content, issuer, created, keywords) VALUES (:sql_topic_id, :sql_content, :sql_issuer, :sql_created, :sql_keywords)"
        val = { 'sql_topic_id': articleObj.topic_id,
                'sql_content':  articleObj.content,
                'sql_issuer':   articleObj.issuer,
                'sql_created':  articleObj.created,
                'sql_keywords': articleObj.keywords }
        cur = self.connection.cursor()
        cur.execute(sql, val)
        articleObj.id = cur.lastrowid # 拿出 db insert 時的 id, 因為 id 是 db 自動產生的。
                                      # 其他 table 需要參照寫 FK 的時候需要先知道 id
        self.connection.commit()
        cur.close()
        return articleObj


    def isExistedTopic(self, topicObj):
        sql = "SELECT * FROM topic WHERE title=:sql_title AND issuer=:sql_issuer AND created=:sql_created"
        val = { 'sql_title':    topicObj.title,
                'sql_issuer':   topicObj.issuer,
                'sql_created':  topicObj.created }
        cur = self.connection.cursor()
        cur.execute(sql, val)
        results = cur.fetchall()
        cur.close()
        return None if len(results) == 0 else Topic(results[0][0], 
                                                    results[0][1], 
                                                    results[0][2], 
                                                    results[0][3], 
                                                    results[0][4])


    def isExistedArticle(self, articleObj):
        sql = "SELECT * FROM article WHERE topic_id=:sql_topic_id AND content=:sql_content AND issuer=:sql_issuer AND created=:sql_created"
        val = { 'sql_topic_id': articleObj.topic_id,
                'sql_content':  articleObj.content,
                'sql_issuer':   articleObj.issuer,
                'sql_created':  articleObj.created }
        cur = self.connection.cursor()
        cur.execute(sql, val)
        results = cur.fetchall()
        cur.close()
        return None if len(results) == 0 else Article(results[0][0], 
                                                    results[0][1], 
                                                    results[0][2], 
                                                    results[0][3], 
                                                    results[0][4],
                                                    results[0][5])

    # 回傳搜尋結果的 "物件清單"
    def searchArticle(self, start_date, end_date):
        sql = "SELECT * FROM article WHERE created>=:sql_start_date AND created<=:sql_end_date AND keywords IS NOT NULL"
        val = { 'sql_start_date': start_date,
                'sql_end_date':   end_date }
        cur = self.connection.cursor()
        cur.execute(sql, val)
        results = cur.fetchall()
        cur.close()

        article_list = []
        for result in results:
            article_list.append(Article(result[0], 
                                        result[1], 
                                        result[2], 
                                        result[3], 
                                        result[4],
                                        result[5]))
        return article_list


    def insertStock(self, stockObj):
        try:
            sql = "INSERT INTO stock(stock_id, stock_name) VALUES (:sql_stock_id, :sql_stock_name)"
            val = { 'sql_stock_id':   stockObj.stock_id,
                    'sql_stock_name': stockObj.stock_name }
            cur = self.connection.cursor()

            # 如果資料重複不寫入，之前的例子使用 isExistedXXX() 判斷 -- 需要對資料庫做搜尋
            # 但也可以偷懶讓 Exception 處理，對資料表的 PK 做寫入動作，如果資料不在就寫入，如果資料已經存在就會丟 Exception
            cur.execute(sql, val)
            self.connection.commit()
        except:
            pass
        finally: # 不管 try, except 執行後，都會執行 finally
            cur.close()

    def insertStockHistory(self, stockHisObj):
        try:
            sql = "INSERT INTO stock_history(stock_id, trad_date, open_price, high_price, low_price, close_price, total_volume) VALUES (:stockid, :traddate, :openprice, :highprice, :lowprice, :closeprice, :totalvolume)"
            val = { 'stockid':     stockHisObj.stock_id,
                    'traddate':    stockHisObj.trad_date,
                    'openprice':   stockHisObj.open_price,
                    'highprice':   stockHisObj.high_price,
                    'lowprice':    stockHisObj.low_price,
                    'closeprice':  stockHisObj.close_price,
                    'totalvolume': stockHisObj.total_volume }

            cur = self.connection.cursor()
            # 如果資料重複不寫入，之前的例子使用 isExistedXXX() 判斷 -- 需要對資料庫做搜尋
            # 但也可以偷懶讓 Exception 處理，對資料表的 PK 做寫入動作，如果資料不在就寫入，如果資料已經存在就會丟 Exception
            cur.execute(sql, val)
            self.connection.commit()
        except Exception as e:
            print(e) # for debug
            # pass
        finally: # 不管 try, except 執行後，都會執行 finally
            cur.close()


    def getAllStockList(self):
        sql = "SELECT * FROM stock"
        cur = self.connection.cursor()
        cur.execute(sql)
        results = cur.fetchall()
        cur.close()

        stock_list = []
        for result in results:
            stock_list.append(Stock(result[0], result[1]))

        return None if len(results) == 0 else stock_list


    def searchStockHistory(self, start_date, end_date):
        sql = """
                SELECT stock_history.stock_id, stock_name, trad_date, open_price, high_price, low_price, close_price, total_volume 
                FROM stock_history JOIN stock ON stock.stock_id == stock_history.stock_id 
                WHERE trad_date >= :sql_start_date AND trad_date <= :sql_end_date 
        """
        val = { 'sql_start_date': start_date,
                'sql_end_date'  : end_date }
        cur = self.connection.cursor()
        cur.execute(sql, val)
        results = cur.fetchall()
        cur.close()

        stock_list = []
        for result in results:
            stock_list.append(StockHistory(result[0], result[2], result[3], result[4], result[5], result[6], result[7], result[1]))

        return None if len(results) == 0 else stock_list