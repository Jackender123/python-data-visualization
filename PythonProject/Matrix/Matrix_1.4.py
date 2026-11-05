import numpy as np
#score broad 5 x 3
X = np.array([[8.0, 7.5, 9.0], [5.0, 6.0, 4.5], [9.5, 8.5, 10.0], [6.5, 7.0, 6.0], [7.0, 8.0, 7.5]])
#tinh diem trung binh cua moi hoc sinh (cot) -> shape (3,)
mean_per_subject = np.mean(X, axis=0)
print("Diem trung binh cua moi mon hoc:\n", mean_per_subject)
#2. Mean Centering bang broadcasting: (5, 3) - (3,) = (5, 3)
#mang mean_per_subject = np.mean(X, axis=0) co shape (3,) nen khi thuc hien phep tru voi X co shape (5, 3) se tu dong broadcast mean_per_subject sang shape (5, 3)
X_centered = X - mean_per_subject
print("Ma tran sau khi mean centering:\n", X_centered.round(2))
#3. chuan hoa Min_Mã Scaling về đoạn (0, 1] cho tung mon hoc
min_val = np.min(X, axis=0)
max_val = np.max(X, axis=0)
X_normalized = (X - min_val) / (max_val - min_val) if np.any(max_val - min_val) else np.zeros_like(X)
X_scaled = (X - min_val) / (max_val - min_val)
print("Ma tran sau khi chuan hoa Min-Max Scaling:\n", X_scaled.round(2))