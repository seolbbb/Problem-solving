import sys

n = int(sys.stdin.readline())
n_lst = list(map(int,sys.stdin.readline().split()))
m = int(sys.stdin.readline())
m_lst = list(map(int,sys.stdin.readline().split()))

dict = {}
ans = []

for i in n_lst:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1

for i in m_lst:
    if i in dict:
        ans.append(str(dict[i]))
    else:
        ans.append(str(0))
    
sys.stdout.write(' '.join(ans))