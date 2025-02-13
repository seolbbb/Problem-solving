import sys
from math import log2
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]
st = [[0 for _ in range(int(log2(n))+1)] for _ in range(n)]

for i in range(n):
    st[i][0] = arr[i]

for j in range(1, int(log2(n))+1):
    for i in range(n):
        if i + (1 << j) > n:
            continue
        st[i][j] = min(st[i][j-1], st[i + (1 << (j-1))][j-1])

for _ in range(m):
    s, e = map(int, input().split())
    length = e - s + 1
    k = int(log2(length))
    minimum = min(st[s-1][k], st[e - (1 << k)][k])

    print(minimum)