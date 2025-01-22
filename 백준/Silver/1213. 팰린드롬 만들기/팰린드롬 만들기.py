name = sorted(list(input()))
odd = 0
odd_s = ''
char = {}
ans = ''

for s in name:
    char[s] = char.get(s,0) + 1

for st, n in char.items():
    ans += st * (n//2)
    if n % 2 == 1:
        if odd == 1:
            print("I'm Sorry Hansoo")
            exit()
        odd_s = st
        odd = 1

print(ans + odd_s + ans[::-1])