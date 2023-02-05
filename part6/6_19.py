import pandas as pd
import seaborn as sns

# titanic 데이터셋에서 age, sex 등 5개 열을 선택하여 데이터프레임 만들기
titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age','sex', 'class', 'fare', 'survived']]

# class 열, sex 열을 기준으로 분할
grouped = df.groupby(['class', 'sex'])

# 그룹 객체에 연산 메서드 적용
gdf = grouped.mean()
print(gdf)
print()

print(gdf.loc['First'])
print()

print(gdf.loc[('First', 'female')])
print()

# xs 인덱서
print(gdf.xs('male', level='sex'))
print()