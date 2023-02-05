import seaborn as sns

titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age','fare']]
print(df.head())
print()

# 함수 정의
def add_10(n) :
    return n+10

# 데이터프레임 --> 함수 매핑
df_map = df.applymap(add_10)
print(df_map.head())
