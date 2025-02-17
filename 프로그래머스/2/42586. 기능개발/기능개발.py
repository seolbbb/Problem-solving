def solution(progresses, speeds):
    stack = []
    answer = []
    for i in range(len(progresses)):
        day = ((100-progresses[i]) + (speeds[i]-1)) // speeds[i]
        if not stack or max(stack) >= day:
            stack.append(day)
        else:
            answer.append(len(stack))
            stack = [day]            
    answer.append(len(stack))

    return answer