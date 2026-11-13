import numpy as np
import pandas as pd
data = {
    'MSSV': ['B2001', 'B2002', 'B2003', 'B2004', 'B2005', 'B2006', 'B2007', 'B2008'],
    'HoTen': ['Nguyễn Văn An', 'Trần Thị Bình', 'Lê Hoàng Cường', 'Phạm Minh Dung', 
              'Phan Văn Giang', 'Vũ Thị Hoa', 'Đặng Quốc Khánh', 'Bùi Lan Huệ'],
    'Nhom': ['Nhóm 1', 'Nhóm 2', 'Nhóm 1', 'Nhóm 2', 'Nhóm 1', 'Nhóm 2', 'Nhóm 1', 'Nhóm 2'],
    'DiemQuaTrinh': [8.5, 7.0, 9.5, 1000, 6.5, np.nan, 8.0, 5.5],
    'DiemThi': [7.5, 8.0, 9.0, 10000, 7.0, 8.5, np.nan, 6.0]
}
df = pd.DataFrame(data)
#1 --kham pha data--
print(df.head())
#1.2 --so luong gia tri thieu--
print(df.isnull().sum())
#1.3 thay gia tri khuyet bang diem trung binh cua cot tuong ung
df['DiemQuaTrinh'] = df['DiemQuaTrinh'].fillna(df['DiemQuaTrinh'].mean())
df['DiemThi'] = df['DiemThi'].fillna(df['DiemThi'].mean())
#2 thong ke va mo ta tu phan vi
#2.1 thong ke cot diem thi
print("mean:",df['DiemThi'].mean())
print("median:",df['DiemThi'].median())

q1 = df['DiemThi'].quantile(0.25)
q3 = df['DiemThi'].quantile(0.75)
print("Q1:", q1)
print("Q3:", q3)
#3tao cot mot va phan loai
df['DiemTongKet']=(df['DiemQuaTrinh']*0.4+df['DiemThi']*0.6).round(2)
df['KetQua'] = np.where(df['DiemTongKet'] >= 5, 'Đậu', 'Rớt')
print("\n--- DataFrame sau khi thêm cột ---")
print(df)