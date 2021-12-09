import numpy as np

fin = open("input_09.txt")

height = np.zeros((102, 102), dtype='int32')+9
offsets = [(1, 0), (0, 1), (-1, 0), (0, -1)]

for i, line in enumerate(fin):
    digits = list(line.strip())
    height[i+1, 1:101] = digits

total = 0
# there should be a better way than iterating
for x in range(1, 101):
    for y in range(1, 101):
        if all(height[x, y] < height[x+dx, y+dy] for dx, dy in offsets):
            total += height[x, y]+1

print(total)
