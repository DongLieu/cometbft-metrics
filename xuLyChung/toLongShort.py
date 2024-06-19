from csv_reader import *
from blockTimeOuts import *

def Chia_DataLong_DataShort(dirPath, heighttimeouts, heightContinues):
    for i in read_file(dirPath + "/block.csv"):
        if i[0] in heightContinues:
            continue
        if i[0] in heighttimeouts:
            write_file(dirPath + "/longBlock/block.csv", i)
        else:
            write_file(dirPath + "/shortBlock/block.csv", i)
        
    for i in read_file(dirPath + "/blockOnlyTimeStep.csv"):
        if i[0] in heightContinues:
            continue
        if i[0] in heighttimeouts:
            write_file(dirPath + "/longBlock/blockOnlyTimeStep.csv", i)
        else:
            write_file(dirPath + "/shortBlock/blockOnlyTimeStep.csv", i)
        
    for i in read_file(dirPath + "/blockProposalStep.csv"):
        if i[0] in heightContinues:
            continue
        if i[0] in heighttimeouts:
            write_file(dirPath + "/longBlock/blockProposalStep.csv", i)
        else:
            write_file(dirPath + "/shortBlock/blockProposalStep.csv", i)

    for i in read_file(dirPath + "/blockVoteStep.csv"):
        if i[0] in heightContinues:
            continue
        if i[0] in heighttimeouts:
            write_file(dirPath + "/longBlock/blockVoteStep.csv", i)
        else:
            write_file(dirPath + "/shortBlock/blockVoteStep.csv", i)