import numpy as np

n = np.loadtxt('input_01.txt')

def increasecount(field, k):
    d = field[k:] - field[:-k]
    count = np.argwhere(d > 0)
    return count.shape[0]


print(increasecount(n, 3))
