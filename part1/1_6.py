import pandas as pd

# 리스트 --> 행 인덱스
df = pd.DataFrame([[15, '남', '덕영중'], [17, '여', '수리중']],
                  index=['준서', '예은'],
                  columns=['나이','성별','학교'])

print(df)
print()
# rename 메소드 --> 파라미터 index/columns 딕셔너리 형태
# 일부 인덱스만 변경할 때 용이!!

df.rename(columns = {'나이':'연령','성별':'남녀','학교':'소속'}, inplace=True)
df.rename(index = {'준서':'학생1','예은':'학생2'}, inplace=True)
print(df)
print()

df.rename(columns = {'남녀':'성별'}, inplace=True)
print(df)