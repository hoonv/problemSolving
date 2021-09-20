n, m = map(int, input().split(" "))
board = [list(map(int, input().split(" "))) for _ in range(n)]
blocks = [
    [(0, 0), (0, 1), (0, 2), (0, 3)],
    [(0, 0), (1, 0), (2, 0), (3, 0)],

    [(0, 0), (0, 1), (1, 0), (1, 1)],

    [(0, 0), (0, 1), (1, 1), (2, 1)],
    [(0, 0), (0, -1), (1, -1), (2, -1)],
    [(0, 0), (1, 0), (1, -1), (1, -2)],
    [(0, 0), (-1, 0), (-1, -1), (-1, -2)],
    [(0, 0), (0, -1), (-1, -1), (-2, -1)],
    [(0, 0), (0, 1), (-1, 1), (-2, 1)],
    [(0, 0), (-1, 0), (-1, 1), (-1, 2)],
    [(0, 0), (1, 0), (1, 1), (1, 2)],

    [(0, 0), (0, 1), (1, 1), (1, 2)],
    [(0, 0), (1, 0), (1, -1), (2, -1)],
    [(0, 0), (0, -1), (1, -1), (1, -2)],
    [(0, 0), (-1, 0), (-1, -1), (-2, -1)],

    [(0, 0), (1, 0), (1, 1), (1, -1)],
    [(0, 0), (0, 1), (1, 1), (-1, 1)],
    [(0, 0), (-1, -1), (-1, 0), (-1, 1)],
    [(0, 0), (0, -1), (1, -1), (-1, -1)],

]
ret = 0
for i in range(n):
    for j in range(m):
        for block in blocks:
            count = 0
            for ele in block:
                ny, nx = i + ele[0], j + ele[1]
                if ny < 0 or nx < 0 or ny >= n or nx >= m:
                    break
                count += board[ny][nx]
            else:
                ret = max(ret, count)

print(ret)

