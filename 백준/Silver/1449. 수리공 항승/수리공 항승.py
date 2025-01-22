n, L = map(int,input().split())
spot = list(map(int,input().split()))
spot.sort()
left = 0
cnt = 0

for s in spot:
    if s > left:
        left = s + (L-1)
        cnt += 1

print(cnt)