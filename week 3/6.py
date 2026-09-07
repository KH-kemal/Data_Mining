import pandas as pd

df = pd.read_csv('titanic.csv')

df['Age'] = df.groupby('Pclass')['Age'].transform(lambda x: x.fillna(x.mean()))

df['Age_scaled']= (df['Age'] - df['Age'].min()) / (df['Age'].max() - df['Age'].min())
df['fare_scaled']= (df['Fare'] - df['Fare'].min()) / (df['Fare'].max() - df['Fare'].min())

print(df[['Age', 'Age_scaled', 'Fare', 'fare_scaled']].head())