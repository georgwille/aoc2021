# target area: x=81..129, y=-150..-108

xt_max = 129
xt_min = 81
yt_min = -150
yt_max = -108
hitcount = 0
# dumb brute force is not terribly slow
for ix in range(int(xt_min**0.5),xt_max+1):
    for iy in range(yt_min,-yt_min):
        x = y = 0
        dx = ix
        dy = iy
        hit = False
        while not hit:
            x += dx
            y += dy
            if xt_min <= x <= xt_max and yt_min <= y <= yt_max:
                hit = True
                hitcount += 1
                break
            if x > xt_max or y < yt_min:
                break
            dy -= 1
            if dx > 0:
                dx -= 1
            
print(hitcount)
