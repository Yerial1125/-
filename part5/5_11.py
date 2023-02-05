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

# numpy 의 histogram
counts, bin_dividers = np.histogram(df['horsepower'], bins=3)
print(counts, '\n', bin_dividers)

df['hp_bin'] = pd.cut(x=df.horsepower, bins = bin_dividers,
                              labels=['저출력', '보통출력', '고출력'],
                              include_lowest=True)
print()

# 더미변수  -->  범주형 데이터를 머신러닝 알고리즘에 바로 사용할 수 없을 때, 컴퓨터가 인식가능한 입력값으로 변환!
horesepower_dummies = pd.get_dummies(df.hp_bin)
print(horesepower_dummies.head(10))
