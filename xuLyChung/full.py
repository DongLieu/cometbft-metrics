from blockTimeOuts import *
from toLongShort import *
from toTrain import *

dirPath = "/Users/donglieu/62024/injective/cometbft-metrics/old_data/data11/cometbft-metrics"


maxTime, heightimeouts, hightContinue, dists_Times = heightsTimeOut(dirPath)
# print(timeout)
print("TimeMax:", maxTime)
print("num:", len(heightimeouts))

# chia long short
Chia_DataLong_DataShort(dirPath, heightimeouts, hightContinue)

# chia datatrain
Chia_DataTrain(dirPath)