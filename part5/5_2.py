import seaborn as sns

df = sns.load_dataset('titanic')
print(df.head())

print()

# 누락데이터 확인
null_df = df.isnull()
print(null_df)

for col in null_df.columns :
    null_count = null_df[col].value_counts()
    try:
        print(col, ':', null_count[True])
    except:
        print(col, ':', 0)

# 누락데이터 제거 : 결측치가 500개 이상인 column 제거
df_thresh = df.dropna(axis=1, thresh=500)
print(df_thresh.columns)
print()

# 누락데이터 제거 : age컬럼에 결측치가 있는 열 제거
df_age = df.dropna(subset=['age'])
print(len(df_age))
print()
df_age.info()
