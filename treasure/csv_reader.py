import csv

titleEachHeight = ['height','islongblock', 'numRound', 'blockIntervalSeconds','numTx', 'blockSizeBytes', 'blockParts', 'blockGossipPartsReceived', 'quorumPrevoteDelay', 'fullPrevoteDelay', 'proposalReceiveCount', 'proposalCreateCount']
titleEachVote = ['height','islongblock', 'roundID', 'step', 'numVoteReceived','numVoteSent','missingValidatorsPowerPrevote','validatorsPower']
titleEachProposal = ['height','islongblock', 'roundID', 'blockSize','numTxs','blockPartsSend', 'blockPartsReceived', 'numblockParts']
titleEachTime = ['height','islongblock', 'roundID', 'stepName', 'stepTime']
titleEachP2P = ['height','islongblock', 'roundID', 'step', 'fromPeer', 'toPeer', 'chID', 'msgType', 'size', 'rawByte', 'content']
titleVoteSet = ['height','islongblock', 'roundID', 'type', 'blockID', "time", "valAddress", "indexVal", 'signatureByte']
timeThreshold = 5.0

def eachVote():
    file_path = '/Users/donglieu/52024/injective/cometbft-metrics/treasure/gen/blockVoteStep.csv'

    return read_file(file_path)

def eachHeight():
    file_path = '/Users/donglieu/52024/injective/cometbft-metrics/treasure/gen/block.csv'

    return read_file(file_path)

def eachProposal():
    file_path = '/Users/donglieu/52024/injective/cometbft-metrics/treasure/gen/blockProposalStep.csv'

    return read_file(file_path)

def eachTimeStep():
    file_path = '/Users/donglieu/52024/injective/cometbft-metrics/treasure/gen/blockOnlyTimeStep.csv'

    return read_file(file_path)

def eachP2P():
    file_path = '/Users/donglieu/52024/injective/cometbft-metrics/treasure/gen/blockP2P.csv'

    return read_file(file_path)

def read_file(path):
    file = open(path, "r")

    data = file.read().split("\n")

    data = data[:-1]
    for x in range(len(data)):
        data[x] = data[x].split(",")
     
    return data

def heightTimeOut():
    eachHeigh = eachHeight()
    height_timeout = []
    max = 0
    for x in eachHeigh:
        if float(x[3]) > max:
            max = float(x[3])

        if float(x[3]) > timeThreshold:
            height_timeout.append(x[0])

    # print(max)
    return height_timeout


def write_file(path_file, data):
    with open(path_file, 'a', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(data)


# def heightTimeOutFromPath(file_path):
#     eachHeigh = read_file(file_path)
#     height_timeout = []
#     max = 0
#     for x in eachHeigh:
#         # print(x)
#         if x[0] == "0":continue
#         if x[-1] == "0" and x[-2] == "0" and x[-3] == "0" and x[-4] == "0":continue
#         if float(x[3]) > max:
#             max = float(x[3])

#         # if float(x[2]) > 3 and float(x[2]) < 5:
#         if float(x[3]) > 5:
#             height_timeout.append(x[0])
#     print(max)
#     return height_timeout