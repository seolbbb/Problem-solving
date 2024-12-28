import sys
input = sys.stdin.readline

n = int(input())
max_lst = [[0,0,0],[0,0,0]]
min_lst = [[0,0,0],[0,0,0]]
cur = []

for i in range(n):
    if i == 0:
        max_lst[1] = list(map(int,input().split()))
        min_lst[1] = max_lst[1][:]
    else:
        max_lst[0] = max_lst[1][:]
        min_lst[0] = min_lst[1][:]

        cur = list(map(int,input().split()))

        max_lst[1][0] = max(max_lst[0][0] + cur[0], max_lst[0][1] + cur[0])
        max_lst[1][1] = max(max_lst[0][0] + cur[1], max_lst[0][1] + cur[1], max_lst[0][2] + cur[1])
        max_lst[1][2] = max(max_lst[0][1] + cur[2], max_lst[0][2] + cur[2])

        min_lst[1][0] = min(min_lst[0][0] + cur[0], min_lst[0][1] + cur[0])
        min_lst[1][1] = min(min_lst[0][0] + cur[1], min_lst[0][1] + cur[1], min_lst[0][2] + cur[1])
        min_lst[1][2] = min(min_lst[0][1] + cur[2], min_lst[0][2] + cur[2])

print(max(max_lst[1]), min(min_lst[1]))