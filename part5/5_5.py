import seaborn as sns

df = sns.load_dataset('titanic')
print(df.embark_town[825:830])
print()

# method
df.embark_town.fillna(method='ffill', inplace=True)
print(df.embark_town[825:830])
print()


