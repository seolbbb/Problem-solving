import sys

n,k = map(int,sys.stdin.readline().split())
dic = {}
cnt = 0
for i in range(1,7):
    for j in range(2):
        dic[(j,i)] = 0

for i in range(n):
    s, y = map(int,sys.stdin.readline().split())
    dic[(s,y)] += 1

for i in range(1,7):
    for j in range(2):
        if dic[(j,i)] == 0:
            continue
        if 1 <= dic[(j,i)] <= k:
            cnt += 1
        else:
            if k == 1:
                cnt += dic[(j,i)]
            else:
                cnt += (dic[(j,i)] + k - 1) // k
            
print(cnt)