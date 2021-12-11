import numpy as np

with open('input_04.txt') as fin:
    firstline = fin.readline()
    numbers = [int(a) for a in firstline.strip().split(',')]

    boards = np.zeros((1,5,5),dtype='int32')-1
    bindex = -1

    for line in fin:
        line = line.strip()
        if not line:
            bindex += 1
            x = 0
            boards = np.append(boards,np.zeros((1,5,5),dtype='int32')-1,axis=0)
            continue
        num = line.split()
        for y in range(5):
            boards[bindex,x,y] = int(num[y])
        x += 1

marked = boards*0
bns = []

for number in numbers:
    marked = marked | (boards == number)
    colsum = marked.sum(axis=1)
    rowsum = marked.sum(axis=2)
    if np.any(colsum == 5) or np.any(rowsum == 5):
        winners = np.argwhere(np.logical_or(colsum==5,rowsum==5))[:,0]
        winners = np.unique(winners)
        for winb in winners:
            score = boards[winb,:,:]*(1-marked[winb,:,:])*number
            bns.append((winb,number,score.sum()))
            marked[winb,:,:] = -999

print(f"First: Board {bns[0][0]}, Number {bns[0][1]}, Score {bns[0][2]}")
print(f"Last:  Board {bns[-1][0]}, Number {bns[-1][1]}, Score {bns[-1][2]}")
