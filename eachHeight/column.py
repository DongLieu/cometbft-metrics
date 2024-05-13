import sys

sys.path.insert(1, '/Users/donglieu/52024/injective/cometbft-metrics/reader/')

from csv_reader import *

eachHeight = eachHeight()

print(eachHeight[-1])