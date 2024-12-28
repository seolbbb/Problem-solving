import sys
input = sys.stdin.readline

n = int(input())
lst = [list(map(int,input().split())) for _ in range(n)]
start = 0
cnt = 0

lst.sort(key=lambda x:(x[1],x[0]))

for time in lst:
    st,end = time
    if st >= start:
        cnt += 1
        start = end

print(cnt)