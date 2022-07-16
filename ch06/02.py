import pandas as pd

df = pd.read_excel('data/data_5710_20220716.xlsx', index_col=0)
df.index = df.to_datetime(df.index)
