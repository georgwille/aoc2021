# MUCH room for optimization

import numpy as np
from scipy.spatial.transform import Rotation as R

with open('input_19.txt') as fin:
    signals = {} # raw coordinates
    for line in fin:
        if line == '\n':
            continue
        elif line.startswith('--'):
            p_n = int(line[12:14])
            signals[p_n] = []
        else:
            x,y,z = [int(x) for x in line.strip().split(',')]
            signals[p_n].append((x,y,z))

def get_diffs(coords):
    '''
    calculate complete set of difference measures from
    given list of 3D coordinates

    returns set of differences and a dict with the points
    that are involved in each difference
    '''
    diffs = set()
    points = {}
    for i, b1 in enumerate(coords):
        for b2 in coords[i+1:]:
            euc, rec, pro = 0, 0, 1
            for c in range(3):
                dist = b1[c]-b2[c]
                euc += dist**2
                rec += abs(dist)
                pro *= abs(dist)
            diffs.add((euc,rec,pro))
            points[(euc,rec,pro)] = (b1,b2)
    return diffs, points

def center(coords):
    '''
    Calculate center of gravity for given list of points
    '''
    x = y = z = 0
    for entry in coords:
        x += entry[0]
        y += entry[1]
        z += entry[2]
    l = len(coords)
    return x/l, y/l, z/l
    
def eudist2(coords1, coords2):
    "squared euclidian distance between two points"
    return sum((coords1[i]-coords2[i])**2 for i in range(3))

def sort_by_remoteness(coords):
    "sort list of points by distance from center of gravity"
    xc, yc, zc = center(coords)
    t = [(eudist2((xc,yc,zc),point),point) for point in coords]
    t.sort()
    return [el[1] for el in t]

themap = signals[0]
themap_diffs, themap_points = get_diffs(themap)

todo = list(range(1,len(signals)))
scanner_pos = [(0,0,0)]

all_diffs = [0]*len(signals)
all_points = [0]*len(signals)

for i,entry in signals.items():
    all_diffs[i], all_points[i] = get_diffs(entry)

while todo:
    curr_i = todo.pop()
    curr = signals[curr_i]
    curr_diffs, curr_points = all_diffs[curr_i], all_points[curr_i]
    intersection = curr_diffs & themap_diffs
    if len(intersection) < 66:
        if todo == []:
            break
        todo.insert(0,curr_i)
        continue
    themap_i_points = set()
    curr_i_points = set()
    for el in intersection:
        for k in (0,1):
            themap_i_points.add(themap_points[el][k])
            curr_i_points.add(curr_points[el][k])
    themap_i_points = np.asarray(sort_by_remoteness(themap_i_points))
    center_themap_i = np.asarray(center(themap_i_points))
    curr_i_points = np.asarray(sort_by_remoteness(curr_i_points))
    center_curr_i = np.asarray(center(curr_i_points))
    r,_ = R.align_vectors(themap_i_points-center_themap_i, curr_i_points-center_curr_i)
    curr_transform = r.apply(np.asarray(curr)-center_curr_i)+center_themap_i
    scanner_pos.append(tuple(np.round(r.apply(np.asarray((0,0,0))-center_curr_i)+center_themap_i)))
    for x,y,z in curr_transform:
        themap.append((int(round(x)),int(round(y)),int(round(z))))
    themap = list(set(themap))
    themap_diffs, themap_points = get_diffs(themap)

print("Part 1:", len(themap))
