from heapq import heappop, heappush, heapify

def solution(n, works):
    answer = 0

    if n >= sum(works): # 남은 작업량 없으면 종료
        return answer
    
    hq = [-w for w in works]
    heapify(hq)
    
    for _ in range(n):
        w = heappop(hq)
        w += 1
        heappush(hq, w)
    
    works = [-w for w in hq]
    square = [i ** 2 for i in range(0, max(works) + 1)]
    
    for w in works:
        answer += square[w]

    return answer