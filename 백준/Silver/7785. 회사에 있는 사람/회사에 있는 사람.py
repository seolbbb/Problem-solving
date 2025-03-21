import sys
input = sys.stdin.readline

n = int(input())
state = dict()

for _ in range(n):
    name, stat = map(str, input().rstrip().split())

    if stat == 'enter':
        state[name] = 1
    elif stat == 'leave':
        state[name] = 0

state = dict(sorted(state.items(), reverse=True))

for m, s in state.items():
    if s == 1:
        print(m)