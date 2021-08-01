import sqlite3

dbcon = sqlite3.connect('week3/invest.db3')

##########################################
# 使用問號代表即將傳入的參數，使用 tuple 對應數值
##########################################

# Insert
# sql = "INSERT INTO topic(title, issuer, created, keywords) VALUES (?, ?, ?, ?)"
# val = ('Test Title - Python', 'Hana', '2021-07-05', None)
# cur = dbcon.cursor()
# cur.execute(sql, val)
# dbcon.commit()
# cur.close()

# Select
# sql = "SELECT * FROM topic WHERE created>=? AND created<=?"
# val = ('2021-07-02', '2021-07-03')
# cur = dbcon.cursor()
# cur.execute(sql, val)
# result = cur.fetchall()
# print(result)
# cur.close()

# Update
# sql = "UPDATE topic SET created=? WHERE id=?"
# val = ('2021-07-07', 3)
# cur = dbcon.cursor()
# cur.execute(sql, val)
# dbcon.commit()
# cur.close()


# Delete
# sql = "DELETE FROM topic WHERE id=?"
# val = (6, ) # tuple 只有一筆資料時，後面要加 , 讓 python 知道這是 tuple
# cur = dbcon.cursor()
# cur.execute(sql, val)
# dbcon.commit()
# cur.close()

# 使用 ? 有個麻煩之處，當參數過多時，對應關係需要很小心地一一比對。

###############
# 使用代稱 & 字典
###############

# Insert 多筆 --> ? 改成代稱; 但 val 要使用字典
# sql = "INSERT INTO topic(title, issuer, created, keywords) VALUES (:sql_title, :sql_issuer, :sql_created, :sql_keywords)"
# val = { 'sql_title': 'SQL Python',
#         'sql_issuer': 'Hana',
#         'sql_created': '2021-07-03',
#         'sql_keywords': None }
# cur = dbcon.cursor()
# cur.execute(sql, val)
# dbcon.commit()
# cur.close()

# Select
# sql = "SELECT * FROM topic WHERE created>=:created_from AND created<=:created_to"
# val = { 'created_from': '2021-07-02', 
#         'created_to': '2021-07-03' }
# cur = dbcon.cursor()
# cur.execute(sql, val)
# result = cur.fetchall()
# print(result)
# cur.close()

# Update
# sql = "UPDATE topic SET created=:created WHERE id=:id"
# val = { 'created': '2021-07-04', 
#         'id': 2 }
# cur = dbcon.cursor()
# cur.execute(sql, val)
# dbcon.commit()
# cur.close()

# Delete
# sql = "DELETE FROM topic WHERE id=:del_id"
# val = { 'del_id': 7 }
# cur = dbcon.cursor()
# cur.execute(sql, val)
# dbcon.commit()
# cur.close()