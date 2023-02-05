import pandas as pd

# Period 배열 만들기 : 1개월 길이
pr_m = pd.period_range(start='2019-01-01',
                      periods=3,
                      freq='M')
print(pr_m)
print()

# Period 배열 만들기 : 1시간 길이
pr_h = pd.period_range(start='2019-01-01',
                       periods=3,
                       freq='H')
print(pr_h)
print()

# Period 배열 만들기 : 3시간 길이
pr_3h = pd.period_range(start='2019-01-01',
                       periods=3,
                       freq='3H')
print(pr_3h)
print()

