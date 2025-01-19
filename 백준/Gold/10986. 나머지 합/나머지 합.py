import sys
input = sys.stdin.readline

n, m = map(int,input().split())
lst = list(map(int,input().split()))

prefix_mod = 0
mod_cnt = [0 for _ in range(m)]
cnt = 0

for i in range(n):
    prefix_mod = (prefix_mod + lst[i]) % m
    if prefix_mod == 0:
        cnt += 1
    mod_cnt[prefix_mod] += 1

for freq in mod_cnt:
    if freq > 1:
        cnt += (freq * (freq-1)) // 2

print(cnt)