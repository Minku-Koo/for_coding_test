def solve():
    global N

    N, K = map(int, input().split())

    field = list(map(int, input().split()))
    robot_list = []
    iter_num = 0

    while True:
        iter_num += 1
        field, robot_list = move_field(field, robot_list)
        robot_list = move_robots(field, robot_list)
        # 올리는 칸에 로봇 올리기
        if field[0] > 0:
            robot_list.append(0)
            field[0] -= 1

        # 내구도 0인 칸 갯수
        zero_num = 0
        # 내구도 0인 칸 세기
        for elm in field:
            if elm == 0:
                zero_num += 1

        # 내구도 0인 칸이 K 이상이면
        if zero_num >= K:
            print(iter_num)
            break


# 로봇 이동
def move_robots(field, robot_list):
    global N
    next_robot_list = []

    for i in range(len(robot_list)):
        robot_x = robot_list[i]
        next_x = get_next_x(robot_x)

        # 해당칸에 내구도 1 이상이면
        if field[next_x] > 0:
            # 로봇이 내리는 위치면
            if next_x == (N - 1):
                robot_list[i] = -1
                field[next_x] -= 1
                continue
            # 해당칸에 로봇 없으면
            if next_x not in robot_list:
                    # 로봇 이동
                    robot_list[i] = next_x
                    # 내구도 감소
                    field[next_x] -= 1

    for elm in robot_list:
        if elm != -1:
            next_robot_list.append(elm)

    return next_robot_list


# 컨베이어 벨트 이동
def move_field(field, robot_list):
    global N

    next_field = [0 for _ in range(N * 2)]
    next_robot_list = []

    for x in range(N * 2):
        elm = field[x]
        next_x = get_next_x(x)
        next_field[next_x] = elm

    for robot_x in robot_list:
        next_x = get_next_x(robot_x)
        # 로봇이 내리는 위치 아니면
        if next_x != (N - 1):
            next_robot_list.append(next_x)

    return next_field, next_robot_list


def get_next_x(x):
    global N
    next_x = x + 1

    if next_x == (N * 2):
        next_x = 0

    return next_x


solve()