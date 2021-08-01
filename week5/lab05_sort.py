import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('week5/dataframe.csv', index_col=0) # 需要 utf-8 with BOM header
                                        # index_col=0 表示第一行是索引值
print(df)

#             元大台灣50  元大臺灣ESG永續  元大高股息
# 2021-07-01   138.3      34.71  35.00
# 2021-07-02   138.3      34.70  35.20
# 2021-07-03   139.6      35.04  35.69

print(df.sort_values('元大臺灣ESG永續'))
print(df.sort_values('元大高股息',))

# kind: line, bar, barh, hist, box, kde, area, pie...
df.plot(kind='bar', title='ETF') # 這一行其實已經把圖片畫到畫布了，但是尚未顯示。必須配合使用後面的 plt 顯示。

plt.rcParams['font.sans-serif'] = ['Microsoft Jhenghei']
plt.rcParams['axes.unicode_minus'] = False
plt.xlabel('日期')
plt.ylabel('股價')
plt.show()