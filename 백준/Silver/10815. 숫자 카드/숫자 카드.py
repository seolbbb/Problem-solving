import sys
input = sys.stdin.readline

n = int(input())
num = set(map(int, input().split()))
m = int(input())
cards = list(map(int, input().split()))

for card in cards:
    if card in num:
        print(1, end=' ')
    else:
        print(0, end=' ')