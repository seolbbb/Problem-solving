# c= c- dz= d- lj nj s= z=

strings = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
s = input()
n = len(s)
cnt = 0
for i in range(len(strings)):
    while True:
        if strings[i] not in s:
            break
        else:
            s = s.replace(strings[i], ' ', 1)
            if strings[i] == 'dz=':
                cnt += 2
            else:
                cnt += 1

print(n - cnt)