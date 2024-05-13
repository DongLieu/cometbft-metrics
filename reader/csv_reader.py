import csv

titleEachHeight = ['height', 'numRound', 'blockIntervalSeconds','numTx', 'blockSizeBytes', 'blockParts', 'blockGossipPartsReceived', 'quorumPrevoteDelay', 'fullPrevoteDelay', 'proposalReceiveCount', 'proposalCreateCount']
titleEachVote = ['height', 'roundID', 'step', 'validatorsPower', 'missingValidatorsPowerPrevote']
titleEachProposal = ['height', 'roundID', 'step', 'numblockParts', 'blockPartsReceived']
titleEachTime = ['height', 'roundID', 'stepName', 'stepTime']
titleEachP2P = ['height', 'roundID', 'step', 'fromPeer', 'toPeer', 'chID', 'msgType', 'size', 'rawByte']

def eachVote():
    file_path = '/Users/donglieu/52024/injective/cometbft-metrics/reader/blockVoteStep.csv'

    return read_file(file_path)

def eachHeight():
    file_path = '/Users/donglieu/52024/injective/cometbft-metrics/reader/block.csv'

    return read_file(file_path)

def eachProposal():
    file_path = '/Users/donglieu/52024/injective/cometbft-metrics/reader/blockProposalStep.csv'

    return read_file(file_path)

def eachTimeStep():
    file_path = '/Users/donglieu/52024/injective/cometbft-metrics/reader/blockOnlyTimeStep.csv'

    return read_file(file_path)

def eachP2P():
    file_path = '/Users/donglieu/52024/injective/cometbft-metrics/reader/blockP2P.csv'

    return read_file(file_path)

def read_file(path):
    file = open(path, "r")

    data = file.read().split("\n")

    data = data[:-1]
    for x in range(len(data)):
        data[x] = data[x].split(",")
     
    return data
