import seaborn as sns

titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age','fare']]

# 각 열의 결측치 찾기 : DF --> DF
def missing_value(x) :
    return x.isnull()

# 각 열의 결측치 개수 반환 : DF --> S
def missing_count(x) :
    return missing_value(x).sum()

# 데이터 프레임의 총 결측치 개수 : DF --> scholar
def missing_total(x) :
    return missing_count(x).sum()

# pipe()
result_df = df.pipe(missing_value)
print(result_df.head())
print(type(result_df))
print()

result_series = df.pipe(missing_count)
print(result_series)
print(type(result_series))
print()

result_value = df.pipe(missing_total)
print(result_value)
print(type(result_value))
