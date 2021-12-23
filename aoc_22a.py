import numpy as np

with open('input_22.txt') as fin:
    seq = []
    for line in fin:
        state,rest = line.strip().split(' ')
        state = 1 if state == 'on' else 0
        xr, yr, zr = rest.split(',')
        xmin,xmax = xr.split('..')
        ymin,ymax = yr.split('..')
        zmin,zmax = zr.split('..')
        seq.append((state,int(xmin[2:]),int(xmax),int(ymin[2:]),int(ymax),int(zmin[2:]),int(zmax)))

field = np.zeros((120,120,120))

for state,xmin,xmax,ymin,ymax,zmin,zmax in seq[:20]:
    field[xmin+50:xmax+51,ymin+50:ymax+51,zmin+50:zmax+51] = state

print(field.sum())