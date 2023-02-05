# 라이브러리 불러오기
import pandas as pd
import seaborn as sns

# IPyhton 디스플레이 설정 변경
pd.set_option('display.max_columns', 10)    # 출력할 최대 열의 개수
pd.set_option('display.max_colwidth', 20)    # 출력할 열의 너비

# titanic 데이터셋에서 age, sex 등 5개 열을 선택하여 데이터프레임 만들기
titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age','sex', 'class', 'fare', 'survived']]
print(df.head())
print()

pdf1 = pd.pivot_table(df,
                      index='class',
                      columns='sex',
                      values='age',
                      aggfunc='mean')
print(pdf1.head())

pdf2 = pd.pivot_table(df,
                      index='class',
                      columns='sex',
                      values='survived',
                      aggfunc=['mean','sum'])
print(pdf2.head())

pdf3 = pd.pivot_table(df,
                      index = ['class','sex'],
                      columns= 'survived',
                      aggfunc=['mean','max'],
                      values=['age','fare'])
print(pdf3.head())
print()

print(pdf3.index)
print(pdf3.columns)
print()

print(pdf3.xs('First'))
print()

print(pdf3.xs(('First','female')))
print()

print(pdf3.xs('male', level='sex'))
print()

print(pdf3.xs(('Second','male'), level=[0,'sex']))
print()

print(pdf3.xs('mean', axis=1))
print()

print(pdf3.xs(('mean','age'), axis=1))
print()

print(pdf3.xs(1, level='survived', axis=1))
print()

print(pdf3.xs(('max','fare',0), level=[0,1,2], axis=1))

