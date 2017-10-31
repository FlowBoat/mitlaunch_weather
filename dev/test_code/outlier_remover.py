import numpy

data = []

with open("data.txt", "r") as f:
    for line in f.readlines():
        data.append(list(map(float, line.strip().split())))

def ofilter(matrix):
    transpose = list(zip(*matrix))
    stds = list(map(numpy.std, transpose))
    means = [sum(col) / len(col) for col in transpose]
    dels = []
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if abs(matrix[row][col] - means[col]) > 2 * stds[col]:
                dels.append(row)
    return [e for i, e in enumerate(matrix) if i not in dels]

print(data)
filtered = ofilter(data)
print(filtered)
print(len(filtered))
