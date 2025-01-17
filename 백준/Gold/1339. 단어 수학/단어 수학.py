n = int(input())
m = 9
words = [input() for _ in range(n)]
char = {}
res = 0

for word in words:
    L = len(word) - 1
    for i, s in enumerate(word):
        char[s] = char.get(s,0) + 10 ** (L - i)

char = dict(sorted(char.items(),key = lambda x: x[1], reverse = True))

for num in char.values():
    res += m * num
    m -= 1

print(res)