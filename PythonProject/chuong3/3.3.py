import pandas as pd

sales_q1 = pd.Series([100,150,200], index=['hanoi','cantho','tphcm'])
sales_q2 = pd.Series([120,160,210], index=['cantho','tphcm','danang'])

#1. cong truc tiep(xuat hien NaN hanoi va danang)
total_direct = sales_q1 + sales_q2
#2. cong voi fill_value=0 (khong xuat hien NaN)
total_clean = sales_q1.add(sales_q2, fill_value=0)
print(total_clean)