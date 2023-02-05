import seaborn as sns

titanic = sns.load_dataset('titanic')
df = titanic.loc[0:4, 'survived':'age']
print(df)
print()

# 열 이름의 리스트 만들기
# print(df.columns) --> 인덱스리스트
columns = list(df.columns.values)
print(columns)
print()

# 열 순서 정렬 : 알파벳 순
columns_sorted = sorted(columns)
df_sorted = df[columns_sorted]
print(df_sorted)
print()

# 열 순서 정렬 : 기존데이터의 정반대 순
columns_reversed = reversed(columns)
df_reversed = df[columns_reversed]
print(df_reversed)
print()

# 임의 순서
columns_customed = ['pclass','sex','age','survived']
df_customed = df[columns_customed]
print(df_customed)