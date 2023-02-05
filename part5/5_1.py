import seaborn as sns

df = sns.load_dataset('titanic')
print(df.head())

df.info()
print()

# 결측치 개수 확인 --> dropna = False
deck = df.deck.value_counts(dropna=False)
print(deck)

print(df.head().isnull())
print()
print(df.head().notnull())
print(df.head().isna().sum())

