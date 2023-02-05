import pandas as pd
import numpy as np

# read_csv() 함수로 df 생성
df = pd.read_csv('data/auto-mpg.csv', header=None)

# 열 이름을 지정
df.columns = ['mpg','cylinders','displacement','horsepower','weight',
              'acceleration','model year','origin','name']

print(df.horsepower.unique())
df.horsepower.replace('?', np.nan, inplace=True)
df.dropna(subset='horsepower', inplace=True)
df.horsepower = df.horsepower.astype('float')

# 최댓값 확인
print(df.horsepower.describe())
print()

# 정규화2 --> 최솟값은 0, 최댓값은 1
min_x = df.horsepower - df.horsepower.min()
min_max = df.horsepower.max() - df.horsepower.min()
df.horsepower = min_x / min_max

print(df.horsepower.head())
print()
print(df.horsepower.describe())

