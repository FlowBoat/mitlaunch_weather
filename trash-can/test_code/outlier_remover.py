import numpy
import json
import prettyprint

with open("test_configs.json", "r") as f:
    settings = json.loads(f.read())

data = []

def get(name, default = None):
    sub = settings
    for part in name.strip().split("."):
        part = part.strip()
        if part in sub:
            sub = sub[part]
        else:
            break
    else:
        return sub
    return default

in_file = get("io.filename", "data.txt")
deviations = get("algo.deviations", 2)
maxcycles = get("algo.maxcycles", -1)

with open(in_file, "r") as f:
    for line in f.readlines():
        data.append(list(map(float, line.strip().split())))

def ofilter(matrix):
    transpose = list(zip(*matrix))
    stds = list(map(numpy.std, transpose))
    means = [sum(col) / len(col) for col in transpose]
    dels = []
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if abs(matrix[row][col] - means[col]) > deviations * stds[col]:
                dels.append(row)
    return [e for i, e in enumerate(matrix) if i not in dels]

old = []
cycles = 0
while cycles < maxcycles and old != data:
    old = data
    data = ofilter(data)
    cycles += 1
# print(data)
print(prettyprint.plot([row[0] for row in data], 0.1))
# print(len(data))
# print(cycles)
