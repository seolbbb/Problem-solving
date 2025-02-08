import sys
import heapq
input = sys.stdin.readline
'''
 (달 * 100 + 일) 형식으로 날짜 저장.
 [start, end] 
 first는 301로, start <= 301 이면서 end가 가장 큰 꽃 구하기.
 first를 start로 갱신, 다시 start <= first 이면서 end가 가장 큰 꽃 구하기...
'''
n = int(input())
start = 301
flowers = []
cnt = 0
ans = 0

for _ in range(n):
    a, b, c, d = map(int, input().split())
    heapq.heappush(flowers, [a*100 + b, c*100 + d])

while flowers:
    lst = []
    
    while flowers and flowers[0][0] <= start:
        lst.append(heapq.heappop(flowers))
    if len(lst) == 0:
        break
    cnt += 1
    start = sorted(lst, reverse= True, key= lambda x:x[1])[0][1]
    if start >= 1201:
        ans = 1
        break

if ans == 0:
    print(0)
else:
    print(cnt)