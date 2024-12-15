import sys
N = int(sys.stdin.readline().rstrip())
lst = []

for i in range(N):
    lst.append(str(sys.stdin.readline().rstrip()))

uniq = set(lst)
uniq_lst = list(uniq)
uniq_lst.sort()
uniq_lst.sort(key=len)

for i in uniq_lst:
    print(i)