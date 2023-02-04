import pandas as pd

# DataFrame() 함수로 데이터프레임 변환. 변수 df에 저장
exam_data = {'이름' : [ '서준', '우현', '인아'],
             '수학' : [ 90, 80, 70],
             '영어' : [ 98, 89, 95],
             '음악' : [ 85, 95, 100],
             '체육' : [ 100, 90, 90]}
df = pd.DataFrame(exam_data)
print(df)
print(type(df))
print('\n')

math1 = df['수학']
print(math1)
print()

eng1 = df.영어
print(eng1)
print()

music_gym = df[['음악','체육']]
print(music_gym)
print()

# 데이터가 하나라도 리스트 형태로 주면 [데이터프레임] 형태 추출
math2 = df[['수학']]
print(math2)
print(type(math2))
print()

# 슬라이싱 활용
df_op = df.iloc[::-1]
print(df_op)