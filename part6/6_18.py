import pandas as pd
import seaborn as sns

# titanic 데이터셋에서 age, sex 등 5개 열을 선택하여 데이터프레임 만들기
titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age','sex', 'class', 'fare', 'survived']]

grouped = df.groupby('class')
print(grouped)
print()

# 함수 매핑 : 집계
agg_grouped = grouped.apply(lambda x: x.describe())
print(agg_grouped)
print()

# zscore 사용자 정의 함수
def zscore(x):
    return (x-x.mean())/x.std()

age_zscore = grouped.age.apply(zscore)
print(age_zscore.head())

# 필터링
age_filter = grouped.apply(lambda x: x.age.mean() < 30)
print(age_filter)
print()
for x in age_filter.index :
    if age_filter[x] == True:
        age_filter_df = grouped.get_group(x)
        print(age_filter_df.head())
        print()