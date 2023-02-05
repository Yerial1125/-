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

# 정규화1 --> 범위 : 0~1 , 최댓값은 1
df.horsepower = df.horsepower/abs(df.horsepower.max())
print(df.horsepower.head())
print()
print(df.horsepower.describe())