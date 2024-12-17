import sys

n = int(sys.stdin.readline())
cnt = 0
for i in range(n):
    st = sys.stdin.readline().rstrip()
    lst = []
    for s in st:
        if len(lst) == 0:
            lst.append(s)
            continue
        if s == lst[-1]:
            lst.pop()        
        else:
            lst.append(s)
    if len(lst) > 0:
        cnt += 1 
print(n-cnt)    