import matplotlib.pyplot as plt
import squarify

labels = [
    "Đào tạo\n50 tỷ",
    "Nghiên cứu khoa học\n25 tỷ",
    "Cơ sở vật chất\n15 tỷ",
    "Công nghệ thông tin\n7 tỷ",
    "Khác\n3 tỷ"
]

sizes = [50, 25, 15, 7, 3]

# 2. Khai báo màu sắc
colors = ["skyblue", "lightgreen", "orange", "pink", "lightgray"]

# 3. Vẽ biểu đồ Treemap
plt.figure(figsize=(10, 6))
squarify.plot(
    sizes=sizes,
    label=labels,
    color=colors,
    alpha=0.8,
    text_kwargs={"fontsize": 10}
)

# 4. Đặt tiêu đề
plt.title("Phân bổ ngân sách của trường đại học")

# 5. Ẩn trục tọa độ
plt.axis("off")

# 6. Hiển thị biểu đồ
plt.show()
