import pandas as pd

# 중복 데이터를 갖는 데이터프레임 만들기
df = pd.DataFrame({'c1':['a', 'a', 'b', 'a', 'b'],
                  'c2':[1, 1, 1, 2, 2],
                  'c3':[1, 1, 2, 2, 2]})
print(df)
print()

# 데이터셋 중복 제거
df2 = df.drop_duplicates()
print(df2)
print()

df3= df.drop_duplicates(subset=['c2','c3'])
print(df3)