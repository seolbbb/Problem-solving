n = int(input())
s = input()
# 0:A 1:B 2:C
train = 0
# 0:5명 1:1명 2: 6명
lever = 0
multi = 0
ans = 0

for cmd in s:
    if cmd == 'P':
        if train == 1:
            multi = 1
        else:
            lever = 1-lever
    elif cmd == 'W':
        train += 1
        if train == 2:
            break

if multi == 1:
    ans = 6
else:
    if lever == 0:
        ans = 5
    else:
        ans = 1

if train >= 2:
    print(ans)
else:
    print(0)