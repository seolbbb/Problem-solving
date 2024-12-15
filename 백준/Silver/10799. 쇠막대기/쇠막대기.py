line = input()
stack = []
laser = 1
stick_cnt = 0
stick = 0
num = 0

for x in line:
    if x == '(':
        stack.append(x)
        laser = 1
        stick_cnt += 1
    if x == ')':
        if laser == 1:
            laser = 0
            stack.pop()
            stick_cnt -= 1
            num += len(stack)
        else:
            laser = 0
            stack.pop()
            stick_cnt -= 1
            stick += 1

print(num + stick)