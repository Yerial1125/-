import pandas as pd

tup_data = ('영인', '2010-05-01', '여', True)
sr = pd.Series(tup_data, index=['이름','생년월일','성별','힉생여부'])

print(sr)

print(sr[0])
print(sr['이름'])
print()

# 여러 값을 선택할 때는 리스트 형태로!
print(sr[[1,2]])
print()
print(sr[['생년월일','성별']])

# 슬라이싱 - 정수형은 끝값 포함X, 문자열은 끝값 포함.ㅌ
print()
print(sr[1:2])
print()
print(sr['생년월일':'성별'])