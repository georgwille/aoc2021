from collections import defaultdict

WAYS = defaultdict(list)

with open('input_12.txt') as fin:
    for line in fin:
        x,y = line.strip().split('-')
        WAYS[x].append(y)
        WAYS[y].append(x)

def paths_to_end(history):
    paths = 0
    for target in WAYS[history[-1]]:
        if target == 'end':
            paths += 1
        elif target.isupper() or target not in history:
            history.append(target)
            paths += paths_to_end(history)
            history.pop()
        elif not history[0] and target.islower() and target != 'start':
            history[0] = True # visited some cave twice
            history.append(target)
            paths += paths_to_end(history)
            history.pop()
            history[0] = False
    return paths

print(paths_to_end([False,'start']))
