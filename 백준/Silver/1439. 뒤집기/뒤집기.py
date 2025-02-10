s = input()
zero = 0
one = 0

for i in range(1, len(s)):
    if s[i] != s[i-1]:
        if s[i] == '1':
            zero += 1
        else:
            one += 1

if s[-1] == '0':
    zero += 1
else:
    one += 1
    
print(min(zero, one))