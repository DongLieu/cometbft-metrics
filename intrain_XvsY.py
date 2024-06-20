import numpy as np
# data
# 0:"blockIntervalSeconds"
# 1:"numRound"
# 2:"numTx",
# 3:"blockSizeBytes", 
# 4:"blockParts",
# 5:"blockGossipPartsReceived", 
# 6:'quorumPrevoteDelay',
# 7:'fullPrevoteDelay',
# 8:'proposalReceiveCount',
# 9:'proposalCreateCount',
# 10:'TotalnumVoteReceived', 
# 11:'TotalnumVoteSent', 
# 12:'TotalmissingValidatorsPowerPrevote', 
# 13: "ToTalblockPartsReceived"

def read_file(path):
    path = path + "/cometbft-metrics/train/train.csv"
    file = open(path, "r")

    data = file.read().split("\n")

    data = data[:-1]
    for x in range(len(data)):
        data[x] = data[x].split(",")
     
     # data
    np.random.seed(0)
    X = np.random.rand(len(data), 1 )  
    Y = np.random.rand(len(data), 1) * 10.1  

    for i in range(len(data)):
        Y[i] = float(data[i][0])
        X[i] = float(data[i][1])
        
    return X, Y


X,Y = read_file("/Users/donglieu/62024/injective/cometbft-metrics/old_data/data12")

import matplotlib.pyplot as plt
# Vẽ biểu đồ scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(X, Y, c='blue', marker='o')
plt.title('cac diem bieu dien')
plt.xlabel('TotalnumVoteReceived')
plt.ylabel('blockTime')
plt.grid(True)
plt.show()