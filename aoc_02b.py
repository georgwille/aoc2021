fin = open("input_02.txt")

p = 0
d = 0
aim = 0

for line in fin:
    command, number = line.strip().split()
    number = int(number)
    if command =="forward":
        p += number
        d += aim*number
    if command =="down":
        aim += number
    if command =="up":
        aim -= number

print(p, d, p*d)