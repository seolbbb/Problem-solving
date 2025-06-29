import sys
input = sys.stdin.readline

n, m = map(int, input().split())
num = list(map(int, input().split()))
pre = [0 for _ in range(n+1)]

for idx, i in enumerate(num):
    pre[idx+1] = pre[idx] + i

for _ in range(m):
    s, e = map(int, input().split())
    print(pre[e] - pre[s-1])