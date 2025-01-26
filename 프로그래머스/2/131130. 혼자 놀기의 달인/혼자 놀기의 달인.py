def solution(cards):
    cards = [0] + cards
    visit = [0 for _ in range(len(cards))]
    group = []
    
    for i in range(1, len(cards)):
        if visit[i] == 1:
            continue
        visit[i] = 1
        cnt = 1
        nxt = cards[i]
        
        while True:
            if visit[nxt] == 1:
                break
            visit[nxt] = 1
            cnt += 1
            nxt = cards[nxt]
        group.append(cnt)
        
    if len(group) == 1:
        answer = 0
    else:
        group.sort(reverse = True)
        answer = group[0] * group[1]
    
    return answer