def solve():
    global N, field, pass_field
    N, M, fuel = map(int, input().split())

    field = []
    pass_list = []

    for _ in range(N):
        line = list(map(int, input().split()))
        field.append(line)

    x, y = map(int, input(). split())
    taxi_x = x - 1
    taxi_y = y - 1

    for idx in range(M):
        x, y, des_x, des_y = map(int, input().split())
        pass_list.append((x - 1, y - 1, des_x - 1, des_y - 1))

    while True:
        if len(pass_list) == 0:
            print(fuel)
            break

        # 최단 택시 승객 찾기
        target_pass, min_dist = find_shortest_pass(taxi_x, taxi_y, pass_list)
        # 데려다 줄 수 있는지 검사
        if target_pass == -1:
            print(-1)
            break

        # 택시 이동
        taxi_x, taxi_y, des_x, des_y = target_pass
        fuel -= min_dist
        # 연료 검사
        if fuel < 0:
            print(-1)
            return

        # 손님 태우기
        pass_list.remove(target_pass)

        # 목적지 검사
        dist = find_shortest(taxi_x, taxi_y, des_x, des_y)
        if dist <= -1:
            print(-1)
            return
        taxi_x = des_x
        taxi_y = des_y
        # 택시 이동
        fuel -= dist

        # 연료 검사
        if fuel < 0:
            print(-1)
            return

        # 연료 얻기
        fuel += (dist * 2)


def find_shortest(x, y, target_x, target_y):
    global N, field, pass_field

    move_info = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)}
    queue = [(x, y, 0)]
    visited = [(x, y)]
    min_dist = -1

    while queue:
        x, y, distance = queue.pop(0)

        if (x == target_x) and (y == target_y):
            min_dist = distance
            break

        for direct in range(4):
            move_x, move_y = move_info[direct]
            next_x = x + move_x
            next_y = y + move_y

            # overflow 및 underflow 검사
            if (0 <= next_x < N) and (0 <= next_y < N):
                # 방문 검사
                if (next_x, next_y) not in visited:
                    # 벽 검사
                    if field[next_x][next_y] != 1:
                        visited.append((next_x, next_y))
                        queue.append((next_x, next_y, distance + 1))

    return min_dist


def find_shortest_pass(start_x, start_y, pass_list):
    pass_coords = []
    result = []

    for x, y, _, _ in pass_list:
        pass_coords.append((x, y))

    move_info = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)}
    queue = [(start_x, start_y, 0)]
    visited = [(start_x, start_y)]
    min_dist = (N * N) + 1
    while queue:
        x, y, distance = queue.pop(0)
        if (x, y) in pass_coords:
            if distance <= min_dist:
                min_dist = distance
                result.append((x, y, distance))

        for direct in range(4):
            move_x, move_y = move_info[direct]
            next_x = x + move_x
            next_y = y + move_y

            # overflow 및 underflow 검사
            if (0 <= next_x < N) and (0 <= next_y < N):
                # 방문 검사
                if (next_x, next_y) not in visited:
                    # 벽 검사
                    if field[next_x][next_y] != 1:
                        visited.append((next_x, next_y))
                        queue.append((next_x, next_y, distance + 1))

    if len(result) == 0:
        return -1, -1
    elif len(result) == 1:

        for idx in range(len(pass_list)):
            pass_x, pass_y, _, _ = pass_list[idx]
            if result[0][0] == pass_x and result[0][1] == pass_y:
                result_idx = idx
                break

        return pass_list[result_idx], min_dist
    else:
        target_pass = result[0]
        for x, y, _ in result:
            target_x, target_y, _ = target_pass
            # 거리 같으면 행번호 검사
            if x < target_x:
                target_pass = (x, y, _)
            elif x == target_x:
                # 행번호 같으면 열번호 검사
                if y < target_y:
                    target_pass = (x, y, _)
        for idx in range(len(pass_list)):
            pass_x, pass_y, _, _ = pass_list[idx]
            if target_pass[0] == pass_x and target_pass[1] == pass_y:
                result_idx = idx
                break

        return pass_list[result_idx], min_dist
solve()