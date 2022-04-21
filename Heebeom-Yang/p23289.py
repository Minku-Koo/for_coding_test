import sys
from copy import deepcopy
from collections import deque

input = sys.stdin.readline
dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]


def func(x, y, f):
    if check[x][y] == 0:
        check[x][y] = 1
        a[x][y] += f
        q.append([x, y])

r, c, k = map(int, input().split())
heater, checker = [], []
for i in range(r):
    a = list(map(int, input().split()))
    for j in range(c):
        if 0 < a[j] < 5:
            heater.append([i, j, a[j]])
        elif a[j] == 5:
            checker.append([i, j])

w = int(input())
wall = [[[] for _ in range(c)] for _ in range(r)]
for _ in range(w):
    x, y, d = map(int, input().split())
    wall[x-1][y-1].append(d)

a = [[0] * c for _ in range(r)]
cnt = 0
while True:
    for i, j, d in heater:
        q = deque()
        check = [[0] * c for _ in range(r)]
        nx, ny = i + dx[d], j + dy[d]
        a[nx][ny] += 5

        if not 0 <= nx + dx[d] < r or not 0 <= ny + dy[d] < c:
            continue

        q.append([nx, ny])
        flag = 0
        for f in range(4, 0, -1):
            for _ in range(len(q)):
                x, y = q.popleft()

                if d == 1:
                    if y + 1 >= c:
                        flag = 1
                        break
                    if 1 not in wall[x][y]:
                        nx, ny = x, y + 1
                        func(nx, ny, f)
                    if x - 1 >= 0:
                        if 0 not in wall[x][y] and 1 not in wall[x - 1][y]:
                            nx, ny = x - 1, y + 1
                            func(nx, ny, f)
                    if x + 1 < r:
                        if not wall[x + 1][y]:
                            nx, ny = x + 1, y + 1
                            func(nx, ny, f)

                elif d == 2:
                    if y - 1 < 0:
                        flag = 1
                        break
                    if 1 not in wall[x][y - 1]:
                        nx, ny = x, y - 1
                        func(nx, ny, f)
                    if x - 1 >= 0:
                        if 1 not in wall[x - 1][y - 1] and 0 not in wall[x][y]:
                            nx, ny = x - 1, y - 1
                            func(nx, ny, f)
                    if x + 1 < r:
                        if 1 not in wall[x + 1][y - 1] and 0 not in wall[x + 1][y]:
                            nx, ny = x + 1, y - 1
                            func(nx, ny, f)

                elif d == 3:
                    if x - 1 < 0:
                        flag = 1
                        break
                    if 0 not in wall[x][y]:
                        nx, ny = x - 1, y
                        func(nx, ny, f)
                    if y - 1 >= 0:
                        if not wall[x][y - 1]:
                            nx, ny = x - 1, y - 1
                            func(nx, ny, f)
                    if y + 1 < c:
                        if 0 not in wall[x][y + 1] and 1 not in wall[x][y]:
                            nx, ny = x - 1, y + 1
                            func(nx, ny, f)

                else:
                    if x + 1 >= r:
                        flag = 1
                        break
                    if 0 not in wall[x + 1][y]:
                        nx, ny = x + 1, y
                        func(nx, ny, f)
                    if y - 1 >= 0:
                        if 0 not in wall[x + 1][y - 1] and 1 not in wall[x][y - 1]:
                            nx, ny = x + 1, y - 1
                            func(nx, ny, f)
                    if y + 1 < c:
                        if 1 not in wall[x][y] and 0 not in wall[x + 1][y + 1]:
                            nx, ny = x + 1, y + 1
                            func(nx, ny, f)

            if flag == 1 or len(q) == 0:
                break

    temp_a = deepcopy(a)
    for x in range(r):
        for y in range(c):
            dir = []
            if x < r - 1 and 0 not in wall[x + 1][y]:
                dir.append(4)
            if 1 not in wall[x][y]:
                dir.append(1)

            for d in dir:
                nx, ny = x + dx[d], y + dy[d]
                if 0 <= nx < r and 0 <= ny < c:
                    if a[x][y] > a[nx][ny]:
                        diff = (a[x][y] - a[nx][ny]) // 4
                        temp_a[x][y] -= diff
                        temp_a[nx][ny] += diff
                    elif a[x][y] < a[nx][ny]:
                        diff = (a[nx][ny] - a[x][y]) // 4
                        temp_a[x][y] += diff
                        temp_a[nx][ny] -= diff
    a = temp_a

    for i in range(r):
        if i == 0 or i == r - 1:
            for j in range(c):
                if a[i][j] > 0:
                    a[i][j] -= 1
        else:
            for j in [0, c - 1]:
                if a[i][j] > 0:
                    a[i][j] -= 1

    cnt += 1
    if cnt > 100:
        break

    flag = 0
    for x, y in checker:
        if a[x][y] < k:
            flag = 1
            break
    if flag == 0:
        break

print(cnt)