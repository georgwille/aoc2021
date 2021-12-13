fin = open('input_13.txt')

p = set()

fold = []

for line in fin:
    line = line.strip()
    if ',' in line:
        x,y = [int(a) for a in line.split(',')]
        p.add((x,y))
    elif '=' in line:
        line = line.split(' ')[2]
        axis,pos = line.split('=')
        fold.append((axis,int(pos)))

for i,(axis,pos) in enumerate(fold,1):
    temp = p.copy()
    for px,py in p:
        if axis == 'x' and px > pos:
                temp.add((pos-(px-pos),py))
                temp.discard((px,py))
        if axis == 'y' and py > pos:
                temp.add((px,pos-(py-pos)))
                temp.discard((px,py))
    p = temp
    print(i,':',len(p))

for y in range(10):
    for x in range(40):
        char = '#' if (x,y) in p else ' '
        print(char,end='')
    print()
