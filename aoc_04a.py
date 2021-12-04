import numpy as np

with open('input_04.txt') as fin:
    firstline = fin.readline()
    numbers = [int(a) for a in firstline.strip().split(',')]

    boards = np.zeros((1,5,5),dtype='int16')-1
    bindex = -1

    for line in fin:
        line = line.strip()
        if not line:
            bindex += 1
            x = 0
            boards = np.append(boards,np.zeros((1,5,5),dtype='int16')-1,axis=0)
            continue
        num = line.split()
        for y in range(5):
            boards[bindex,x,y] = int(num[y])
        x += 1

marked = boards*0

for number in numbers:
    marked = marked | (boards == number)
    colsum = marked.sum(axis=1)
    rowsum = marked.sum(axis=2)
    if np.any(colsum == 5) or np.any(rowsum == 5):
        winb = np.argwhere(np.logical_or(colsum==5,rowsum==5))[0,0]
        score = boards[winb,:,:]*(1-marked[winb,:,:])*number
        print(f"Board {winb}, Number {number}, Score {score.sum()}")
        break
