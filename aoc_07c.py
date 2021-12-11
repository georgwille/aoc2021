with open("input_07.txt") as fin:
    a = fin.readline()

pos = [int(x) for x in a.split(',')]
pos.sort()
middle1 = pos[len(pos)//2]
middle2 = int(sum(pos)/len(pos))
# because dependency is quadratic
# the optimum might be +1, but not for my data

fuel1 = 0
fuel2 = 0

for x in pos:
    fuel1 += abs(middle1-x)
    d = abs(middle2-x)
    fuel2 += d * (d+1) //2

print(f'Part 1: {fuel1}')
print(f'Part 2: {fuel2}')