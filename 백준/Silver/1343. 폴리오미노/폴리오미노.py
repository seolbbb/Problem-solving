board = input()
length = 0
ans = ''

for c in board:
    if c == 'X':
        length += 1

    if c == '.':
        if length % 2 == 1:
            print(-1)
            exit()
        else:
            ans += (length//4) * 'AAAA'
            length %= 4
            if length:
                ans += 'BB'
        length = 0
        ans += '.'
    
if length % 2 == 1:
    print(-1)
    exit()
    
if length and length % 2 != 1:
    ans += (length//4) * 'AAAA'
    length %= 4
    if length:
        ans += 'BB'

print(ans)