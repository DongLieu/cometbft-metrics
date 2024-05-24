def eachP2P():
    file_path = '/Users/donglieu/52024/injective/cometbft-metrics/treasure/blockP2P1.csv'

    return read_file(file_path)

def read_file(path):
    file = open(path, "r")

    data = file.read().split("\n")

    data = data[:-1]
    for x in range(len(data)):
        data[x] = data[x].split(",")
     
    return data

def heightTimeOut():
    eachHeigh = eachP2P()
    x_from = 0
    receive = 0
    for x in eachHeigh:
        if x[3] == "":
            x_from +=1
    
    receive = len(eachHeigh)-x_from
    print(x_from)
    print(receive)
            
        
# 1.520132042+0.002022702+2.937912053+0.088719586+0.637672203+0.05429426
heightTimeOut()