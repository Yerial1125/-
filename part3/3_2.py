import pandas as pd

df = pd.read_csv('data/auto-mpg.csv', header=None)

df.columns = ['mpg','cylinders','displacement','horsepower','weight',
              'acceleration','model year','origin','name']

# 결측치 제외
print(df.count())
print(type(df.count()))

# 각 열의 고유값 개수, 결측치 포함 (dropna=*False)
unique_values = df['origin'].value_counts()
print(unique_values)
print()
print(type(unique_values))
