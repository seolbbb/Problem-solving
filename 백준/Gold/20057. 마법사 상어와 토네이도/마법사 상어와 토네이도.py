def check(x, y, portion):
    global ans
    if x < 0 or x >= n or y < 0 or y >= n:
        ans += int(portion * dust)
    else:
        A[x][y] += int(portion * dust)

n = int(input())
A = [list(map(int, input().split())) for _ in range(n)]
visit = [[0 for _ in range(n)] for _ in range(n)]

dir = [(0, -1), (1, 0), (0, 1), (-1, 0)]
cur = (n // 2, n // 2)
visit[n // 2][n // 2] = 1
cur_dir = 0
ans = 0

while cur != (0, 0):
    x, y = cur
    nxt_dir = (cur_dir + 1) % 4
    nx = x + dir[cur_dir][0]
    ny = y + dir[cur_dir][1]
    cur = (nx, ny)
    visit[nx][ny] = 1
    dust = A[nx][ny]

    if dust > 0:
        A[nx][ny] = 0

        tmp = cur
        cur_x, cur_y = tmp

        alpha = dust
        alpha -= int(0.05 * dust)
        for _ in range(2):
            alpha -= int(0.1 * dust)
            alpha -= int(0.07 * dust)
            alpha -= int(0.01 * dust)
            alpha -= int(0.02 * dust)

        # 진행 방향
        cur_x += dir[cur_dir][0]
        cur_y += dir[cur_dir][1]
        if cur_x < 0 or cur_x >= n or cur_y < 0 or cur_y >= n:
            ans += alpha
        else:
            A[cur_x][cur_y] += alpha
        cur_x += dir[cur_dir][0]
        cur_y += dir[cur_dir][1]
        check(cur_x, cur_y, 0.05)

        #진행 방향 좌우
        for i in [1, 3]:
            cur_x, cur_y = tmp
            lr = (cur_dir + i) % 4

            cur_x += dir[lr][0]
            cur_y += dir[lr][1]
            check(cur_x, cur_y, 0.07)
            
            for j in [1, 3]:
                cur_xx = cur_x + dir[(lr + j) % 4][0]
                cur_yy = cur_y + dir[(lr + j) % 4][1]

                if i == 1:
                    if j == 1:
                        check(cur_xx, cur_yy, 0.01)
                    else:
                        check(cur_xx, cur_yy, 0.1)
                else:
                    if j == 1:
                        check(cur_xx, cur_yy, 0.1)
                    else:
                        check(cur_xx, cur_yy, 0.01)


            cur_x += dir[lr][0]
            cur_y += dir[lr][1]
            check(cur_x, cur_y, 0.02)

    # print(*A, sep = '\n')
    # res = 0
    # for row in A:
    #     res += sum(row)
    # print(res, ans)
    # print()

    if visit[nx + dir[nxt_dir][0]][ny + dir[nxt_dir][1]] == 0:
        cur_dir = nxt_dir

print(ans)