import sys
from collections import defaultdict

n = int(sys.stdin.readline())
s = list(map(int,sys.stdin.readline().split()))

right = 0
left = 0
cnt = defaultdict(int)
k = 0

for i in range(n):
    cnt[s[right]] += 1
    right += 1

    while len(cnt) > 2:
        cnt[s[left]] -= 1
        if cnt[s[left]] == 0:
            del cnt[s[left]]
        left += 1

    if k <= right - left:
        k = right - left

print(k)