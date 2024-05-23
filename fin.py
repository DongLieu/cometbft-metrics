def eachHeight():
    file_path = '/Users/donglieu/52024/injective/cometbft-metrics/treasure/block.csv'

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
    # data = [70917290, 1, 0.408425436, 4, 9948, 2048, 5, 0.05217152, 0.269370465, 1, 0]
    # for data in datas:
    with open(path_file, 'a', newline='') as csvfile:
        # Tạo writer object
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(data)


def heightTimeOut():
    eachHeigh = eachHeight()
    eachVotes = eachTime()
    for x in eachHeigh:
        sum = 0
        for y in eachVotes:
            if x[0] == y[0]:
                sum += float(y[3])
        
        if x[0]=="70936284":
            print(sum)
            print(x)
            print(x[3])
            print(abs(float(x[2]) ))
            print(abs(float(x[2]) - sum))


        if abs(float(x[2]) - sum) > 0.1:
            write_file("/Users/donglieu/52024/injective/cometbft-metrics/ttt.csv", x)
        else:
            write_file("/Users/donglieu/52024/injective/cometbft-metrics/ppp.csv", x)
            

        
# 0.295311491+0.005125644+0.346825766+0.068239132+0.057279223
# 0.151666704+0.149336283+0.531047416+0.050715277+0.055331848

heightTimeOut()