import pandas as pd

# DataFrame() 함수로 데이터프레임 변환. 변수 df에 저장
exam_data = {'수학' : [ 90, 80, 70], '영어' : [ 98, 89, 95],
             '음악' : [ 85, 95, 100], '체육' : [ 100, 90, 90]}

df = pd.DataFrame(exam_data, index=['서준','우현','인아'])
print(df)
print()

df4 = df.copy()
df5 = df.copy()

df4 = df4.drop('수학', axis=1)
print(df4)
print()

df5 = df5.drop(['영어','음악'] ,axis=1)
print(df5)
