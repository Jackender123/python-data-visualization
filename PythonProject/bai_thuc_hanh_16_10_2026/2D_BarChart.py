import matplotlib.pyplot as plt
courses = ["Python",
            "Java",
            "Phân tích trục quan dữ liệu",
            "Phát triển web"]
students = [40,25,30,20]

plt.figure(figsize=(10,6))
plt.bar(courses,students,color = "cornflowerblue")

plt.title("Số lượng sinh viên đăng ký khóa học")
plt.xlabel("Khóa học")
plt.ylabel("Số lượng sinh viên")

plt.grid(axis="y",linestyle="--",alpha=0.7)

plt.show()