import pandas as pd
import numpy as np

# Load data
df = pd.read_csv('titanic.csv')

# 1. Isi missing values Age dengan Global Mean (bukan Pclass mean)
df['Age'] = df['Age'].fillna(df['Age'].mean())

# 2. Hitung Z-score standar (biarkan default ddof=1)
df['Age_zscore'] = (df['Age'] - df['Age'].mean()) / df['Age'].std()
df['Fare_zscore'] = (df['Fare'] - df['Fare'].mean()) / df['Fare'].std()

# 3. Hitung menggunakan Bipolar Sigmoidal: (1 - e^-z) / (1 + e^-z)
df['Age_sigmoid'] = (1 - np.exp(-df['Age_zscore'])) / (1 + np.exp(-df['Age_zscore']))
df['Fare_sigmoid'] = (1 - np.exp(-df['Fare_zscore'])) / (1 + np.exp(-df['Fare_zscore']))

# Tampilkan hasilnya
print(df[['Age', 'Fare', 'Age_sigmoid', 'Fare_sigmoid']].head(25))