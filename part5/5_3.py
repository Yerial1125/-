import seaborn as sns

df = sns.load_dataset('titanic')
print(df.head(10))

print()

# 평균 나이(NaN 제외)
mean_age = df['age'].mean()
print(mean_age)
print()

df.age.fillna(mean_age, inplace=True)
print(df.age.head(10))