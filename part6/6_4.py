import seaborn as sns

titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age','fare']]
print(df.head())
print()

# 함수 정의
def min_max(series) :
    return series.max() - series.min()

# apply : 시리즈 ->  scholar? --> 시리즈
result = df.apply(min_max, axis=0)
print(result)
print()
print(type(result))