import pandas as pd

# MS = 월의 시작일 기준
ts_ms = pd.date_range(start='2019-01-01',
                      periods=6,
                      freq='MS',
                      tz='Asia/Seoul')
print(ts_ms)

# M = 월 간격, 월의 마지막날 기준
ts_me = pd.date_range(start='2019-01-01',
                      periods=6,
                      freq='M',
                      tz='Asia/Seoul')
print(ts_me)

# 3개월(분기) 간격, 월의 마지막날 기준
ts_3m = pd.date_range(start='2019-01-01',
                      periods=6,
                      freq='3M',
                      tz='Asia/Seoul')
print(ts_3m)
