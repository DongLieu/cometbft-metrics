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

def write_file(path_file, data):
    with open(path_file, 'a', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(data)

