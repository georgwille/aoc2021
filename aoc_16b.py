with open('input_16.txt') as fin:
    transmission = fin.readline().strip()

# transmission = 'D2FE28'
# transmission = '38006F45291200'

d = int(transmission, base=16)
b = str(bin(d))[2:]
b = '0'*((4-len(b)%4)%4)+b

def calc(typ, values): # could be inlined
    if typ == 0:
        return sum(values)
    elif typ == 1:
        p = values[0]
        for v in values[1:]:
            p *= v
        return p
    elif typ == 2:
        return min(values)
    elif typ == 3:
        return max(values)
    elif typ == 5:
        return int(values[0] > values[1])
    elif typ == 6:
        return int(values[0] < values[1])
    elif typ == 7:
        return int(values[0] == values[1])
    else:
        raise AssertionError("Unknown Type")

def parse(startpos, endpos=-1): # start at i, end at j
    # returns value of this packet and start of next
    if startpos == endpos:
        return None, None

    if startpos > len(b) - 4:
        return None, None

    typ = int(b[startpos+3:startpos+6], base=2)

    if typ == 4:
        num_str = ""
        startpos += 6
        while True:
            chunk = b[startpos:startpos+5]
            num_str += chunk[1:]
            startpos += 5
            if chunk[0] == "0":
                break
        val = int(num_str, base=2)
        return val, startpos

    sub_packs = []
    next_start = None

    lenID = b[startpos+6]
    if lenID == "0": # 15 bits, length of subpackets
        n_bits = int(b[startpos+7:startpos+22], base=2)
        end = startpos + 22 + n_bits
        index = startpos + 22
        prev_index = None
        while index:
            prev_index = index
            x, index = parse(index, endpos=end)
            sub_packs.append(x)
        sub_packs = sub_packs[:-1]  # Remove last None
        next_start = prev_index

    else: # 11 bits, number of subpackets
        n_pcks = int(b[startpos+7:startpos+18], base=2)
        index = startpos + 18
        while n_pcks > 0:
            x, index = parse(index)
            n_pcks -= 1
            sub_packs.append(x)
        next_start = index

    value = calc(typ, sub_packs)
    return value, next_start

print(parse(0)[0])
