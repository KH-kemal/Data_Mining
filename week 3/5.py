import pandas as pd

df = pd.read_csv('titanic.csv')
print('jumlah missing values SEBELUM imputasi:\n',df[['Age']].isnull().sum())

df['Age']= df.groupby('Pclass')['Age'].transform(lambda x: x.fillna(x.mean()))

print('jumlah missing values SETELAH imputasi:\n',df[['Age']].isnull().sum())