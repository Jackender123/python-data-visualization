import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Tạo dữ liệu doanh số
salesMen = ['Ahmed', 'Omar', 'Ali', 'Ziad', 'Salwa', 'Lila']
Mobile_Sales = [1200, 1500, 1100, 1800, 1600, 1300]
TV_Sales = [900, 1100, 1300, 1000, 1400, 1200]

df = pd.DataFrame({
    'Mobile_Sales': Mobile_Sales,
    'TV_Sales': TV_Sales
}, index=salesMen)

print(df)