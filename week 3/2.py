import pandas as pd

dataset = pd.read_csv('titanic.csv')
rows,cols = dataset.shape
print('jumlah baris\n',rows)
print('jumlah kolom\n',cols)
