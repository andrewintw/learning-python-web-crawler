import pandas as pd
from pandas.io.json import read_json, to_json


df = pd.read_csv('week5/dataframe.csv', index_col=0) # 需要 utf-8 with BOM header
                                        # index_col=0 表示第一行是索引值
print(df)

# df.to_csv('week5/data2.csv')

to_json('week5/data2.json', df, force_ascii=False)
dfj = read_json('week5/data2.json')
