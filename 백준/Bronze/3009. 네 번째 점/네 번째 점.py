lst = []

for _ in range(3):
    x, y = map(int,input().split())
    lst.append([x,y])

x = 0
y = 0

for i in range(3):
    if [j[0] for j in lst].count(lst[i][0]) == 1:
        x = lst[i][0]
    if [j[1] for j in lst].count(lst[i][1]) == 1:
        y = lst[i][1]

print(x, y)