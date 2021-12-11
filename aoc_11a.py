import numpy as np

fin = open("input_11.txt")

f = np.zeros((12,12),dtype='int32')

for i,line in enumerate(fin,1):
    f[i,1:11] = list(line.strip())

flashcounter = 0

for _ in range(100):
    f = f+1
    flashlist = np.argwhere(f > 9)
    while flashlist.shape[0] > 0:
        for x,y in flashlist:
            f[x-1:x+2,y-1:y+2] += 1 
            f[x,y] = -999
            flashcounter += 1
        flashlist = np.argwhere(f > 9)
    f[0,:] = f[11,:] = f[:,0] = f[:,11] = 0
    f[np.where(f<0)] = 0

print(flashcounter)
