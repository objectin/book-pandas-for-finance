import pprint

import pandas as pd

# 1
df = pd.read_excel('data/data_5710_20220716.xlsx', index_col=0)

df.index = pd.to_datetime(df.index)
df = df.sort_index()
# print(df, '\n')


# 2

df = pd.read_excel('data/data_5710_20220716.xlsx', parse_dates=['일자'])
df = df.sort_values('일자')
# print(df, '\n')


# print(df['일자'].dtype)
# print(type(df['일자'].iloc[0]))

# Groupby 월봉 OHCL
df = df[['일자', '시가', '저가', '고가', '종가', '거래량']].copy()
df['year'] = df['일자'].dt.year
df['month'] = df['일자'].dt.month
# print(df.head())
# print(df['year'])
# print(df['month'])

gb = df.groupby(['year', 'month'])
# print("==>> gb.get_group((2021, 9)).head(): \n", gb.get_group((2021, 9)).head())

how = {'시가': 'first', '고가': max, '저가': min, '종가': 'last', '거래량': sum}

print("==>> gb.agg(how): \n", gb.agg(how))
