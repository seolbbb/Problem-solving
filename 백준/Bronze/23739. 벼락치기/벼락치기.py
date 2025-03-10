n = int(input())
time = 30
ans = 0

for _ in range(n):
    t = int(input())

    if time >= t:
        ans += 1
        time -= t
    else:
        if time >= (t / 2):
            ans += 1
        time = 0

    if time == 0:
        time = 30

print(ans)