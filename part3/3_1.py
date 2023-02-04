import pandas as pd

df = pd.read_csv('data/auto-mpg.csv', header=None)

df.columns = ['mpg','cylinders','displacement','horsepower','weight',
              'acceleration','model year','origin','name']

print(df.head())
print()
print(df.tail())

print('데이터프레임의 크기는',df.shape)
print()
print(df.info())
print()
print(df.dtypes)
print(df.origin.dtypes)
print()
print(df.describe())
print()
print(df.describe(include='all'))
print()
