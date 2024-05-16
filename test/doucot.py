import matplotlib.pyplot as plt
import numpy as np

# Danh sách các môn học
subjects = ['Toán', 'Văn', 'Anh', 'Hóa', 'Lý']

# Giả sử bạn có 2 list với nội dung giống nhau
scores1 = [8.5, 7.0, 9.0, 6.5, 8.0]
scores2 = [8.5, 7.0, 9.0, 6.5, 8.0]

# Số lượng môn học
num_subjects = len(subjects)

# Tạo các vị trí cho các cột
indices = np.arange(num_subjects)

# Độ rộng của mỗi cột
width = 0.35

# Tạo biểu đồ
fig, ax = plt.subplots()

# Vẽ cột đầu tiên với màu xanh lá cây
rects1 = ax.bar(indices - width/2, scores1, width, label='List 1', color='green')

# Vẽ cột thứ hai với màu đỏ
rects2 = ax.bar(indices + width/2, scores2, width, label='List 2', color='red')

# Thêm các nhãn, tiêu đề và chú giải
ax.set_xlabel('Môn học')
ax.set_ylabel('Điểm số')
ax.set_title('Biểu đồ điểm số cho hai danh sách')
ax.set_xticks(indices)
ax.set_xticklabels(subjects)
ax.legend()

# Hiển thị số điểm trên mỗi cột
ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)

# Hiển thị biểu đồ
plt.show()
