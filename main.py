import pandas as pd

df = pd.read_csv('AB_NYC_2019.csv')

print(df.head())
print(df.columns)
print(df.dtypes)
print(df.isna())
print(df.isna().sum(), df.count())
df = df['name'].dropna(0)
print(df.isna().sum())