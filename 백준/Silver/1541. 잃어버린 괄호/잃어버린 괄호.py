eq = input()
num = ''
lst = [[] for _ in range(51)]
i = 1
ans = 0


for c in eq:
    if c.isnumeric():
        num += c
    elif c == '+':
        lst[i].append(int(num))
        num = ''
    else:
        lst[i].append(int(num))
        num = ''
        i += 1
lst[i].append(int(num))

print(-(sum([sum(x) for x in lst]) - 2*sum(lst[1])))