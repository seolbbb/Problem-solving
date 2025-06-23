import sys
input = sys.stdin.readline

n = int(input())
s = set()

for _ in range(n):
    s.add(input().rstrip())

lst = list(s)

lst.sort(key=lambda x:(len(x), x))

print(*lst, sep='\n')