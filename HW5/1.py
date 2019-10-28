#HW Assignment 5
#2302 Python 2
#Professor Bowler
#3-31-19

#part1

import numpy as np

list = np.linspace(-1, 1, 200)

withoutbroadcasting = [(np.sin(i)) ** 2 + (np.cos(i)) ** 2 for i in list]

withbroadcasting = (np.sin(list)) ** 2 + (np.cos(list)) ** 2
print (withbroadcasting)