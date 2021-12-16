import heapq

with open('input_15.txt') as fin:
    m = {}
    for x,line in enumerate(fin):
        size = len(line.strip())
        for y,char in enumerate(line.strip()):
            d = int(char)
            for x_off in range(5):
                for y_off in range(5):
                    d_new = (d-1+x_off+y_off) % 9 + 1
                    m[x+size*x_off, y+size*y_off] = d_new

xmax = size*5-1
ymax = size*5-1

start = (0,0)
target = (xmax,ymax)

# here comes a cheap implementation of A*

openlist = {start:[0, None]} #   (x,y): [cost to here, parent]
closedlist = {} #                (x,y): [cost to here, parent]
olheap = []
heapq.heappush(olheap, [0,start])

while openlist:
    while True:
        current = heapq.heappop(olheap)[1]
        if current in openlist:
            break

    closedlist[current] = openlist.pop(current)

    if current == target:
        print(closedlist[current][0]+m[(xmax,ymax)]-m[(0,0)])
        # for path printing see 15a
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
        heapq.heappush(olheap,[thiscost-xn-yn,(xn,yn)])
