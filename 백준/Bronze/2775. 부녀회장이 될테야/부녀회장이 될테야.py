import sys

t = int(input())

x = [i+1 for i in range(14)]
temp = []
y = []
y.append(x)


for i in range(14):
    s = 0
    for j in range(14):
        temp.append(y[i][j] + s)
        s += y[i][j]
    y.append(temp)
    temp = []

for i in range(t):
    a = int(input())
    b = int(input())

    print(y[a][b-1])