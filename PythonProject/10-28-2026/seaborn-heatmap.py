import seaborn as sns
import matplotlib.pyplot as plt

# Tải tập dữ liệu 'iris'
df = sns.load_dataset('iris')

# Chỉ tính tương quan giữa các cột số (loại bỏ cột 'species')
corr_matrix = df.drop(columns='species').corr()

# Thiết lập kích thước biểu đồ
plt.figure(figsize=(6, 4.5))

# Vẽ biểu đồ nhiệt (Heatmap)
sns.heatmap(
    corr_matrix,
    annot=True,
    cmap='Blues',
    fmt='.2f',
    linewidths=0.5
)

# Thêm tiêu đề và hiển thị
plt.title('Ma trận tương quan của bộ dữ liệu Iris')
plt.tight_layout()
plt.show()