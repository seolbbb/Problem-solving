import sys
from math import log2
input = sys.stdin.readline

MAX = 500000
k = int(log2(MAX)) + 1

m = int(input())
arr = [0] + list(map(int, input().split()))

st = [[0 for _ in range(m+1)] for _ in range(k)]

for i in range(1, m+1):
    st[0][i] = arr[i]

for i in range(1, k):
    for j in range(1, m+1):
        st[i][j] = st[i-1][st[i-1][j]]

q = int(input())

for _ in range(q):
    n, x = map(int, input().split())
    
    for i in range(k-1, -1, -1):
        if n & (1 << i):
            x = st[i][x]

    print(x)