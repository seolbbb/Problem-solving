import sys
from collections import defaultdict
input = sys.stdin.readline

m,n = map(int,input().split())
universe = []
cnt = 0

for _ in range(m):
    lst = list(map(int,input().split()))
    dic = {}
    for i,planet in enumerate(sorted(lst)):
        if planet in dic:
            continue
        else:
            dic[planet] = i
    for i in range(n):
        lst[i] = dic[lst[i]]

    universe.append(tuple(lst))

freq = defaultdict(int)
for planet in universe:
    freq[planet] += 1

for count in freq.values():
    if count >= 2:
        cnt += (count * (count-1)) // 2

print(cnt)