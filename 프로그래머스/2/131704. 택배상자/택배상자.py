# 임시 컨테이너 입구에서만 상자를 뺄 수 있다. -> stack의 pop()
# 벨트에서 오는 상자들도 stack으로 볼 수 있음.
# 두 컨테이너의 top을 확인해서 원하는 상자가 있는지 확인한다.
# 1. 원하는 상자가 있는 경우 컨테이너에서 꺼내고 answer += 1
# 2. 원하는 상자가 없고 컨테이너에 상자가 남아 있는 경우 원래 컨테이너에서 상자를 꺼내 임시 컨테이너에 넣는다.
# 3. 원하는 상자가 없고 컨테이너에 상자가 없는 경우 종료한다.

def solution(order):
    s1 = [i for i in range(1,len(order)+1)][::-1]
    s2 = []
    idx = 0
    
    while idx < len(order):
        cur = order[idx]
        
        if s1 and s1[-1] == cur:
            s1.pop()
            idx += 1
        elif s2 and s2[-1] == cur:
            s2.pop()
            idx += 1
        else:
            if s1:
                s2.append(s1.pop())
            else:
                break
    
    answer = idx
    return answer