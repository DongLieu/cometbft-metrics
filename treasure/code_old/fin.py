def eachHeight():
    file_path = '/Users/donglieu/52024/injective/cometbft-metrics/treasure/valid/block.csv'

    return read_file(file_path)

def eachTime():
    file_path = '/Users/donglieu/52024/injective/cometbft-metrics/treasure/blockOnlyTimeStep.csv'

    return read_file(file_path)

def eachPro():
    file_path = '/Users/donglieu/52024/injective/cometbft-metrics/treasure/blockProposalStep.csv'

    return read_file(file_path)

def eachVote():
    file_path = '/Users/donglieu/52024/injective/cometbft-metrics/treasure/blockVoteStep.csv'

    return read_file(file_path)


def read_file(path):
    file = open(path, "r")

    data = file.read().split("\n")

    data = data[:-1]
    for x in range(len(data)):
        data[x] = data[x].split(",")
     
    return data

import csv

def write_file(path_file, data):
    with open(path_file, 'a', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(data)


def heightTimeOut():
    eachHeigh = eachHeight()
    eachVotes = eachPro()
    for x in eachHeigh:
        for y in eachVotes:
            if x[0] == y[0]:
                write_file("/Users/donglieu/52024/injective/cometbft-metrics/treasure/valid/blockProposalStep1.csv", y)
            


heightTimeOut()