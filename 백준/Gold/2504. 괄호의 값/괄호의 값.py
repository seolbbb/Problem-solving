s = input()
lst = []

for x in s:
    # 여는 괄호, 대괄호면 스택에 추가.
    if x == '(' or x == '[':
        lst.append(x)
        continue
    # 닫는 괄호 ')' 일 때
    if x == ')':
        if not lst:
            print(0)
            exit(0)
        if lst[-1] == '(':  # 직전에 여는 괄호 '('가 왔다면 숫자 2로 치환
            lst[-1] = 2
        else:
            while len(lst) >= 2 and type(lst[-2]) == int and type(lst[-1]) == int:
                a = lst.pop()
                lst[-1] += a
            if len(lst) < 2:
                print(0)
                exit(0)  
            if lst[-2] == '(':  # 완성된 괄호 '()' 안에 있는 숫자들을 모두 더한 후 *2를 해서 내보냄.
                a = lst.pop()
                lst.pop()
                lst.append(a * 2)
    #닫는 괄호 ']' 일 때
    if x == ']':
        if not lst:
            print(0)
            exit(0)
        if lst[-1] == '[':  # 직전에 여는 괄호 '['가 왔다면 숫자 3으로 치환
            lst[-1] = 3
        else:
            while len(lst) >= 2 and type(lst[-2]) == int and type(lst[-1]) == int:
                a = lst.pop()
                lst[-1] += a
            if len(lst) < 2:
                print(0)
                exit(0)   
            if lst[-2] == '[':  #완성된 괄호 '[]' 안에 있는 숫자들을 모두 더한 후 *3을 해서 내보냄.
                a = lst.pop()
                lst.pop()
                lst.append(a * 3)
try: 
    print(sum(lst))
except:
    print(0)