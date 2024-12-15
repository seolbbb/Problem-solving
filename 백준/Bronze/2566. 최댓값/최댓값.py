col = 0
row = 0
max = 0

X = []

for i in range(9):
    X.append(list(map(int,input().split())))

for i in range(9):
    for j in range(9):
        num = X[i][j]
        if num >= max:
            max = num
            col = i + 1
            row = j + 1

print(max)
print(col, row)