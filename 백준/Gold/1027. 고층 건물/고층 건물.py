import sys
input = sys.stdin.readline

n = int(input())
heights = list(map(int, input().split()))
view = [0 for _ in range(n)]

for i in range(n):
    for j in range(i+1, n):
        # y = ax + b 에서 a, b 구하기
        a = (heights[j]-heights[i]) / (j-i)
        b = heights[j] - a*j
        blocked = False

        for k in range(i+1, j):
            if heights[k] >= a*k + b:
                blocked = True
                break
        
        if blocked == False:
            view[i] += 1
            view[j] += 1

print(max(view))