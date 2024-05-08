import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('breadprice.csv')

df.dropna(inplace=True)

df['Year'] = pd.to_datetime(df['Year'], format='%Y')
df.set_index('Year', inplace=True)
df_mean_year = df.resample('YE').mean()

plt.figure(figsize=(10, 6))
plt.plot(df_mean_year.index.year, df_mean_year.mean(axis=1), marker='o', linestyle='-')
plt.title('Average Price of Bread per Year')
plt.xlabel('Year')
plt.ylabel('Average Price')
plt.grid(True)
plt.show()
