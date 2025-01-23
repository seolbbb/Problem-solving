def pwd(vowel, cons, num):

    if len(password) == L:
        if vowel >= 1 and cons >= 2:
            print(''.join(map(str,password)))
        return
    
    for i in range(num,c):
        if char[i] in 'aeiou':
            vowel += 1
        else:
            cons += 1
        password.append(char[i])
        pwd(vowel, cons, i+1)
        if password.pop() in 'aeiou':
            vowel -= 1
        else:
            cons -= 1

L, c = map(int,input().split())
char = sorted(list(map(str,input().split())))
password = []

pwd(0,0,0)