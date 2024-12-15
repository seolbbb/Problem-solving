import sys
t = int(sys.stdin.readline())

pd = [0 for _ in range(11)]

pd[1] = 1
pd[2] = 2
pd[3] = 4

for i in range(4,11):
    pd[i] = pd[i-3] + pd[i-2] + pd[i-1]

for i in range(t):
    n = int(sys.stdin.readline())
    print(pd[n])