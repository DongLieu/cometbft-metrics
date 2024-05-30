def eachHeight():
    file_path = '/Users/donglieu/52024/injective/cometbft-metrics/old_data/data7/block.csv'
    # file_path = "/Users/donglieu/52024/injective/cometbft-metrics/old_data/data5/block.csv"
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
        if x[0] == "0":continue
        if x[-1] == "0" and x[-2] == "0" and x[-3] == "0" and x[-4] == "0":continue
        if float(x[3]) > max:
            max = float(x[3])

        # if float(x[2]) > 3 and float(x[2]) < 5:
        if float(x[3]) > 5:
            height_timeout.append(x[0])
    print(max)
    return height_timeout
# 1.520132042+0.002022702+2.937912053+0.088719586+0.637672203+0.05429426

print(heightTimeOut())