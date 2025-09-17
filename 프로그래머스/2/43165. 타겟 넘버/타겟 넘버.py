def solution(numbers, target):
    answer = 0
    
    def backtrack(i, total):
        nonlocal answer
        
        if i == len(numbers):
            if total == target:
                answer += 1
            return

        backtrack(i + 1, total + numbers[i])
        backtrack(i + 1, total - numbers[i])
    
    backtrack(0, 0)
    return answer