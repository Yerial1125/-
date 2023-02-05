import pandas as pd

# IPyhton 디스플레이 설정 변경
pd.set_option('display.max_columns', 10)                  # 출력할 최대 열의 개수
pd.set_option('display.max_colwidth', 20)                 # 출력할 열의 너비
pd.set_option('display.unicode.east_asian_width', True)   # 유니코드 사용 너비 조정

# 주식 데이터를 가져와서 데이터프레임 만들기
df1 = pd.read_excel('data/stock price.xlsx', index_col='id', engine= 'openpyxl')
df2 = pd.read_excel('data/stock valuation.xlsx', index_col='id', engine= 'openpyxl')

# 데이터프레임 결합(join) --> 행기준으로 결합
df3 = df1.join(df2)
print(df3)
print('\n')

# 데이터프레임 결합(join) - 교집합
df4 = df1.join(df2, how='inner')
print(df4)