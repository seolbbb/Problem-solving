import sys
input = sys.stdin.readline

seq = input().rstrip()
temp = ''
prev = 0
minus = 0
total = 0

for s in seq:
    if s == '+':
        prev += int(temp)
        temp = ''
    elif s == '-':
        prev += int(temp)
        temp = ''
        if minus == 1:
            total -= prev
            prev = 0
        else:
            total += prev
            prev = 0
            minus = 1
    else:
        temp += s

prev += int(temp)

if minus == 1:
    total -= prev
else:
    total += prev

print(total)