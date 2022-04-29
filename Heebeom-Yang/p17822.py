def solve():
    global N, M

    N, M, T = map(int, input().split())
    field = []
    move_list = []

    for _ in range(N):
        line = list(map(int, input().split()))
        field.append(line)

    for _ in range(T):
        x, d, k = list(map(int, input().split()))
        move_list.append((x, d, k))

    for move in move_list:
        target_x, direct, distance = move
        temp = target_x
        # 끝까지 2배 하면서 원판 돌리기
        while target_x <= N:
            move_line(field, target_x, direct, distance)
            target_x += temp

        # 인접한 원소 찾기 BFS
        near_list = find_near(field)

        for x, y in near_list:
            field[x][y] = 0
        # 만약 인접한 원소 없으면
        if len(near_list) == 0:
            elm_sum, elm_num = sum_field(field)
            if elm_num > 0:
                elm_avg = elm_sum / elm_num
                for x in range(N):
                    for y in range(M):
                        elm = float(field[x][y])
                        if elm != 0.0:
                            if elm > elm_avg:
                                field[x][y] -= 1
                            elif elm < elm_avg:
                                field[x][y] += 1

    elm_sum, _ = sum_field(field)
    print(elm_sum)

def sum_field(field):
    elm_sum = 0
    elm_num = 0

    for line in field:
        for elm in line:
            if elm != 0:
                elm_num += 1
            elm_sum += elm

    return elm_sum, elm_num

def find_near(field):
    global N, M
    result = []
    move_info = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)}

    for x in range(N):
        for y in range(M):
            if field[x][y] != 0:
                queue = [(x, y)]
                # visited.append((x, y))
                visited = [(x, y)]
                while queue:
                    x, y = queue.pop()
                    curt_elm = field[x][y]

                    for direct in range(4):
                        move_x, move_y = move_info[direct]
                        next_x = x + move_x
                        next_y = y + move_y
                        # overflow 처리
                        if next_y == M:
                            next_y = 0
                        # underflow 처리
                        if next_y == -1:
                            next_y = (M - 1)

                        # x만 검사
                        if 0 <= next_x < N:
                            # 방문 검사
                            if (next_x, next_y) not in visited:
                                next_elm = field[next_x][next_y]
                                if curt_elm == next_elm:
                                    visited.append((next_x, next_y))
                                    result.append((x, y))
                                    result.append((next_x, next_y))

    return list(set(result))


def move_line(field, target_x, direct, distance):
    global N, M

    for x in range(N):
        if x == (target_x - 1):
            # 시계방향으로 회전
            if direct == 0:
                for _ in range(distance):
                    temp = []
                    last_elm = field[x][M - 1]
                    temp.append(last_elm)

                    for idx in range(M - 1):
                        temp.append(field[x][idx])

                    field[x] = temp[:]
            # 반시계방향으로 회전
            elif direct == 1:
                for _ in range(distance):
                    temp = []
                    first_elm = field[x][0]

                    for idx in range(1, M):
                        temp.append(field[x][idx])
                    temp.append(first_elm)

                    field[x] = temp[:]

    return field


solve()