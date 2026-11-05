import pandas as pd

df = pd.DataFrame({'PhongBan': ['kinhdoanh', 'kythuat', 'nhansu', 'kinhdoanh', 'kythuat'],
                   'nhanvien': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
                   'luong': [5000, 6000, 5500, 7000, 6500]})
# 1. Sap xep luong giam dan
df_sorted = df.sort_values(by='luong', ascending=False)
# 2. Gom nhom theo PhongBan va tinh Luong Trung Binh & Tong Luong
bg_summary = df.groupby('PhongBan')['luong'].agg(['mean', 'sum', 'count'])
print(bg_summary)