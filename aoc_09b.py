import numpy as np

fin = open("input_09.txt")

height = np.zeros((102, 102), dtype='int32') + 9
b = height * 0  # basin map

offsets = [(1, 0), (0, 1), (-1, 0), (0, -1)]

for i, line in enumerate(fin):
    digits = list(line.strip())
    height[i+1, 1:101] = digits

mcounter = 1
sob = [0]  # size of basins
# there should be a better way than iterating
for x in range(1, 101):
    for y in range(1, 101):
        islowest = all(height[x, y] < height[x+dx, y+dy] for dx, dy in offsets)
        if islowest:
            b[x, y] = mcounter
            sob.append(1)
            mcounter += 1

map_changed = True

while map_changed:
    map_changed = False
    for x in range(1, 101):
        for y in range(1, 101):
            if b[x, y] > 0:
                for dx, dy in offsets:
                    nx = x+dx
                    ny = y+dy
                    if b[nx, ny] == 0 and 9 > height[nx, ny] > height[x, y]:
                        b[nx, ny] = b[x, y]
                        sob[b[x, y]] += 1
                        map_changed = True

sob.sort()
print(sob[-1]*sob[-2]*sob[-3])
