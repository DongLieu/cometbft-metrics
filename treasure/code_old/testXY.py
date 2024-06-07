import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
import matplotlib.pyplot as plt

# data
np.random.seed(0)
X = np.random.rand(10000, 12)  # 10000 mẫu có 12 đặc trưng
Y = np.random.rand(10000, 1) * 10  # 10000 giá trị nhãn Y

# Chia data
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=0)

# Huấn luyện mô hình RandomForestRegressor để đánh giá tầm quan trọng của đặc trưng
model = RandomForestRegressor()
model.fit(X_train, Y_train.ravel())

# Lấy tầm quan trọng của đặc trưng
feature_importances = model.feature_importances_

# Hiển thị tầm quan trọng của đặc trưng
features = [f'X[{i}]' for i in range(X.shape[1])]
importance_df = pd.DataFrame({'Feature': features, 'Importance': feature_importances})
importance_df = importance_df.sort_values(by='Importance', ascending=False)

# Plot feature importances
plt.figure(figsize=(10, 6))
plt.barh(importance_df['Feature'], importance_df['Importance'])
plt.xlabel('Feature Importance')
plt.title('Feature Importances in RandomForestRegressor')
plt.gca().invert_yaxis()
plt.show()

print(importance_df)
