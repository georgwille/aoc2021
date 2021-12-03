with open("input_03.txt") as fin:
    lines = fin.readlines()

l = []

for line in lines:
    l.append(int(line.strip(), base=2))


def most_common(l, p, mode):
    l1 = []
    l0 = []
    for el in l:
        if el & (2 ** (11 - p)):
            l1.append(el)
        else:
            l0.append(el)
    if mode ^ (len(l1) < len(l0)):
        return l1
    else:
        return l0


def lfilter(l, mode):
    ltest = l.copy()
    for p in range(12):
        ltest = most_common(ltest, p, mode)
        if len(ltest) == 1:
            print(p, ltest)
            return ltest[0]


print(lfilter(l, 1)*lfilter(l, 0))
