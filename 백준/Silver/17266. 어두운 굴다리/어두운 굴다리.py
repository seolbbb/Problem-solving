import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
crd = list(map(int, input().split()))
dist = []
for i in range(1, m):
    dist.append(((crd[i]-crd[i-1])+1) // 2)
dist.append(crd[0])
dist.append(n-crd[-1])

print(max(dist))