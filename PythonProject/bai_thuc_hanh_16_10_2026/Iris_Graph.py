import pandas as pd# su dung de xu ly du lieu bang
import matplotlib.pyplot as plt# su dung de ve bieu do
import seaborn as sns# su dung de ve bieu do(thong ke dep va nang cao)
import sklearn.datasets import load_iris# su dung de hoc may
#to chuc du lieu bang pandas va su dung matplotlib,seaborn de ve bieu do
#Histogram: độ dài cánh hoa phân bố như nào như 
#boxplot: chiều dài đài hoa khác nhau ra giữa các loài 
#pie chảt: tỷ lệ số mẫu cua từng loài là bao nhiêu?
#tải dữ liệu iris
#hàm load_iris( trả về một đối tượng chứa dữ liệu và thông tin mô tả< trong đó:
#iris.data: Ma trận dữ liệu kích thước 150x4.
#iris.feature_names: tên của 4 thuộc tính.
#iris.target:nhân số của loại hoa: 0-setosa 1-versicolor 2-virginica
iris = load_iris()
df = pd.DataFrame(iris.data, columns= iris.feature_names)
print(df.head())# hiển thị 5 dòng đàu tiên
print(df.shape)
print(df.info)

df['specices'] = pd.Categorical.from_codes(iris.target, iris.target_names)
print(df['specices'].value_counts())
#histogram
plt.hist(df['petal Length(cm)'],bins = 20, color='skyblue', edgecolor = 'black')
plt.title('Histogram - Petal Length')
plt.xlabel('Petal Length(cm)')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()
#Boxplot
sns.boxplot(x = 'species', y ='sepal length(cm)',data = df)
plt.title('boxplot - Sepal legth by Species')
plt.show()
#Pie Chart
species_counts = df['species'].value_counts()
plt.pie(species_counts, labels = species_counts.index, autopct= '%1,1%', startangle=0)
plt.title('distribution of iris species')
plt.axis('equal')
plt.show()