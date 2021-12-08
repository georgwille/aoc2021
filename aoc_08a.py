fin = open('input_08.txt')

counter1478 = 0

for line in fin:
    for entry in line.strip().split(' | ')[1].split(' '):
        if len(entry) in [2,4,3,7]:
            counter1478 += 1

print(counter1478)
