import pandas as pd
import numpy as np

# 딕셔너리 데이터로 판다스 시리즈 만들기
student1 = pd.Series({'국어':np.nan, '영어':80, '수학':90})
student2 = pd.Series({'수학':80, '국어':90})

print(student1)
print('\n')
print(student2)
print('\n')

# 두 학생의 과목별 점수로 사칙연산 수행 (시리즈 vs. 시리즈)
add = student1 + student2
sub = student1 - student2
mul = student1 * student2
div = student1 / student2

# 공통 인덱스가 없거나 NaN이 포함된 경우, 결과도 NaN
result = pd.DataFrame([add,sub,mul,div],
                      index=['덧셈','뺄셈','곱셈','나눗셈'])
print(result)