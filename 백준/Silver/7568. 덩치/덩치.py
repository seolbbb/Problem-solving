n = int(input())
lst = []
rank = [0 for _ in range(n)]

for _ in range(n):
    x, y = map(int,input().split())
    lst.append((x,y))

for i in range(n):
    cnt = 0
    x1, y1 = lst[i]
    for j in range(n):
        x2, y2 = lst[j]
        if x1 < x2 and y1 < y2:
            cnt += 1
    rank[i] = cnt + 1

print(' '.join(map(str,rank)))