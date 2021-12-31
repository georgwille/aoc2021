import numpy as np

# occurence(player,day,position,score)
occ = np.zeros((2, 15, 11, 31),dtype='int64')

# score: # of ways to get that score
dthrow = {3: 1, 4: 3, 5: 6, 6: 7, 7: 6, 8: 3, 9: 1}

# real: 8,5; test: 4,8
occ[0, 0, 8, 0] = 1
occ[1, 0, 5, 0] = 1

p0wins = 0
p1wins = 0

for r in range(1, 15):
    for p in (0, 1):
        for pos in range(1, 11):
            for score in range(30):
                if occ[p, r - 1, pos, score] == 0:
                    continue
                for eyes, prob in dthrow.items():
                    pos_n = (pos + eyes - 1) % 10 + 1
                    score_n = score + pos_n
                    occ[p, r, pos_n, score_n] += occ[p, r - 1, pos, score] * prob

    p0wins += occ[0, r, :, 21:].sum() * occ[1, r - 1, :, :21].sum()
    p1wins += occ[1, r, :, 21:].sum() * occ[0, r, :, :21].sum()
    occ[0, r, :, 21:] = 0
    occ[1, r, :, 21:] = 0
    if occ[:,r,:,:].sum() == 0:
        break

print(max(p0wins, p1wins))
