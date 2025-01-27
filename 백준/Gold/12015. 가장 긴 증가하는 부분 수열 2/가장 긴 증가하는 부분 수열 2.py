import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
lis = [0]

for num in arr:
    if num > lis[-1]:
        lis.append(num)
    else:
        idx = 0
        bl = 0
        br = len(lis)-1

        while bl <= br:
            middle = (bl+br)//2
            if lis[middle] >= num:
                br = middle-1
            else:
                bl = middle+1
        lis[bl] = num

print(len(lis)-1)