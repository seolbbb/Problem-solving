s = input()
result = set()

for length in range(1, len(s)+1):
    for i in range(len(s)):
        j = length + i
        if j > len(s):
            continue
        result.add(s[i:j])

print(len(result))