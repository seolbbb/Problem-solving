import sys
input = sys.stdin.readline

n = int(input())
cards = list(map(int, input().split()))
score = [0 for _ in range(n)]
nums = [-1 for _ in range(1000001)]

for idx, num in enumerate(cards):
    nums[num] = idx

for i in range(1000001):
    if nums[i] > -1:
        for j in range(i*2, 1000001, i):
            if nums[j] > -1:
                score[nums[i]] += 1
                score[nums[j]] -= 1

print(*score)