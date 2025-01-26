def solution(n, words):
    used = {}
    answer = [0, 0]
    
    for i in range(len(words)):
        turn = i//n + 1
        user = i%n + 1
        cur = words[i]
        
        if cur in used:
            answer = [user, turn]
            break
        if i != 0 and cur[0] != words[i-1][-1]:
            answer = [user, turn]
            break
        used[cur] = 1
        
    return answer