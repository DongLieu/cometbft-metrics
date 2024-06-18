# data
#Y: 0:"blockIntervalSeconds"
#X: 1:"numRound",
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

from csv_reader import *

def Chia_DataTrain(dirPath):
    layData(dirPath, "shortBlock")
    layData(dirPath, "longBlock")

def layData(dirPath, longShort):
    votes = read_file(dirPath + "/"+longShort+"/blockVoteStep.csv")
    pros = read_file(dirPath + "/"+longShort+"/blockProposalStep.csv")
    heights = read_file(dirPath + "/"+longShort+"/block.csv")

    for i in heights:
        tmp = []
        # 0,            1,      2,                  3,              4,                          5,                  6,                      7,                      8
        # "numRound", "numTx", "blockSizeBytes", "blockParts", "blockGossipPartsReceived", 'quorumPrevoteDelay', 'fullPrevoteDelay', 'proposalReceiveCount', 'proposalCreateCount'
        tmp.append(float(i[3]))
        tmp.append(float(i[2]))
        tmp.append(float(i[4]))
        tmp.append(float(i[5]))

        tmp.append(float(i[6]))
        tmp.append(float(i[7]))
        tmp.append(float(i[8]))

        tmp.append(float(i[9]))
        tmp.append(float(i[10]))
        tmp.append(float(i[11]))
                        # 9
        # 4,5,6 VOTE 'TotalnumVoteReceived','TotalnumVoteSent','TotalmissingValidatorsPowerPrevote',
        vote4 =0
        vote5 =0
        vote6 =0
        flag = 0
        for j in votes:
            if j[0] == i[0]:
                vote4 += float(j[4])
                vote5 += float(j[5])
                vote6 += float(j[6])
                flag = 1
            if flag == 1 and j[0] != i[0]:break

        tmp.append(vote4)
        tmp.append(vote5)
        tmp.append(vote6)

        # PRO :6 "ToTalblockPartsReceived"
        pro6 = 0
        flag2 = 0
        for j in pros:
            if j[0] == i[0]:
                pro6 += float(j[6])
                flag2 = 1
            if flag2 == 1 and j[0] != i[0]:break
            
        
        tmp.append(pro6)
        write_file(dirPath + "/train/train.csv", tmp)