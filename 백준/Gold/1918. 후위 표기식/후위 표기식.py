str = input()
stack = []
ans = ''

for char in str:
    if char.isalpha():
        ans += char
    elif char == '(':
        stack.append(char)
    elif char == '*' or char == '/':
        while stack and (stack[-1] == '*' or stack[-1] == '/'):
            ans += stack.pop()
        stack.append(char)
    elif char == '+' or char == '-':
        while stack and stack[-1] != '(':
            ans += stack.pop()
        stack.append(char)
    else:
        while stack and stack[-1] != '(':
            ans += stack.pop()
        stack.pop()
    
while stack:
    ans += stack.pop()

print(ans)