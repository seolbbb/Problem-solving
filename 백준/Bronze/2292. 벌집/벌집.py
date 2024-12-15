x = int(input())
n = 2
cnt = 1
i = 0
while True:
    i += 1
    if x >= n:
        cnt += 1
        n += (i * 6)
    else:
        break

print(cnt)