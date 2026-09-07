import pandas as pd
import numpy as np

df = pd.read_csv('titanic.csv')
df['Age']= df.groupby('Pclass')['Age'].transform(lambda x: x.fillna(x.mean()))

df['Age_zscore_manual'] = (df['Age'] - df['Age'].mean()) / df['Age'].std(ddof=0)
df['Fare_zscore_manual'] = (df['Fare'] - df['Fare'].mean()) / df['Fare'].std(ddof=0)

df['Age_sigmoid'] = 1 / (1 + np.exp(-df['Age_zscore_manual']))
df['Fare_sigmoid'] = 1 / (1 + np.exp(-df['Fare_zscore_manual']))

print(df[['Age', 'Age_zscore_manual', 'Age_sigmoid', 'Fare', 'Fare_zscore_manual', 'Fare_sigmoid']].head())