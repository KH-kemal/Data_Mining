import pandas as pd

dataset = pd.read_csv('titanic.csv')
rows, cols = dataset.shape
print(f"Jumlah baris: {rows}")
print(f"Jumlah kolom: {cols}")