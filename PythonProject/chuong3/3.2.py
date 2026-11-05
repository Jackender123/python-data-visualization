import pandas as pd
import numpy as np
#1.khoi tao dataframe tu dictionary cac list
gpa = pd.Series([3.5, 3.7, 3.9, 4.0], index=['Alice', 'Bob', 'Charlie', 'David'],name = 'GPA')
print(gpa)
#2. khoi tao dataframe tu dictionary cac list
data = {
    'Hoten':['Alice', 'Bob', 'Charlie', 'David'],
    'tuoi':[20, 21, 22, 23],
    'DiemLapTrinh':[8.5, 9.0, 7.5, 8.0]
}
df = pd.DataFrame(data)
print(df.info())