import sys
n = int(input())
x = []

for i in range(n):
    x.append(list(map(int,sys.stdin.readline().split())))

x.sort(key=lambda x: (x[0], x[1]))

for i in range(n):
    print(x[i][0], x[i][1])