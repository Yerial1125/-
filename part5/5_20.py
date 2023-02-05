import pandas as pd

# read_csv() 함수로 파일 읽어와서 df로 변환
df = pd.read_csv('data/stock-data.csv')

# 문자열인 날짜 데이터를 판다스 Timestamp로 변환
df['new_Date'] = pd.to_datetime(df['Date'])
df.set_index('new_Date', inplace=True)
print(df.head())
print()
print(df.index)
print()

# 시계열 데이터에 대한 인덱싱과 슬라이싱
df_y = df['2018']
print(df_y.head())
print()

df_ym = df.loc['2018-07']
print(df_ym)
print()

df_ym_cols = df.loc['2018-07','Start':'High']
print(df_ym_cols)
print()

# KeyError
# df_ymd = df['2018-07-02']
# print(df_ymd)
# print()

df_ymd_range = df['2018-06-20':'2018-06-25']
print(df_ymd_range)
print()

# 시간 간격 계산
today = pd.to_datetime('2018-12-25')
df['time_delta'] = today-df.index
df.set_index('time_delta', inplace=True)
df_180 = df['180 days':'189 days']
print(df_180)
print(df_180.index)