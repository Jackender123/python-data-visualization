import seaborn as sns
import matplotlib.pyplot as plt
tips = sns.load_dataset('tips')
# so sanh hoa doon trung binh theo ngay va gioi tinh
sns.barplot(data=tips,
            x='day',
            y='total_bill',
            hue='sex',
            palette='Set2')
plt.title('hoa don trung binh theo ngay va gioi tinh')
plt.tight_layout()
plt.show()
#pairplot:bo dong lenh sau de xem ma tran tuong quan
#sns.pairplot(tips,hue='smoker',palette='husl')