import sys

n = int(sys.stdin.readline())
n_lst = []
stack = []
result = []
push = 1

for i in range(n):
    n_lst.append(int(sys.stdin.readline()))

for x in n_lst:
    while push <= x:
        stack.append(push)
        result.append('+')
        push += 1
    
    if stack[-1] == x:
        stack.pop()
        result.append('-')
    else:
        print('NO')
        exit(0)

print('\n'.join(result))