def solve():
    global N, M
    N, M = map(int, input().split())
    field = []
    score = 0

    for _ in range(N):
        line = list(map(int, input().split()))
        field.append(line)

    while True:
        result = find_biggest_group(field)

        if len(result) == 0:
            break
        score += len(result)**2

        for x, y in result:
            field[x][y] = -2


        field = apply_gravity(field)
        next_field = []

        # 반시계 방향으로 회전
        for y in reversed(range(N)):
            temp = []
            for x in range(N):
                temp.append(field[x][y])
            next_field.append(temp)

        field = apply_gravity(next_field)

    print(score)


def apply_gravity(field):
    global N

    for x in reversed(range(N)):
        for y in range(N):
            elm = field[x][y]
            if elm >= 0:
                next_x = x
                while True:
                    next_x += 1
                    if next_x >= N:
                        break
                    if field[next_x][y] >= -1: break
                if (next_x > x):
                    field[x][y] = -2
                    field[next_x - 1][y] = elm

    return field



def find_biggest_group(field):
    global N
    # 이동 정보 > 0: 북쪽, 1: 동쪽, 2: 남쪽, 3: 서쪽
    move_info = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)}
    result = []
    result_rainbow = []

    queue = []
    visited = []

    for i in range(N):
        for r in range(N):
            if (i, r) not in visited:
                if field[i][r] > 0:
                    group = [(i, r)]
                    visited.append((i, r))
                    queue.append((i, r, field[i][r], group, list()))
                    while queue:
                        x, y, stan_val, group, rainbow = queue.pop(0)
                        # 4방향으로 진행
                        for direct in range(4):
                            move_x, move_y = move_info[direct]
                            next_x = x + move_x
                            next_y = y + move_y

                            # 범위 검사
                            if (0 <= next_x < N) and (0 <= next_y < N):
                                next_val = field[next_x][next_y]
                                # 방문 검사
                                if (next_x, next_y) not in visited:
                                    if (next_x, next_y) not in rainbow:
                                        if next_val == 0:
                                            rainbow.append((next_x, next_y))
                                            group.append((next_x, next_y))
                                            queue.append((next_x, next_y, stan_val, group, rainbow))
                                        if stan_val == next_val:
                                            visited.append((next_x, next_y))
                                            group.append((next_x, next_y))
                                            queue.append((next_x, next_y, stan_val, group, rainbow))

                    if len(group) > 1:
                        if len(group) > len(result):
                            result = group.copy()
                            result_rainbow = rainbow.copy()
                        elif len(group) == len(result):
                            if len(result) > 0 and len(group) > 0:
                                if len(rainbow) > len(result_rainbow):
                                    result = group.copy()
                                    result_rainbow = rainbow.copy()
                                elif len(rainbow) == len(result_rainbow):
                                    if group[0][0] > result[0][0]:
                                        result = group.copy()
                                        result_rainbow = rainbow.copy()
                                    elif group[0][0] == result[0][0]:
                                        if group[0][1] > result[0][1]:
                                            result = group.copy()
                                            result_rainbow = rainbow.copy()
    return result


solve()