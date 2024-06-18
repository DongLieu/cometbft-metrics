import csv
import os

titleEachHeight = ['height','islongblock', 'numRound', 'blockIntervalSeconds','numTx', 'blockSizeBytes', 'blockParts', 'blockGossipPartsReceived', 'quorumPrevoteDelay', 'fullPrevoteDelay', 'proposalReceiveCount', 'proposalCreateCount']
titleEachVote = ['height','islongblock', 'roundID', 'step', 'numVoteReceived','numVoteSent','missingValidatorsPowerPrevote','validatorsPower']
titleEachProposal = ['height','islongblock', 'roundID', 'blockSize','numTxs','blockPartsSend', 'blockPartsReceived', 'numblockParts']
titleEachTime = ['height','islongblock', 'roundID', 'stepName', 'stepTime']
titleEachP2P = ['height', 'roundID', 'step', 'fromPeer', 'toPeer', 'chID', 'msgType', 'size', 'info']
titleVoteSet = ['height','islongblock', 'roundID', 'type', 'blockID', "time", "valAddress", "indexVal", 'signatureByte']
timeThreshold = 5.0

def read_file(path):
    file = open(path, "r")

    data = file.read().split("\n")

    data = data[:-1]
    for x in range(len(data)):
        data[x] = data[x].split(",")
     
    return data

def write_file(path_file, data):
    os.makedirs(os.path.dirname(path_file), exist_ok=True)
    with open(path_file, 'a', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(data)