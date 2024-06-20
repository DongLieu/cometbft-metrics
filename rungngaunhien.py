import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
import matplotlib.pyplot as plt
import joblib

def read_file(path):
    file = open(path, "r")

    data = file.read().split("\n")

    data = data[:-1]
    for x in range(len(data)):
        data[x] = data[x].split(",")
     
     # data
    np.random.seed(0)
    X = np.random.rand(len(data), len(data[0]) -1 )  
    Y = np.random.rand(len(data), 1) * 10.1  

    for i in range(len(data)):
        if float(data[i][1]) <2 and float(data[i][0]) >4:
            continue
        Y[i] = float(data[i][0])
        for j in range(len(data[0]) - 1):
            X[i][j] = float(data[i][j+1])
        
    return X, Y

# data
#X: 
# 0:"numRound"
# 1:"numTx",
# 2:"blockSizeBytes", 
# 3:"blockParts",
# 4:"blockGossipPartsReceived", 
# 5:'quorumPrevoteDelay',
# 6:'fullPrevoteDelay',
# 7:'proposalReceiveCount',
# 8:'proposalCreateCount',
# 9:'TotalnumVoteReceived', 
# 10:'TotalnumVoteSent', 
# 11:'TotalmissingValidatorsPowerPrevote', 
# 12: "ToTalblockPartsReceived"
#Y: # 0:"blockIntervalSeconds"
X, Y = read_file("/Users/donglieu/62024/injective/cometbft-metrics/old_data/data12/cometbft-metrics/train/train3.csv")

# data split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=0)

# train module RandomForestRegressor đánh giá tầm quan trọng của đặc trưng
model = RandomForestRegressor()
model.fit(X_train, Y_train.ravel())
# ravel()
# Lấy tầm quan trọng của đặc trưng
feature_importances = model.feature_importances_

features =[ "numRound", "numTx", "blockSizeBytes", "blockParts", "blockGossipPartsReceived", 'quorumPrevoteDelay', 'fullPrevoteDelay', 'proposalReceiveCount', 'proposalCreateCount','TotalnumVoteReceived','TotalnumVoteSent','TotalmissingValidatorsPowerPrevote',"ToTalblockPartsReceived"]


importance_df = pd.DataFrame({'Feature': features, 'Importance': feature_importances})
importance_df = importance_df.sort_values(by='Importance', ascending=False)

# Lưu mô hình đã huấn luyện
joblib.dump(model, 'random_forest_model.joblib')

# Plot feature importances
plt.figure(figsize=(10, 6))
plt.barh(importance_df['Feature'], importance_df['Importance'])
plt.xlabel('Feature Importance')
plt.title('Feature Importances in RandomForestRegressor')
plt.gca().invert_yaxis()
plt.show()



# # Tải lại mô hình đã lưu
# loaded_model = joblib.load('random_forest_model.joblib')

# # Kiểm tra mô hình đã tải lại
# print(loaded_model.predict(X_test[:5]))  # Dự đoán với vài mẫu từ tập kiểm tra