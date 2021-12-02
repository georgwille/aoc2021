fin = open("input_02.txt")

p = 0
d = 0

for line in fin:
    command, number = line.strip().split()
    number = int(number)
    if command =="forward":
        p += number
    if command =="down":
        d += number
    if command =="up":
        d -= number

print(p, d, p*d)