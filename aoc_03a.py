fin = open("input_03.txt")

linecount = 0
count = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0,
         6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0}

for line in fin:
    linecount += 1
    n = line.strip()
    for i, letter in enumerate(n):
        if letter == "1":
            count[i] += 1
result = 0

for i in count:
    result = 2*result+(count[i] >= linecount//2)

print(result*(2**12-1-result))
