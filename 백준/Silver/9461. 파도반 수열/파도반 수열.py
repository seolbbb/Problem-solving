import sys

t = int(sys.stdin.readline())

pd = [0 for _ in range(101)]

pd[1] = 1
pd[2] = 1
pd[3] = 1
pd[4] = 2
pd[5] = 2
pd[6] = 3
pd[7] = 4
pd[8] = 5
pd[9] = 7
pd[10] = 9

for i in range(11,101):
    pd[i] = pd[i-1] + pd[i-5]

for i in range(t):
    print(pd[int(sys.stdin.readline())])