import sys
input = sys.stdin.readline

n, m, b = map(int,input().split())
blocks = [list(map(int,input().split())) for _ in range(n)]
time = [0 for _ in range(257)]
h = 0

for i in range(257):
    remain = b
    for j in range(n):
        for k in range(m):
            if blocks[j][k] > i:
                time[i] += (blocks[j][k] - i) * 2
                remain += blocks[j][k] - i
            else:
                time[i] += i - blocks[j][k] 
                remain -= i - blocks[j][k]
    
    if remain >= 0 and time[i] <= time[h]:
        h = i

print(time[h],h)