# 두 큐의 합이 같게 만들지 못 하는 경우 : 모든 원소의 합이 홀수일 때

from collections import deque

def solution(queue1, queue2):
    answer = 0
    max_move = len(queue1)
    s1 = sum(queue1)
    s2 = sum(queue2)
    total = s1 + s2
    
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    
    if total % 2 == 1:
        answer = -1
        return answer
    
    while answer < 3 * max_move:
        if s1 > s2:
            #print('queue1 -> queue2')
            #print(queue1, queue2)
            cur = queue1.popleft()
            queue2.append(cur)
            s1 -= cur
            s2 += cur
            answer += 1
        elif s1 < s2:
            #print('queue2 -> queue1')
            #print(queue1, queue2)
            cur = queue2.popleft()
            queue1.append(cur)
            s1 += cur
            s2 -= cur
            answer += 1
        else:
            return answer
    print(s1, s2, answer)
    return -1