import matplotlib.pyplot as plt
import pandas as pd

data = {'categories':['do dien tu','quan ao','do gia dung','do choi'],
        'quarter1_sales':[35000,45000,30000,20000],
        'quarter2_sales':[35000,45000,30000,20000]
        }
df = pd.DataFrame(data)
print(df)
plt.figure(figsize=(10,6))
bars1 = plt.bar(df['categories'],df['quarter1_sales'],label = 'quy 1',color ='skyblue')
bars2 = plt.bar(df['categories'],df['quarter2_sales'], label ='quy 2',color='orange',bottom=df['quarter1_sales'])

for bar1,bar2 in zip(bars1, bars2):
    height1 = bar1.get_height()
    height2 = bar2.get_height()
    plt.text(bar1.get_x()+bar1.get_width()/2,height1/2,height1,color='black',ha='center',va='center')
    plt.text(bar2.get_x()+bar2.get_width()/2,height1+height2/2,height1,color='black',ha='center',va='center')

plt.xlabel('Danh muc san pham')
plt.ylabel('danh so ban hang')
plt.title('bieu do doanh so ban hang thang theo danh muc san pham va quy')
plt.legend()
plt.show()
