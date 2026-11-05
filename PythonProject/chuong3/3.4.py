import pandas as pd

df = pd.DataFrame({'lop':['CNTT1','CNTT2','CNTT3','CNTT4','CNTT4'],
                   'diem':[8.5,9.0,7.5,8.0,9.5],
                   'hocphi':[1000,1200,1100,1300,1400]
                   },index = ['sv1','sv2','sv3','sv4','sv5'])
#1 truy xuat bang loc
sv1_diem = df.loc['sv1','diem']# 8.5
sub_df = df.iloc[0:2,0:2]# SV01, SV02 (dong 0->1, cot 0->1)
# 2. Loc danh sach SV DAT (Diem >= 5.0) cua Lop CNTT1
pass_cntt1 = df[(df['diem']>= 5.0) & (df['lop']=='CNTT1')]
print(pass_cntt1)