import numpy as np

with open("input_20.txt") as fin:
    a = fin.read()

algotemp, imtemp = a.split("\n\n")
algo = np.zeros(512, dtype="int32")
for i, char in enumerate(algotemp):
    algo[i] = 1 if char == "#" else 0

lines = imtemp.strip().split("\n")
center = np.zeros((len(lines), len(lines[0])), dtype="int32")
for i, line in enumerate(imtemp.split("\n")):
    for j, char in enumerate(line):
        center[i, j] = 1 if char == "#" else 0

key = np.asarray([2 ** (8 - i) for i in range(9)]).reshape((3, 3))
border = 0

canvas = np.pad(center, ((1, 1), (1, 1)), mode="constant", constant_values=border)

for count in range(2):
    canvas = np.pad(canvas, ((3, 3), (3, 3)), mode="constant", constant_values=border)
    newcanvas = np.zeros((canvas.shape[0], canvas.shape[1]), dtype="int32")
    for i in range(1, canvas.shape[0] - 1):
        for j in range(1, canvas.shape[1] - 1):
            index = canvas[i - 1 : i + 2, j - 1 : j + 2] * key
            newcanvas[i, j] = algo[index.sum()]
    canvas = newcanvas[1:-1, 1:-1]
    if algo[0]:
        border = 1 - border

print(canvas.sum())
