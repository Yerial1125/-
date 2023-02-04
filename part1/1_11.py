import pandas as pd

# DataFrame() 함수로 데이터프레임 변환. 변수 df에 저장
exam_data = {'이름' : [ '서준', '우현', '인아'],
             '수학' : [ 90, 80, 70],
             '영어' : [ 98, 89, 95],
             '음악' : [ 85, 95, 100],
             '체육' : [ 100, 90, 90]}
df = pd.DataFrame(exam_data)

df.set_index('이름', inplace=True)
print(df)
print()

a = df.loc['서준','음악']
print(a)

b = df.iloc[0,2]
print(b)
print()

c = df.loc['서준',['음악','체육']]
print(c)

d = df.iloc[0,[2,3]]
print(d)

e = df.loc['서준','음악':'체육']
print(e)

f = df.iloc[0,2:4]
print(f)

g = df.loc[['서준','우현'],['음악','체육']]
h = df.iloc[[0,1],[2,3]]
i = df.loc['서준':'우현', '음악':'체육']
j = df.iloc[0:2,2:]
print(g)
print(h)
print(i)
print(j)