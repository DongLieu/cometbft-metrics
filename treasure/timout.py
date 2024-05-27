from check_height import *
from csv_reader import *

heghtTimeout = heightTimeOut()

time = eachTimeStep()

vote = eachVote()

pro = eachProposal()

height = eachHeight()

for i in heghtTimeout:
    if time[0] == i[]: