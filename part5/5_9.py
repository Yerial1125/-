import pandas as pd
import numpy as np

# read_csv() 함수로 df 생성
df = pd.read_csv('data/auto-mpg.csv', header=None)

# 열 이름을 지정
df.columns = ['mpg','cylinders','displacement','horsepower','weight',
              'acceleration','model year','origin','name']

# 각 열의 자료형 확인
df.info()
print()

# horsepower 열의 고유값 확인
horsepower_uni = df['horsepower'].unique()
print(horsepower_uni)
print()

# 누락 데이터('?') 삭제
df.horsepower.replace('?', np.nan, inplace=True)
df.horsepower.dropna(inplace=True)
df.horsepower = df.horsepower.astype('float')

# horsepower 열의 자료형 확인
print(df['horsepower'].dtypes)
print()

# origin 열의 고유값 확인
print(df.origin.unique())
print()

# 정수형 데이터를 문자형 데이터로 변환
df.origin.replace({1:'USA', 2:'EU', 3:'JPN'}, inplace=True)
print()

# origin 열의 고유값과 자료형 확인
print(df.origin.unique())
print(df.origin.dtypes)
print()

# origin 열의 문자열 자료형을 범주형으로 변환
df.origin = df.origin.astype('category')
print(df.origin.dtypes)
print()

# 범주형을 문자열로 다시 변환
df.origin = df.origin.astype('str')
print(df.origin.dtypes)
print()

# model year 열의 정수형을 범주형으로 변환
print(df['model year'].sample(3))
df['model year'] = df['model year'].astype('category')
print(df['model year'].sample(3))