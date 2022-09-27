# MATRIX MULTIPLICATION two matrices using nested loops

# 2x2 matrix "X"
x = [
    [1, 2],
    [2, 3]
]

# 2x2 matrix "Y"
y = [
    [2, 3],
    [3, 4]
]

# result matrix
result = [[0, 0],
          [0, 0]]

# iterate through rows of "X"
for i in range(len(x)):
    # iterate through columns of Y
    for j in range(len(y[0])):
        # iterate through rows of Y
        for k in range(len(y)):
            result[i][j] += x[i][k] * y[k][j]


for end in result:
    print(end)