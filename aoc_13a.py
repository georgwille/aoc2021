import numpy as np

fin = open('input_13.txt')

p = np.zeros((900,1400),dtype='int32')

fold = []

for line in fin:
    line = line.strip()
    if ',' in line:
        x,y = [int(a) for a in line.split(',')]
        p[y,x] = 1
    elif '=' in line:
        line = line.split(' ')[2]
        axis,pos = line.split('=')
        fold.append((axis,int(pos)))

for axis,pos in fold:
    points = np.argwhere(p > 0)
    for py,px in points:
        if axis == 'x' and px > pos:
                p[py,pos-(px-pos)] = 1
                p[py,px] = 0
        if axis == 'y' and py > pos:
                p[pos-(py-pos),px] = 1
                p[py,px] = 0
    print(len(np.argwhere(p>0)))
    break
