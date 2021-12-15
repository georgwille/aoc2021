fin = open("input_14.txt")

template = fin.readline().strip()
fin.readline()

rules = {}
LETTERS = set()
for line in fin:
    pair,insert = line.strip().split(' -> ')
    rules[pair] = insert
    LETTERS.update(pair[0], pair[1], insert)

m = template

rounds = 10
for _ in range(rounds):
    mnew = ''
    for i,char in enumerate(m[:-1]):
        pair = char+m[i+1]
        mnew += char+rules[pair]
    m = mnew+m[-1]

counts = [m.count(letter) for letter in LETTERS if m.count(letter) > 0]

print(max(counts)-min(counts))
