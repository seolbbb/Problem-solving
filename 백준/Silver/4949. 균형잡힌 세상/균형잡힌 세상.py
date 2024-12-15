import sys

while True:
    s = sys.stdin.readline().rstrip()
    lst = []
    no = 0
    if s == '.':
        break
    for x in s:
        if x == '(' or x == '[':
            lst.append(x)
        if x == ')':
            if not lst:
                no = 1
                break
            elif lst[-1] == '(':
                lst.pop()
            else:
                no = 1
                break
        if x == ']':
            if not lst:
                no = 1
                break
            elif lst[-1] == '[':
                lst.pop()
            else:
                no = 1
                break
    if lst or no == 1:
        print('no')
    else:
        print('yes')