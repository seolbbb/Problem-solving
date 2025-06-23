n = int(input())

lst = []
rank = [1 for _ in range(n)]

for _ in range(n):
    a, b = map(int, input().split())
    lst.append((a, b))

for i in range(n):
    for j in range(i+1, n):
        if lst[i][0] > lst[j][0] and lst[i][1] > lst[j][1]:
            rank[j] += 1
        elif lst[i][0] < lst[j][0] and lst[i][1] < lst[j][1]:
            rank[i] += 1

print(*rank)