fin = open("input_08.txt")

digits = []
output = []

easy = {2:1,3:7,4:4,7:8} # the "easy" solutions
k = [0, 0, 1, 2, 3, 6, 5, 4, 0, 0]  # sorting key
easycount = 0
outputsum = 0

for line in fin:
    line = line.strip()
    digits = line.split(" | ")[0].split(" ")
    output = line.split(" | ")[1].split(" ")
    sol = [set()] * 10 # digit->letters solution for this line 
    digits.sort(key=lambda x: k[len(x)])
    for entry in digits:
        s = set(entry)
        l = len(entry)
        if l in easy:
            sol[easy[l]] = s
        elif l == 6:
            if len(sol[4].intersection(s)) == 4:
                sol[9] = s
            elif len(sol[1].intersection(s)) == 2:
                sol[0] = s
            else:
                sol[6] = s
        else: # l == 5
            if len(s.intersection(sol[4])) == 2:
                sol[2] = s
            elif len(s.intersection(sol[1])) == 2:
                sol[3] = s
            else:
                sol[5] = s

    for weight, entry in zip([1000, 100, 10, 1], output):
        if len(entry) in easy:
            easycount += 1
        outputsum += weight * int(sol.index(set(entry)))

print(easycount)
print(outputsum)
