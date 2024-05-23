def eachHeight():
    file_path = '/Users/donglieu/52024/injective/cometbft-metrics/treasure/block.csv'

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
        # print(x)
        if float(x[2]) > max:
            max = float(x[2])

        if float(x[2]) > 3 and float(x[2]) < 5:
            height_timeout.append(x[0])
    print(max)
    return height_timeout


print(heightTimeOut())