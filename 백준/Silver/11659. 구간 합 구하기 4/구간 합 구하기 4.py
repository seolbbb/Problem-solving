import sys
input = sys.stdin.readline

n,m = map(int,input().split())
n_lst = list(map(int,input().split()))

pre = []
x = 0
for i in range(n):
    x += n_lst[i]
    pre.append(x)

for _ in range(m):
    i,j = map(int,input().split())
    if i == 1:
        print(pre[j-1])
    else:
        print(pre[j-1] - pre[i-2])