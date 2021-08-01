from models import StockDb, StockHistory

def openMyDB(db_path):
    dbObj = StockDb()
    dbObj.openDB(db_path)
    return dbObj

def closeMyDB(dbObj):
    dbObj.closeDB()

# -----

start_date = '2021-07-15'
end_date   = '2021-07-16'

db = openMyDB('week6/invest.db3')

stock_history = db.searchStockHistory(start_date, end_date)
for stock_data in stock_history:
    print(stock_data.stock_name, stock_data.trad_date, stock_data.close_price)


closeMyDB(db)