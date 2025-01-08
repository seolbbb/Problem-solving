import sys
input = sys.stdin.readline

n,m = map(int,input().split())
pre_sum = [[] for _ in range(n)]

for i in range(n):
    lst = list(map(int,input().split()))
    temp = 0
    for j in range(n):
        temp += lst[j]
        pre_sum[i].append(temp)

for i in range(1,n):
    for j in range(n):
        pre_sum[i][j] += pre_sum[i-1][j]

for i in range(m):
    x1,y1,x2,y2 = map(int,input().split())

    if x1 != 1 and y1 != 1:
        result = pre_sum[x2-1][y2-1] - pre_sum[x2-1][y1-2] - pre_sum[x1-2][y2-1] + pre_sum[x1-2][y1-2]
    elif x1 == 1 and y1 != 1:
        result = pre_sum[x2-1][y2-1] - pre_sum[x2-1][y1-2]
    elif x1 != 1 and y1 == 1:
        result = pre_sum[x2-1][y2-1] - pre_sum[x1-2][y2-1]
    else:
        result = pre_sum[x2-1][y2-1]

    print(result)