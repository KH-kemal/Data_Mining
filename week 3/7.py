import pandas as pd

df = pd.read_csv('titanic.csv')
df['Age'] = df.groupby('Pclass')['Age'].transform(lambda x: x.fillna(x.mean()))

df['Age_zscore'] = (df['Age'] - df['Age'].mean()) / df['Age'].std()
df['Fare_zscore'] = (df['Fare'] - df['Fare'].mean()) / df['Fare'].std()

print(df[['Age', 'Age_zscore', 'Fare', 'Fare_zscore']].head())