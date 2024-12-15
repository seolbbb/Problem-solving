import sys
import math

def rounded(n):
    if n - math.trunc(n) >= 0.5:
        return math.ceil(n)
    else:
        return math.floor(n)

n = int(input())
lst = []

for i in range(n):
    lst.append(int(sys.stdin.readline()))

if n == 0:
    print(0)
else:
    lst.sort()
    x = rounded((n * 0.15))
    num = n - 2*x
    if x != 0:
        print(rounded(sum(lst[x:-x])/num))
    else:
        print(rounded(sum(lst)/num))