import sys
input = sys.stdin.readline

isbn = list(input().rstrip())
total = 0

for idx, num in enumerate(isbn):
    if idx%2 == 0 and num.isnumeric():
        total += int(num)
    elif idx%2 == 1 and num.isnumeric():
        total += int(num)*3
    elif not num.isnumeric():
        if idx % 2 == 0:
            t = 1
        else:
            t = 3

for i in range(10):
    if (total + i*t) % 10 == 0:
        print(i)
        break