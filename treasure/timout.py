from check_height import *
from csv_reader import *

heghtTimeouts = heightsTimeOut("/Users/donglieu/52024/injective/cometbft-metrics/old_data/data7/cometbft-metrics")

time = read_file("/Users/donglieu/52024/injective/cometbft-metrics/old_data/data7/cometbft-metrics" + "/blockOnlyTimeStep.csv")

vote = read_file("/Users/donglieu/52024/injective/cometbft-metrics/old_data/data7/cometbft-metrics" + "/blockVoteStep.csv")

pros = read_file("/Users/donglieu/52024/injective/cometbft-metrics/old_data/data7/cometbft-metrics" + "/blockProposalStep.csv")

heig = read_file("/Users/donglieu/52024/injective/cometbft-metrics/old_data/data7/cometbft-metrics" + "/block.csv")

def writeCSVTIME():
    for i in time:
        if i[0] in heghtTimeouts:
            # write
            write_file("/Users/donglieu/52024/injective/cometbft-metrics/treasure/newblocktimeout-305-timestep/time.csv", i)

def writeCSVVOTE():
    for i in vote:
        if i[0] in heghtTimeouts:
            # write
            write_file("/Users/donglieu/52024/injective/cometbft-metrics/treasure/newblocktimeout-305-timestep/vote.csv", i)

def writeCSVpro():
    for i in pros:
        if i[0] in heghtTimeouts:
            # write
            write_file("/Users/donglieu/52024/injective/cometbft-metrics/treasure/newblocktimeout-305-timestep/pro.csv", i)


def writeCSVheight():
    for i in heig:
        if i[0] in heghtTimeouts:
            # write
            write_file("/Users/donglieu/52024/injective/cometbft-metrics/treasure/newblocktimeout-305-timestep/block.csv", i)

writeCSVTIME()
writeCSVVOTE()
writeCSVpro()
writeCSVheight()