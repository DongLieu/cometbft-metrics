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
    times = read_file(dirPath + "/"+longShort+"/blockOnlyTimeStep.csv")

    os.makedirs(os.path.dirname(dirPath + "/train/train.csv"), exist_ok=True)
    with open(dirPath + "/train/train.csv", 'a', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        for i in heights:
            tmp = []
            # 0,            1,      2,                  3,              4,                          5,                  6,                      7,                      8
            # "numRound", "numTx", "blockSizeBytes", "blockParts", "blockGossipPartsReceived", 'quorumPrevoteDelay', 'fullPrevoteDelay', 'proposalReceiveCount', 'proposalCreateCount'
            tmp.append(round(float(i[3]), 3))

            # numroungd
            roundnum = 1 
            m = seachData(0, len(times)-1, i[0] ,times)
            if m == -1: continue
            if m < 10: m =10
            for j in times[m-10:m+10]:
                if j[0] == i[0]:
                    roundnum = 1+int(j[2])

            tmp.append(float(roundnum))
            # tmp.append(float(i[2]))
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
            m = seachData(0, len(votes)-1, i[0] ,votes)
            if m == -1: continue
            if m < 10: m = 10
            for j in votes[m-10:m+10]:
                if j[0] == i[0]:
                    vote4 += float(j[4])
                    vote5 += float(j[5])
                    vote6 += float(j[6])

            tmp.append(vote4)
            tmp.append(vote5)
            tmp.append(vote6)

            # PRO :6 "ToTalblockPartsReceived"
            pro6 = 0
            m = seachData(0, len(pros)-1, i[0] ,pros)
            if m == -1: continue
            if m < 10: m = 10
            for j in pros[m-10:m+10]:
                if j[0] == i[0]:
                    pro6 += float(j[6])
            if i[0] == "73679932": print(pro6)
            tmp.append(pro6)
            csvwriter.writerow(tmp)
            # write_file(dirPath + "/train/train.csv", tmp)

def seachData(start, end, h, datas):
    if start + 1 == end: 
        # print(h)
        return -1
    # if h == "73679968":
    #     print(start)
    # print(h)
    if datas[start][0] == h:
        return start
    if datas[end][0] == h:
        return end
    mid = int((start+end)/2)
    if datas[mid][0] == h:
        return mid
    if float(datas[mid][0]) > float(h):
        return seachData(start, mid, h, datas)

    return seachData(mid, end, h, datas)
