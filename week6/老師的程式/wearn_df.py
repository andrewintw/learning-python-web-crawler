from models import StockDb
import pandas as pd
import bar_chart_race as bcr
from datetime import datetime
# pip install bar_chart_race
start_date = input('請輸入開始日期(yyyy-mm-dd)：')
end_date = input('請輸入結束日期(yyyy-mm-dd)：')

db = StockDb()
db.Open()

stock_values = db.search_stockvalue(start_date, end_date)

db.Close()

stock_names = []
for stock_value in stock_values:
    if stock_value.stock_name not in stock_names:
        stock_names.append(stock_value.stock_name)
# stock_names = [x for x in set(stock_value.stock_name for stock_value in stock_values)]

df = pd.DataFrame(columns=stock_names)
for stock_value in stock_values:
    df.loc[datetime.fromisoformat(stock_value.stock_date), stock_value.stock_name] = stock_value.stock_close
df = df.astype('float64')
bcr.bar_chart_race(df,filename='stock.mp4',
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
