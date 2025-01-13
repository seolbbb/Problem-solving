import sys
import heapq
input = sys.stdin.readline

def sync(hq):
    while hq and hq[0][1] in deleted:
        heapq.heappop(hq)

t = int(input())

for _ in range(t):
    k = int(input())
    min_hq = []
    max_hq = []
    deleted = {}
    cur_id = 0

    for _ in range(k):
        cmd, num = input().strip().split()
        num = int(num)

        if cmd == 'I':
            heapq.heappush(min_hq, (num, cur_id))
            heapq.heappush(max_hq, (-num, cur_id))
            cur_id += 1

        elif cmd == 'D':
            if num == 1:
                sync(max_hq)
                if max_hq:
                    val, id_ = heapq.heappop(max_hq)
                    deleted[id_] = True
            else:
                sync(min_hq)
                if min_hq:
                    val, id_ = heapq.heappop(min_hq)
                    deleted[id_] = True
        
        sync(min_hq)
        sync(max_hq)

    sync(min_hq)
    sync(max_hq)

    if len(min_hq) == 0:
        print('EMPTY')
    else:
        print(-max_hq[0][0], min_hq[0][0])