def eachHeight():
    file_path = '/Users/donglieu/52024/injective/cometbft-metrics/old_data/data3/cometbft-metrics/block.csv'

    return read_file(file_path)

def read_file(path):
    file = open(path, "r")

    data = file.read().split("\n")

    data = data[:-1]
    for x in range(len(data)):
        data[x] = data[x].split(",")
     
    return data

def heightTimeOut():
    eachHeigh = eachHeight()
    height_timeout = []
    max = 0
    for x in eachHeigh:
        if float(x[2]) > max:
            max = float(x[2])

        if float(x[2]) > timeThreshold:
            height_timeout.append(x[0])

    print(max)
    return height_timeout

timeThreshold = 5.0



print(heightTimeOut())