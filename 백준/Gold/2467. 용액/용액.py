import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int,input().split()))
res = [float('inf'),0,0]

left = 0
right = n-1

while left < right:
    cur = lst[left] + lst[right]
    if abs(cur) < res[0]:
        res[0] = abs(cur)
        res[1] = lst[left]
        res[2] = lst[right]
    if cur < 0:
        left += 1
    elif cur > 0:
        right -= 1
    else:
        print(lst[left], lst[right])
        exit(0)

print(res[1],res[2])