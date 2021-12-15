with open('input_15.txt') as fin:
    m = {}
    for x,line in enumerate(fin):
        for y,char in enumerate(line.strip()):
            m[(x,y)] = int(char)

xmax = x
ymax = y

start = (0,0)
target = (xmax,ymax)

# here comes a cheap implementation of A*

openlist = {start:[0, None]} #   (x,y): [cost to here, parent]
closedlist = {} #                (x,y): [cost to here, parent]

while openlist:
    bestscore = 10**8
    for k,v in openlist.items():
        if v[0]-k[0]-k[1] < bestscore:
            current = k
            bestscore = v[0]-k[0]-k[1]

    closedlist[current] = openlist.pop(current)

    if current == target:
        print(closedlist[current][0]+m[(xmax,ymax)]-m[(0,0)])
        # path = set()
        # while current:
        #     path.add(current)
        #     current = closedlist[current][1]
        # for x in range(xmax+1):
        #     for y in range(ymax+1):
        #         if (x,y) in path:
        #             print('#',end='')
        #         else:
        #             print(' ',end='')
        #     print()
        break

    for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
        xn = current[0]+dx
        yn = current[1]+dy
        if not (0<=xn<=xmax and 0<=yn<=ymax):
            continue
        if (xn,yn) in closedlist:
            continue
        thiscost = closedlist[current][0]+m[current]
        if (xn,yn) in openlist and thiscost >= openlist[(xn,yn)][0]:
            continue
        openlist[(xn,yn)] = [thiscost, current]
