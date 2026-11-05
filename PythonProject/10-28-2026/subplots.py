import matplotlib.pyplot as plt
import seaborn as sns

# 1. Khởi tạo lưới 1x2 bằng subplots (Object-Oriented API)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

# 2. Ô 1: Line plot (Bảng màu liên tục Viridis)
ax1.plot(months, sales, marker='o', color=plt.cm.viridis(0.6))
ax1.set_title('A. Xu huong Doanh so')
ax1.grid(True, linestyle='--', alpha=0.5)

# 3. Ô 2: Bar plot (Bảng màu danh mục Set2 - Quy tắc Y=0)
colors = sns.color_palette('Set2', len(categories))
ax2.bar(categories, cat_values, color=colors)
ax2.set_ylim(bottom=0)  # Đảm bảo trục Y bắt đầu từ 0
ax2.set_title('B. Doanh so theo Danh muc')

# 4. Căn chỉnh lề và Xuất tệp ảnh 300 DPI
plt.tight_layout()
plt.savefig('sales_summary_300dpi.png', dpi=300, bbox_inches='tight')