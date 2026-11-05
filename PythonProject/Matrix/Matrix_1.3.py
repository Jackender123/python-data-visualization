import numpy as np
np.random.seed(42)  # For reproducibility
temps = np.random.uniform(low=20.0, high=30.0, size=(5, 5))
print("nhiet do 30 ngay :\n", temps)

#1. boolean indexing
hot_days_mask = temps > 30.0
print("nhung ngay nong hon 30 do C:\n", hot_days_mask)
print("cac gia tri nong hon 30 do C:\n", temps[hot_days_mask])
print("so ngay nong hon 30 do C:\n", np.sum(hot_days_mask))
#2 loc dieu kien ket hop voi bitwise: nhiet do tu 20 den 30 do C
moderate_temps = temps[(temps >= 20.0) & (temps <= 30.0)]
print("nhung ngay co nhiet do tu 20 den 30 do C:\n", moderate_temps)
#3 su dung np.where
cold_days = np.where(temps < 20.0)
print("nhung ngay lanh hon 20 do C:\n", temps[cold_days])
hot_days = np.where(temps > 30.0)
print("nhung ngay nong hon 30 do C:\n", temps[hot_days])