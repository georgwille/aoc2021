with open("input_07.txt") as fin:
    a = fin.readline()

pos = [int(x) for x in a.split(',')]
pos.sort()
middle = pos[len(pos)//2]

print(middle)

fuel = 0
for x in pos:
    fuel += abs(middle-x)

print(fuel)
