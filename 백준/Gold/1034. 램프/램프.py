'''
홀수 = 홀수 + 짝수
짝수 = 홀수 + 홀수, 짝수 + 짝수

k가 홀수라면, 홀수의 갯수가 홀수개인 숫자들의 합으로 나타낼 수 있음.
예를 들어 5 -> 1 4 or 1 1 1 2 or 1 1 1 1 1(홀수의 갯수 1, 3, 5)
k가 짝수라면, 홀수의 갯수가 짝수개인 숫자들의 합으로 나타낼 수 있음.
예를 들어 6 -> 6 or 1 1 4 or 1 1 1 1 2(홀수의 갯수 0, 2, 4)

즉, m개의 열 중 몇개의 열을 바꿀 수 있는지 알아낼 수 있음.
'''

n, m = map(int, input().split())
rows = [input() for _ in range(n)]
k = int(input())
nums = []
dic = dict()
ans = 0

# k가 홀수, 짝수일 때 나눠서 몇 개의 열 바꿀 수 있는지 nums에 저장
if k % 2 == 0:
    for i in range(0, 51, 2):
        if i <= m and i <= k:
            nums.append(i)
else:
    for i in range(1, 50, 2):
        if i <= m and i <= k:
            nums.append(i)

# 꺼져 있는 전구가 num개 인 경우인 상태 dictionary로 count함.
for num in nums:
    for row in rows:
        cnt = 0
        for char in row:
            if char == '0':
                cnt += 1
        
        if cnt == num:
            dic[row] = dic.get(row, 0) + 1

if dic:
    print(max(dic.values()))
else:
    print(0)