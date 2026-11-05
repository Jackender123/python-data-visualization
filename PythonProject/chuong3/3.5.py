import pandas as pd
df = pd.DataFrame({'hoten':['Alice', 'Bob', 'Charlie', 'David'],
                   'diemtb':[8.5, 9.0, 7.5, 8.0]})
# 1. Dung map chuyen doi ten viet hoa
df['hoten'] = df['hoten'].map(lambda x: x.upper())
# 2. Dung apply voi lambda xep loai hoc luc
def xep_loai(score):
    if score >= 8.0:
        return 'Gioi'
    elif score >= 6.5:
        return 'Kha'
    elif score >= 5.0:
        return 'Trung binh'
    else:
        return 'Yeu'
df['xeploai'] = df['diemtb'].apply(xep_loai)
print(df)