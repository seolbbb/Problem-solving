n = int(input())
k = int(input())

low = 1
high = n**2

while low <= high:
    middle = (low + high) // 2
    cnt = 0

    for i in range(1, n+1):
        cnt += min(middle//i, n)

    if cnt >= k:
        high = middle - 1

    else:
        low = middle + 1

print(low)