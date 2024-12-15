import sys

n = int(sys.stdin.readline())
i = 0
while True:
    if n == 1 or i > n:
        print(0)
        break

    i += 1
    i_str = str(i)

    sum = 0
    for j in range(len(i_str)):
        sum += int(i_str[j])

    m = i + sum

    if m == n:
        print(i)
        break