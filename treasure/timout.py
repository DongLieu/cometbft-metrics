from check_height import *
from csv_reader import *

heghtTimeout = heightTimeOutFromPath("/Users/donglieu/52024/injective/cometbft-metrics/old_data/data7/block.csv")

time = read_file("/Users/donglieu/52024/injective/cometbft-metrics/old_data/data7" + "/blockOnlyTimeStep.csv")

vote = read_file("/Users/donglieu/52024/injective/cometbft-metrics/old_data/data7" + "/blockVoteStep.csv")

pros = read_file("/Users/donglieu/52024/injective/cometbft-metrics/old_data/data7" + "/blockProposalStep.csv")

heig = read_file("/Users/donglieu/52024/injective/cometbft-metrics/old_data/data7" + "/block.csv")

def writeCSVTIME():
    for i in time:
        if i[0] in heightTimeOut:
            # write
            write_file("/Users/donglieu/52024/injective/cometbft-metrics/treasure/newblocktimeout-305/time.csv", i)

def writeCSVVOTE():
    for i in vote:
        if i[0] in heightTimeOut:
            # write
            write_file("/Users/donglieu/52024/injective/cometbft-metrics/treasure/newblocktimeout-305/vote.csv", i)

def writeCSVpro():
    for i in pros:
        if i[0] in heightTimeOut:
            # write
            write_file("/Users/donglieu/52024/injective/cometbft-metrics/treasure/newblocktimeout-305/pro.csv", i)


def writeCSVheight():
    for i in heig:
        if i[0] in heightTimeOut:
            # write
            write_file("/Users/donglieu/52024/injective/cometbft-metrics/treasure/newblocktimeout-305/block.csv", i)

