import pandas as pd

dataset = pd.read_csv('ruspini_missing.csv')
print('dataset\n',dataset)
dataset = dataset.fillna(dataset.groupby('class').transform('mean'))
print("dataset setelah pengisian missing values\n", dataset)