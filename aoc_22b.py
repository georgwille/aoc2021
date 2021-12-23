with open("input_22.txt") as fin:
    seq = []
    for line in fin:
        state, rest = line.strip().split(" ")
        state = 1 if state == "on" else 0
        for c in ",.xyz=":
            rest = rest.replace(c, " ")
        xmin, xmax, ymin, ymax, zmin, zmax = [int(s) for s in rest.split()]
        seq.append((state, ((xmin, xmax), (ymin, ymax), (zmin, zmax))))


def intersect_edge(edge1, edge2):
    lo = max(edge1[0], edge2[0])
    hi = min(edge1[1], edge2[1])

    if lo > hi:
        return None
    else:
        return lo, hi


def intersect_cube(cube1, cube2):
    # return overlap cube from two given cubes
    # a cube is a triple of pairs
    # ((xmin,xmax),(ymin,ymax),(zmin,zmax))
    temp = []
    for i in range(3):
        int_edge = intersect_edge(cube1[i], cube2[i])
        if int_edge is None:
            return None
        temp.append(int_edge)
    return tuple(temp)


field = {}  # collecting all input cubes and overlap cubes with their "weight"

for state, curr_inputcube in seq:
    all_contrib = {}  # collects the weights that need to be annulled
    for cube in field:
        int_cube = intersect_cube(curr_inputcube, cube)
        if int_cube:
            if int_cube in all_contrib:
                all_contrib[int_cube] += field[cube]
            else:
                all_contrib[int_cube] = field[cube]

    for cube in all_contrib: # apply cumulative changes to field
        if cube in field:
            field[cube] -= all_contrib[cube]
        else:
            field[cube] = -all_contrib[cube]

    if state == 1: # finally, insert the current input cube if "on"
        if curr_inputcube in field:
            field[curr_inputcube] += 1
        else:
            field[curr_inputcube] = 1


def vol(cube):
    v = 1
    for i in range(3):
        edge = cube[i]
        v *= edge[1] - edge[0] + 1
    return v


total = sum(field[cube] * vol(cube) for cube in field)
print(total)
