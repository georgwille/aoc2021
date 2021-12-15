with open("input_14.txt") as fin:
    template = fin.readline().strip()
    fin.readline()

    rules = {}
    LETTERS = set()
    for line in fin:
        pair, insert = line.strip().split(' -> ')
        rules[pair] = insert
        LETTERS.update(pair[0], pair[1], insert)

empty = {}
for a in LETTERS:
    for b in LETTERS:
        empty[a+b] = 0

count = empty.copy()
for i, char in enumerate(template[:-1]):
    count[char+template[i+1]] += 1

rounds = 40
for _ in range(rounds):
    newcount = empty.copy()
    for a in LETTERS:
        for b in LETTERS:
            pair = a+b
            r = rules[pair]
            newcount[a+r] += count[pair]
            newcount[r+b] += count[pair]
    count = newcount.copy()

charsum = {}
for key, i in count.items():
    if key[0] in charsum:
        charsum[key[0]] += i
    else:
        charsum[key[0]] = i

charsum[template[-1]] += 1

l = [e for e in list(charsum.values()) if e > 0]
print(max(l)-min(l))
