p = [8,5]
s = [0,0]

def ddie():
    i = 1
    while True:
        yield i
        i += 1
        i = (i - 1) % 100 + 1

d = ddie()
throw = 0
end = False

while not end:
    for i in [0,1]:
        p[i] += next(d) + next(d) + next(d)
        throw += 3
        p[i] = (p[i] - 1) % 10 + 1
        s[i] += p[i]
        if s[i] >= 1000:
            print(s,throw, throw*min(s))
            end = True
            break
