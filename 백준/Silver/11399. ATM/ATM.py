import sys

sum = 0
n = int(sys.stdin.readline())
m = list(map(int,sys.stdin.readline().split()))
m.sort()

for i in range(n):
    sum += (n-i)*m[i]

print(sum)