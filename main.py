import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns 
import numpy as np 

sns.set_style('darkgrid')
df = pd.read_csv('AB_NYC_2019.csv')

print(df.head())
print(df.columns)
print(df.dtypes)
# print(df.isna())
# print(df.isna().sum(), df.count())
df.dropna(0, inplace=True, subset=['name',  'host_name'])
# print(df.isna().sum())

df = df[(df['reviews_per_month'] > 1.10) & (df['reviews_per_month'] < 1.30)]
# print(df['minimum_nights'].mean())

# sns.barplot(x='room_type', y='price', data=df, hue='reviews_per_month')
sns.pairplot(df)
plt.show()