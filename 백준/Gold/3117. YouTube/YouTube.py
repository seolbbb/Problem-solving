import sys
from math import log2
input = sys.stdin.readline

n, k, m = map(int, input().split())
L = int(log2(m)) + 1
st = [[0 for _ in range(k+1)] for _ in range(L)]

student = list(map(int, input().split()))
st[0] = [0] + list(map(int, input().split()))

for i in range(1, L):
    for j in range(1, k+1):
        st[i][j] = st[i-1][st[i-1][j]]

ans = []

for start in student:
    start = st[0][start]
    for i in range(L-1, -1, -1):
        if (m-2) & (1 << i):
            start = st[i][start]
    ans.append(start)

print(*ans)