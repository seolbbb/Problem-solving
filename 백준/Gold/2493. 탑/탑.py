import sys

n = int(sys.stdin.readline()) 
lst = list(map(int,sys.stdin.readline().split()))
stack = [0]
ans = [0]


for i in range(1,n):
    while lst[i] > lst[stack[-1]]:
        stack.pop()
        if len(stack) == 0:
            break
    
    if len(stack) == 0:
        ans.append(0)
        stack.append(i)
    
    elif lst[i] <= lst[stack[-1]]:
        ans.append(stack[-1]+1)
        stack.append(i)

print(*ans)
