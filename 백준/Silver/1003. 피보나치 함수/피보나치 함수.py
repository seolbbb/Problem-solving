t = int(input())

lst = [[1,0]]

for i in range(40):
    lst.append([lst[i][1],(lst[i][0]+lst[i][1])])

for i in range(t):
    n = int(input())

    print(*lst[n])