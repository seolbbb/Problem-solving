import sys
input = sys.stdin.readline

k,n = map(int,input().split())
cable = [int(input()) for _ in range(k)]
left = 1
right = max(cable)

while right >= left:
    mid = (left+right) // 2
    temp = 0
    for c in cable:
        temp += c // mid
    
    if temp < n:
        right = mid -1
    else:
        left = mid + 1
    
print(right)