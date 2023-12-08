from pathlib import Path
import pandas as pd

# Adatok elérési útvonala
data_path = Path("C:/Users/Levente/OneDrive/Desktop/NGG/Python/data")

# 1. Feladat
sp500_data = pd.read_parquet(data_path / "sp500.parquet", engine="fastparquet")

# 2. Feladat
ff_factors_data = pd.read_parquet(data_path / "ff_factors.parquet", engine="fastparquet")

# 3. Feladat
merged_data = pd.merge(sp500_data, ff_factors_data, on='Date', how='left')

# 4. Feladat
merged_data['Excess Return'] = merged_data['Monthly Returns'] - merged_data['RF']

# 5. Feladat
merged_data.sort_values(by='Date')
merged_data['ex_ret_1'] = merged_data.groupby('Symbol')['Excess Return'].shift(-1)

# 6. Feladat
merged_data = merged_data.dropna(subset=['ex_ret_1'])
merged_data = merged_data.dropna(subset=['HML'])

# Eredmények kiírása
#print(merged_data.head())

# Amazon részvényhez tartozó sorok kiválasztása
amazon_data = merged_data[merged_data['Symbol'] == 'AMZN']

# Ticker oszlop törlése
amazon_data = amazon_data.drop(columns=['Symbol'])
# del amazon_data["Symbol"]

# Végső eredmények kiírása
print(amazon_data.head())