import sys

n, m = map(int,sys.stdin.readline().split())
s = []
cnt = 0

for i in range(n):
    s.append(sys.stdin.readline().rstrip())

s = set(s)

for i in range(m):
    x = sys.stdin.readline().rstrip()
    if x in s:
        cnt += 1

print(cnt)