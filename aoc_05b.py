import numpy as np

fin = open("input_05.txt")

field = np.zeros((1000, 1000), dtype="int16")

for line in fin:
    x1,y1,x2,y2 = [int(n) for n in line.replace(" -> ",",").split(",")]

    if x2 < x1: # swap start to up&left
        x1, x2 = x2, x1
        y1, y2 = y2, y1

    if y2 < y1:
        x1, x2 = x2, x1
        y1, y2 = y2, y1

    if x1 == x2:
        field[x1, y1 : y2 + 1] += 1
    elif y1 == y2:
        field[x1 : x2 + 1, y1] += 1
    else:
        for c in range(y2 + 1 - y1):
            if x1 < x2: # main diagonal
                field[x1 + c, y1 + c] += 1
            else: # cross diagonal
                field[x1 - c, y1 + c] += 1

print(np.argwhere(field > 1).shape[0])
