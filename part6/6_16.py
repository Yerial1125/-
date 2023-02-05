import pandas as pd
import seaborn as sns

# titanic 데이터셋에서 age, sex 등 5개 열을 선택하여 데이터프레임 만들기
titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age','sex', 'class', 'fare', 'survived']]

grouped = df.groupby('class')
print(grouped)
print()

age_mean = grouped.age.mean()
print(age_mean)
print()

age_std = grouped.age.std()
print(age_std)
print()

for key, group in grouped.age:
    group_zscore = (group - age_mean.loc[key]) / age_std.loc[key]
    print('origin :', key)
    print(group_zscore.head(3))
    print()

# transform
def z_score(x) :
    return (x - x.mean()) / x.std()

age_zscore = grouped.age.transform(z_score)
print(age_zscore.loc[[1,9,0]])
print()
print(len(age_zscore))
print()
print(age_zscore.loc[0:9])
print()
print(type(age_zscore))
