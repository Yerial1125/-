import pandas as pd

df = pd.read_csv('data/stock-data.csv')

print(df.head())
print()
print(df.info())

df['new_data'] = pd.to_datetime(df['Date'])
print()
print(df.head())
print()
print(df.info())
print()
print(type(df.new_data[0]))

df.set_index('new_data', inplace=True)
df.drop('Date', axis=1, inplace=True)

print(df.head())
print()
print(df.info())