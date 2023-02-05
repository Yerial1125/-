import seaborn as sns

df = sns.load_dataset('titanic')
print(df.embark_town[825:830])
print()

# embark_town 최빈값
# .idxmax() --> value값이 가장 큰 index


most_freq = df['embark_town'].value_counts().idxmax()
print(most_freq)
print()

# 결측치 변환
df.embark_town.fillna(most_freq, inplace=True)
print(df.embark_town[825:830])