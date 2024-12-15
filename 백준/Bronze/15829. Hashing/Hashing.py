l = int(input())
s = input()
alpha = 'abcdefghijklmnopqrstuvwxyz'
dict = {}
for i in range(1,27):
    dict[alpha[i-1]] = i
result = 0

for i in range(l):
    result += dict[s[i]]*(31**i)

print(result%1234567891)