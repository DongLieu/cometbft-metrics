from check_height import *
from csv_reader import *

heghtTimeout = heightTimeOut()

time = eachTimeStep()

vote = eachVote()

pro = eachProposal()

height = eachHeight()

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
    for i in pro:
        if i[0] in heightTimeOut:
            # write
            write_file("/Users/donglieu/52024/injective/cometbft-metrics/treasure/newblocktimeout-305/pro.csv", i)


def writeCSVheight():
    for i in height:
        if i[0] in heightTimeOut:
            # write
            write_file("/Users/donglieu/52024/injective/cometbft-metrics/treasure/newblocktimeout-305/block.csv", i)

