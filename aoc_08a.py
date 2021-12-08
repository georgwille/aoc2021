fin = open('input_08.txt')

output = []

for line in fin:
    line = line.strip()
    output.append(line.split(' | ')[1].split(' '))

counter1478 = 0

for line in output:
    for entry in line:
        if len(entry) in [2,4,3,7]:
            counter1478 += 1

print(counter1478)

