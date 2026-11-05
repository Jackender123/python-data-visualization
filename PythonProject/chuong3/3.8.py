import pandas as pd
import numpy as np

df_raw = pd.DataFrame({'Hoten':['Alice', 'Bob', 'Charlie', 'David'],
                       'tuoi':[20, 21, 22, 23],
                       'luong':[5000, 6000, np.nan, 7000]})
# 1. Kiem tra so luong NaN
print("So luong NaN:\n", df_raw.isna().sum())
# 2. Dien gia tri NaN cua cot Tuoi bang Trung vi (Median)
df_clean = df_raw.copy()
df_clean['tuoi'] = df_clean['tuoi'].fillna(df_clean['tuoi'].median())
# 3. Dien NaN cua Luong bang Trung binh (Mean)
df_clean['luong'] = df_clean['luong'].fillna(df_clean['luong'].mean())
# 4. Xuat file CSV da lam sach
df_clean.to_csv('data_clean.csv', index=False, encoding='utf-8')