with open('input_16.txt') as fin:
    transmission = fin.readline().strip()

# transmission = 'D2FE28'
# transmission = '38006F45291200'

d = int(transmission, base=16)
b = str(bin(d))[2:]
b = '0'*((4-len(b)%4)%4)+b

def parse(pckt, count=-1):
    if pckt == "" or int(pckt) == 0:
        return 0

    if count == 0:
        return parse(pckt)

    ver = int(pckt[:3], base=2)
    typ = int(pckt[3:6], base=2)

    if typ == 4:
        num_str = ""
        i = 6
        while True:
            chunk = pckt[i:i+5]
            num_str += chunk[1:]
            i += 5
            if chunk[0] == "0":
                break
        val = int(num_str, base=2)
        return ver + parse(pckt[i:], count-1)

    len_ID = pckt[6]
    if len_ID == "0": # 15 bits, length of subpackets
        n_bits = int(pckt[7:22], base=2)
        return ver + parse(pckt[22:22+n_bits], -1) + parse(pckt[22+n_bits:], count-1)
    else: # 11 bits, number of packets
        n_packs = int(pckt[7:18], base=2)
        return ver + parse(pckt[18:], count=n_packs)

print(parse(b))
