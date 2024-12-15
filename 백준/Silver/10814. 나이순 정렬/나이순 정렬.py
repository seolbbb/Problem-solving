import sys

n = int(sys.stdin.readline())
lst = []

for i in range(n):
    temp = list(sys.stdin.readline().split())
    temp.append(i)
    temp[0] = int(temp[0])
    lst.append(temp)
    
lst.sort(key=lambda x: (x[0],x[2]))
for i in range(n):
    print(*lst[i][:-1])