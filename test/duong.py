import matplotlib.pyplot as plt

# Dữ liệu mẫu
time = ['T1', 'T2', 'T3', 'T4', 'T5']
data = {
    'Đối tượng 1': [10, 12, 14, 13, 15],
    'Đối tượng 2': [15, 17, 16, 18, 20],
    'Đối tượng 3': [20, 19, 21, 22, 24],
    'Đối tượng 4': [18, 20, 19, 21, 23],
    'Đối tượng 5': [22, 24, 23, 25, 27],
    'Đối tượng 6': [25, 27, 26, 28, 30],
    'Đối tượng 7': [30, 32, 33, 34, 35]
}

# Tạo biểu đồ
plt.figure(figsize=(10, 6))
for key, values in data.items():
    plt.plot(time, values, marker='o', label=key)

# Tùy chỉnh biểu đồ
plt.title('Biểu đồ đường cho 7 đối tượng')
plt.xlabel('Thời gian')
plt.ylabel('Giá trị')
plt.legend()
plt.grid(True)

# Hiển thị biểu đồ
plt.show()
