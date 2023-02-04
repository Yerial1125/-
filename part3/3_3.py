import pandas as pd

df = pd.read_csv('data/auto-mpg.csv', header=None)
df.columns = ['mpg','cylinders','displacement','horsepower','weight',
              'acceleration','model year','origin','name']

# 평균값
print(df.mean())
print()
print(df['mpg'].mean())
print(df.mpg.mean())
print()
print(df[['mpg','weight']].mean())
print()

# 중간값
print(df.median())
print()
print(df.mpg.median())
print()

# 최댓값
# '?'이 포함되어 전체 데이터를 문자열로 인식, 아스키코드로 변환하여 최댓값 측정
print(df.max())
print()
print(df['mpg'].max())
print()

# 최솟값
print(df.min())
print()
print(df.mpg.min())
print()

# 표준편차
print(df.std())
print()
print(df['mpg'].std())

# 상관계수
print(df.corr())
print()
print(df[['mpg','weight']].corr())