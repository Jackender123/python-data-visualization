import pandas as pd
# Tap du lieu khao sat 5 sinh vien
df_study = pd.DataFrame({'giohoc':[2,4,6,8,10],
                         'diemthi':[50,60,70,80,90],
                         'thoigiangame':[8,6,4,2,1]})
# 1. Tinh Hiep bien (Covariance)
print("ma tran hiep bien:\n", df_study.cov())
# 2. Tinh Tuong quan Pearson (Correlation)
corr_matrix = df_study.corr()
print("\nma tran tuong quan:\n", corr_matrix.round(3))