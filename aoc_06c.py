from collections import deque

with open('input_06.txt') as fin:
    a = fin.readline()

# fishlist = [int(entry) for entry in a.split(',')]
fishcount = deque([0]*9) # count clustered by age

for i in range(9):
    fishcount[i] = a.count(str(i))

days1 = 80
days2 = 256

def evolve(days):
    global fishcount
    for _ in range(days):
        fishcount.rotate(-1)
        fishcount[6] += fishcount[-1]

evolve(days1)
print(f'Day {days1}: {sum(fishcount)}')

evolve(days2-days1)
print(f'Day {days2}: {sum(fishcount)}')
