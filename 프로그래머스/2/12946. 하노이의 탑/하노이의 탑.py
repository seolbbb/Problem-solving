def solution(n):
    def hannoi(n, s1, s2):
        if n == 1:
            answer.append([s1, s2])
            return
        hannoi(n-1, s1, 6-s1-s2)
        hannoi(1, s1, s2)
        hannoi(n-1, 6-s1-s2, s2)

    answer = []
    hannoi(n, 1, 3)
    print(answer)
    
    return answer