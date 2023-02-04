import pandas as pd

# DataFrame() 함수로 데이터프레임 변환. 변수 df에 저장
exam_data = {'수학' : [ 90, 80, 70], '영어' : [ 98, 89, 95],
             '음악' : [ 85, 95, 100], '체육' : [ 100, 90, 90]}

df = pd.DataFrame(exam_data, index=['서준','우현','인아'])
print(df)
print()

label1 = df.loc['서준']
print(label1)
print()

position1 = df.iloc[0]
print(position1)
print()

# 여러 값 설정시 리스트!!!
label2 = df.loc[['서준','우현']]
print(label2)
print()

position2 = df.iloc[[0,1]]
print(position2)
print()

# 슬라이싱
label3 = df.loc['서준':'우현']
position3 = df.iloc[0:1]

print(label3)
print()
print(position3)