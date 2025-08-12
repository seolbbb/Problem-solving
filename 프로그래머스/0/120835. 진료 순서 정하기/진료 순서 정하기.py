def solution(emergency):
    answer = []
    order = dict()
    sorted_emergency = sorted(emergency, reverse=True)
    
    for idx, item in enumerate(sorted_emergency):
        order[item] = idx + 1
        
    for item in emergency:
        answer.append(order[item])
    
    return answer