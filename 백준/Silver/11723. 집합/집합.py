import sys

n = int(sys.stdin.readline())
s_lst = []

for i in range(n):

    m = list(map(str,sys.stdin.readline().split()))
    if len(m) == 2:
        x = int(m[-1])
    if m[0] == 'add' and x not in s_lst:
        s_lst.append(x)
    if m[0] == 'remove' and x in s_lst:
        s_lst.remove(x)
    if m[0] == 'check':
        if x in s_lst:
            print(1)
        else:
            print(0)
    if m[0] == 'toggle':
        if x in s_lst:
            s_lst.remove(x)
        else:
            s_lst.append(x)
    if m[0] == 'all':
        s_lst = [i for i in range(1,21)]
    if m[0] == 'empty':
        s_lst = []
    x = 0