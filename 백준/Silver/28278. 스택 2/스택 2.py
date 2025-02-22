import sys
input = sys.stdin.readline

n = int(input())
stack = []

for _ in range(n):
    lst = list(map(int, input().split()))

    if len(lst) == 2:
        stack.append(lst[1])
    
    else:
        if lst[0] == 2 or lst[0] == 5:
            if stack:
                if lst[0] == 5:
                    print(stack[-1])
                else:
                    print(stack.pop())
            else:
                print(-1)
        elif lst[0] == 3:
            print(len(stack))
        else:
            if stack:
                print(0)
            else:
                print(1)