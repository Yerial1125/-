import pandas as pd
import seaborn as sns

# titanic 데이터셋에서 age, sex 등 5개 열을 선택하여 데이터프레임 만들기
titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age','sex', 'class', 'fare', 'survived']]

grouped = df.groupby('class')
print(grouped)
print()

# 필터링
grouped_filter = grouped.filter(lambda x: len(x) >= 200)
print(grouped_filter.head())
print(type(grouped_filter))
print()

age_filter = grouped.filter(lambda x: x.age.mean() <30)
print(age_filter.tail())
print()

