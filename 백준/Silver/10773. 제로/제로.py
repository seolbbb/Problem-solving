import sys

k = int(sys.stdin.readline())
lst = []

for i in range(k):
    x = int(sys.stdin.readline())

    if x > 0:
        lst.append(x)
    else:
        lst.pop()

print(sum(lst))