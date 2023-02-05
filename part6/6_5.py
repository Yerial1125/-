import seaborn as sns

titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age','fare']]
df['ten'] = 10
print(df.head())
print()

# 함수 정의
def add_two_obj(a,b) :
    return a+b

# apply : 시리즈
df['add'] = df.apply(lambda x : add_two_obj(x['age'],x['ten']), axis=1)
print(df.head())
print()
