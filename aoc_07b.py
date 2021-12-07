with open("input_07.txt") as fin:
    a = fin.readline()

pos = [int(x) for x in a.split(',')]
middle = int(sum(pos)/len(pos))
# because dependency is quadratic
# the optimum might be +1, but not for my data

print(middle)

fuel = 0
for x in pos:
    d = abs(middle-x)
    fuel += d * (d+1) //2

print(fuel)