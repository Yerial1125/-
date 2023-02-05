import pandas as pd

# 중복 데이터를 갖는 데이터프레임 만들기
df = pd.DataFrame({'c1':['a', 'a', 'b', 'a', 'b'],
                  'c2':[1, 1, 1, 2, 2],
                  'c3':[1, 1, 2, 2, 2]})
print(df)
print()

# 데이터셋 중복 확인
df_dup = df.duplicated()
print(df_dup)
print()

# 특정 컬럼 내 중복확인
col_dup = df.c2.duplicated()
print(col_dup)