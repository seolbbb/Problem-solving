import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    lst = []
    prev = n + 1
    cnt = 0

    for _ in range(n):
        lst.append(list(map(int,input().split())))
    
    lst.sort()

    for s1, s2 in lst:
        if s2 < prev:
            cnt += 1
            prev = s2
    
    print(cnt)