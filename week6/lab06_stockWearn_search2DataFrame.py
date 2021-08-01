import pandas as pd
import bar_chart_race as bcr
import csv
from datetime import datetime
from models import StockDb, StockHistory

def openMyDB(db_path):
    dbObj = StockDb()
    dbObj.openDB(db_path)
    return dbObj

def closeMyDB(dbObj):
    dbObj.closeDB()

# -----

start_date = '2021-07-01'
end_date   = '2021-07-23'

db = openMyDB('week6/invest.db3')
stock_history = db.searchStockHistory(start_date, end_date)
closeMyDB(db)


stock_names = []

# for stock_data in stock_history:
#     print(stock_data.stock_name, stock_data.trad_date, stock_data.close_price)
#     if stock_data.stock_name not in stock_names:
#         stock_names.append(stock_data.stock_name)

stock_names = [ x for x in set(stock_data.stock_name for stock_data in stock_history)]
# print(stock_names)

df = pd.DataFrame(columns=stock_names)
for stock_data in stock_history:
    # print(stock_data.stock_name, stock_data.trad_date, stock_data.close_price)
    df.loc[datetime.fromisoformat(stock_data.trad_date), stock_data.stock_name] = stock_data.close_price
print(df)
# df.to_csv("week6/stock_df.csv", encoding='utf-8')


df = df.astype('float64')
bcr.bar_chart_race( df=df,
                    filename='week6/stock_race.mp4',
                    orientation='h',
                    sort='desc',
                    n_bars=10,
                    fixed_order=False,
                    fixed_max=True,
                    steps_per_period=10,
                    interpolate_period=False,
                    label_bars=True,
                    bar_size=.95,
                    period_label={'x': .99, 'y': .25, 'ha': 'right', 'va': 'center'},
                    period_fmt='%B %d, %Y',
                    period_summary_func=lambda v, r: {'x': .99, 'y': .18,
                                                    's': f'Close Value: {v.nlargest(6).sum():,.0f}',
                                                    'ha': 'right', 'size': 8, 'family': 'Courier New'},
                    perpendicular_bar_func='median',
                    period_length=500,
                    figsize=(5, 3),
                    dpi=144,
                    cmap='dark12',
                    title='Stock Value',
                    title_size='',
                    bar_label_size=7,
                    tick_label_size=7,
                    shared_fontdict={'family' : 'Microsoft JhengHei', 'color' : '.1'},
                    scale='linear',
                    writer=None,
                    fig=None,
                    bar_kwargs={'alpha': .7},
                    filter_column_colors=True)

# period_fmt from
# https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes
# 必須 from datetime import datetime
# df.loc 裡面的時間格式要使用 datetime.fromisoformat() 處理過