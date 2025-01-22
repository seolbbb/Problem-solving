import sys
input = sys.stdin.readline

n = int(input())
dist = list(map(int,input().split()))
price = list(map(int,input().split()))
cur_price = price[0]
ans = 0

for i in range(n-1):
    ans += cur_price * dist[i]
    if price[i+1] < cur_price:
        cur_price = price[i+1]

print(ans)