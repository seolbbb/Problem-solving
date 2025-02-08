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
    # 빈 list에 시작일이 start보다 작은 꽃들 모두 저장
    lst = []
    while flowers and flowers[0][0] <= start:
        lst.append(heapq.heappop(flowers))
    # 시작일이 start보다 작은 꽃이 없으면 조건 만족 x -> break
    if len(lst) == 0:
        break
    # 위에서 구한 가능한 꽃들 중 끝나는 날이 가장 큰 꽃으로 start 갱신
    cnt += 1
    start = sorted(lst, reverse= True, key= lambda x:x[1])[0][1]
    # 끝나는 날이 11월30일 이후라면 break
    if start >= 1201:
        ans = 1
        break

if ans == 0:
    print(0)
else:
    print(cnt)