import seaborn as sns

titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age','fare']]
print(df.head())
print()

# 함수 정의
def missing_value(series) :
    return series.isnull()

# apply : 시리즈 -> 시리즈 --> 데이터 프레임
result = df.apply(missing_value, axis=0)
print(result.head())
print()
print(type(result))