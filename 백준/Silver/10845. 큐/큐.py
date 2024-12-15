import sys
stack = []

n = int(input())

for i in range(n):
    
    com = list(sys.stdin.readline().split())
    size = len(stack)

    if len(com) == 2:
        stack.append(com[1])
    elif com[0] == 'pop':
        if size != 0:    
            print(stack.pop(0))
        else:
            print(-1)
    elif com[0] == 'size':
        print(size)
    elif com[0] == 'empty':
        if size != 0:
            print(0)
        else:
            print(1)
    elif com[0] == 'front':
        if size != 0:    
            print(stack[0])
        else:
            print(-1)
    elif com[0] == 'back':
        if size != 0:    
            print(stack[-1])
        else:
            print(-1)