import sys
input = sys.stdin.readline

string = input().rstrip()
boom = input().rstrip()
ans = ['' for _ in range(1000001)]
ans_idx = 0

for i in range(len(string)):
    if string[i] == boom[0]:
        ans_idx += 1
        ans[ans_idx] += string[i]
    else:
        ans[ans_idx] += string[i]
    
    if ans[ans_idx] == boom:
        ans[ans_idx] = ''
        ans_idx -= 1

if len(ans[ans_idx]) == 0:
    print('FRULA')
else:
    for i in range(ans_idx+1):
        print(ans[i], end='')