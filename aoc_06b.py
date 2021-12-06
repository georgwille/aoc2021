with open('input_06.txt') as fin:
    a = fin.readline()

fishlist = [int(entry) for entry in a.split(',')]
fishcount = [0]*9 # count clustered by age

for i in range(9):
    fishcount[i] = fishlist.count(i)

newcount = [0]*9
days = 256

for day in range(1,days+1):
    newcount[:8] = fishcount[1:] # shift
    newcount[8] = fishcount[0] # spawn
    newcount[6] += fishcount[0] 
    fishcount = newcount.copy()

print(day, fishcount,sum(fishcount))