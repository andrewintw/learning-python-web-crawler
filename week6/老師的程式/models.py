import sqlite3

class Topic:
    def __init__(self, id, title, issuer, created, keywords):
        self.id = id
        self.title = title
        self.issuer = issuer
        self.created = created
        self.keywords = keywords

    def __str__(self) -> str:
        return f'{self.id} {self.title}'

class Article:
    def __init__(self, id, topic_id, content, issuer, created, keywords) -> None:
        self.id = id
        self.topic_id = topic_id
        self.content = content
        self.issuer = issuer
        self.created = created
        self.keywords = keywords

    def __str__(self) -> str:
        return f'{self.id} {self.content}'

class Stock:
    def __init__(self, stock_id, stock_name):
        self.stock_id = stock_id
        self.stock_name = stock_name

    def __str__(self):
        return f'{self.stock_id} {self.stock_name}'

class StockValue:
    def __init__(self, stock_id, stock_date, stock_open, stock_max, stock_min, stock_close, stock_quantity,
        stock_name = None) -> None:

        self.stock_id = stock_id
        self.stock_date = stock_date
        self.stock_open = stock_open
        self.stock_max = stock_max
        self.stock_min = stock_min
        self.stock_close = stock_close
        self.stock_quantity = stock_quantity
        self.stock_name = stock_name

class StockDb:
    def Open(self):
        self.connection = sqlite3.connect('invest.db3')

    def Close(self):
        self.connection.close()

    def insert_topic(self, t):
        sql = "INSERT INTO topic(title, issuer, created, keywords) VALUES(:title, :issuer, :created, :keywords) "
        val = { 'title': t.title, 'issuer': t.issuer, 'created': t.created, 'keywords': t.keywords }
        cur = self.connection.cursor()
        cur.execute(sql, val)
        t.id = cur.lastrowid
        self.connection.commit()
        cur.close()
        return t

    def isexisted_topic(self, t):
        sql = "SELECT * FROM topic WHERE title=:title AND issuer=:issuer AND created=:created"
        val = { 'title': t.title, 'issuer': t.issuer, 'created': t.created }
        cur = self.connection.cursor()
        cur.execute(sql, val)
        results = cur.fetchall()
        return None if len(results) == 0 else Topic(results[0][0], results[0][1], results[0][2], results[0][3], results[0][4])

    def insert_article(self, a):
        sql = "INSERT INTO article(topic_id, content, issuer, created, keywords) VALUES(:topic_id, :content, :issuer, :created, :keywords) "
        val = { 'topic_id': a.topic_id, 'content': a.content, 'issuer': a.issuer, 'created': a.created, 'keywords': a.keywords }
        cur = self.connection.cursor()
        cur.execute(sql, val)
        a.id = cur.lastrowid
        self.connection.commit()
        cur.close()
        return a

    def isexisted_article(self, a):
        sql = "SELECT * FROM article WHERE content=:content AND issuer=:issuer AND created=:created"
        val = { 'content': a.content, 'issuer': a.issuer, 'created': a.created }
        cur = self.connection.cursor()
        cur.execute(sql, val)
        results = cur.fetchall()
        return None if len(results) == 0 else Article(results[0][0], results[0][1], results[0][2], results[0][3], results[0][4], results[0][5])

    def search_article(self, start_date, end_date):
        sql = "SELECT * FROM article WHERE created>=:start_date AND created<=:end_date AND keywords IS NOT NULL"
        val = { 'start_date': start_date, 'end_date': end_date }
        cur = self.connection.cursor()
        cur.execute(sql, val)
        results = cur.fetchall()

        article_list = []
        for result in results:
            article_list.append(Article(result[0], result[1], result[2], result[3], result[4], result[5]))

        return article_list

    def insert_stock(self, s):
        try:
            sql = "INSERT INTO stock(stock_id, stock_name) VALUES(:stock_id, :stock_name) "
            val = { 'stock_id': s.stock_id, 'stock_name': s.stock_name }
            cur = self.connection.cursor()
            cur.execute(sql, val)
            self.connection.commit()
        except Exception as e:
            print(e)
        finally:
            cur.close()

    def search_stock(self):
        sql = "SELECT * FROM stock"
        val = { }
        cur = self.connection.cursor()
        cur.execute(sql, val)
        results = cur.fetchall()

        stock_list = []
        for result in results:
            stock_list.append(Stock(result[0], result[1]))

        return stock_list

    def insert_stockvalue(self, v):
        try:
            sql = "INSERT INTO stock_value(stock_id, stock_date, stock_open, stock_max, stock_min, stock_close, stock_quantity) VALUES(:stock_id, :stock_date, :stock_open, :stock_max, :stock_min, :stock_close, :stock_quantity) "
            val = { 'stock_id': v.stock_id, 'stock_date': v.stock_date, 'stock_open': v.stock_open, 'stock_max': v.stock_max, 'stock_min': v.stock_min, 'stock_close': v.stock_close, 'stock_quantity': v.stock_quantity }
            cur = self.connection.cursor()
            cur.execute(sql, val)
            self.connection.commit()
        except Exception as e:
            # print(e)
            pass
        finally:
            cur.close()
            
    def search_stockvalue(self, start_date, end_date):
        sql = """
            SELECT stock_value.*,stock_name
            FROM stock_value
            JOIN stock ON stock.stock_id=stock_value.stock_id
            WHERE stock_date>=:start_date AND stock_date<=:end_date
        """
        val = { 'start_date': start_date, 'end_date': end_date }
        cur = self.connection.cursor()
        cur.execute(sql, val)
        results = cur.fetchall()

        stockvalue_list = []
        for result in results:
            stockvalue_list.append(
                StockValue(result[0],
                    result[1],
                    result[2],
                    result[3],
                    result[4],
                    result[5],
                    result[6],
                    result[7]))

        return stockvalue_list            