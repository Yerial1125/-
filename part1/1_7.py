import pandas as pd

# DataFrame() 함수로 데이터프레임 변환. 변수 df에 저장
exam_data = {'수학' : [ 90, 80, 70], '영어' : [ 98, 89, 95],
             '음악' : [ 85, 95, 100], '체육' : [ 100, 90, 90]}

df = pd.DataFrame(exam_data, index=['서준','우현','인아'])
print(df)

df2 = df[:]
df3 = df[:]

df2.drop('우현', inplace = True)
print(df2)
print()

df3.drop(['우현','인아'], inplace=True)
print(df3)
