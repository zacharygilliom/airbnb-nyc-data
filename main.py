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

# name and host name are only missing 16 and 21 entries respectively.  Small percent compared to the total 
# so we can just drop those rows
df.dropna(0, inplace=True, subset=['name',  'host_name'])
# print(df.isna().sum())

# we want to slice the data for specific columns and specific criteria based on outliers
df_slice = df[['price', 'minimum_nights',
			'number_of_reviews']]
df_slice = df_slice[df_slice['minimum_nights'] <= 500]
# df_slice = df_slice[df_slice['reviews_per_month'] <= 40]


# df = df[(df['reviews_per_month'] > 1.10) & (df['reviews_per_month'] < 1.30)]

# sns.barplot(x='room_type', y='price', data=df, hue='reviews_per_month')
plot_dfs = df[(df['price'] < 300) & (df['reviews_per_month'] <= 8)]
plot_data = pd.concat([plot_dfs['price'], plot_dfs['reviews_per_month']], axis=1)
# sns.pairplot(df_slice)
plt.subplot(321)
sns.kdeplot(df[df['price'] < 300]['price'], shade=True, color="r")
plt.subplot(312)
sns.barplot(x='room_type', y='price', data=df)
plt.subplot(322)
sns.kdeplot(df[df['reviews_per_month'] <= 4]['reviews_per_month'], shade=True)
plt.subplot(313)
sns.barplot(x='neighbourhood_group', y='price', data=df)
plt.show()

