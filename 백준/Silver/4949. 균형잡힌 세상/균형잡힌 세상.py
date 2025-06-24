import sys
input = sys.stdin.readline

while True:
    sen = input().rstrip()
    if sen == '.':
        break

    lst = []
    ans = 'yes'

    for char in sen:
        if char == '[' or char == '(':
            lst.append(char)
        elif char == ']':
            if lst and lst[-1] == '[':
                lst.pop()
            else:
                ans = 'no'
                break
        elif char == ')':
            if lst and lst[-1] == '(':
                lst.pop()
            else:
                ans = 'no'
                break
    
    if lst:
        ans = 'no'

    print(ans)