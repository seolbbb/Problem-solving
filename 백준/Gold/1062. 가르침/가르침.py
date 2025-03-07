def backtrack(idx, num):
    global ans, learned

    if len(unknown_lst) - idx < (k - 5) - num:
        return
    
    if num == k - 5:
        tmp = 0
        for key, val in counter.items():
            if (learned & key) == key:
                tmp += val
        ans = max(ans, tmp)
        return

    for i in range(idx, len(unknown_lst)):
        bit = 1 << (ord(unknown_lst[i]) - ord('a'))
        learned = learned | bit
        backtrack(i + 1, num + 1)
        learned = learned & ~bit

n, k = map(int, input().split())
default = set(['a', 'c', 'i', 'n', 't'])
counter = dict()
unknown = set()
ans = 0

learned = 0
for char in ['a', 'c', 'i', 'n', 't']:
    learned |= (1 << (ord(char) - ord('a')))

for _ in range(n):
    string = input()
    s = set([c for c in string if c not in default])
    unknown.update(list(s))

    bitmask = 0
    for char in set(string):
        bitmask |= (1 << (ord(char) - ord('a')))
    counter[bitmask] = counter.get(bitmask, 0) + 1

unknown_lst = list(unknown)

if k < 5:
    ans = 0
elif k == 26:
    ans = n
elif k - 5 >= len(unknown_lst):
    ans = n
else:
    backtrack(0, 0)

print(ans)