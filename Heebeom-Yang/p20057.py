def solve():
    global N, field

    N = int(input())
    field = []

    for _ in range(N):
        line = list(map(int, input().split()))
        field.append(line)

    x = y = (N // 2)
    move = -1
    line_size = 1
    total_flow = 0

    while line_size < N:
        for _ in range(line_size):
            y += move
            # 서쪽
            if move < 0:
                flow = move_dust(x, y, 'west')
            else:
                flow = move_dust(x, y, 'east')
            total_flow += flow

        move *= -1

        for _ in range(line_size):
            x += move
            if move < 0:
                flow = move_dust(x, y, 'north')
            else:
                flow = move_dust(x, y, 'south')
            total_flow += flow

        line_size += 1

    # 마지막 한번 돌기
    for _ in range(line_size):
        y += move
        total_flow += move_dust(x, y, 'west')

    print(total_flow)


def move_dust(x, y, direct):
    global field, N
    total_flow = 0
    dir_info = {'north': (-1, 0), 'east': (0, 1), 'south': (1, 0), 'west': (0, -1)}
    seek_info = {'north': [((-1, 1), 0.1), ((-1, -1), 0.1), ((0, 1), 0.07), ((0, -1), 0.07), ((-2, 0), 0.05),
                          ((0, -2), 0.02), ((0, 2), 0.02), ((1, 1), 0.01), ((1, -1), 0.01)],


                 'south': [((1, 1), 0.1), ((1, -1), 0.1), ((0, 1), 0.07), ((0, -1), 0.07), ((2, 0), 0.05),
                          ((0, -2), 0.02), ((0, 2), 0.02), ((-1, 1), 0.01), ((-1, -1), 0.01)],
                 'west': [((-1, -1), 0.1), ((1, -1), 0.1), ((-1, 0), 0.07), ((1, 0), 0.07), ((0, -2), 0.05),
                          ((-2, 0), 0.02), ((2, 0), 0.02), ((-1, 1), 0.01), ((1, 1), 0.01)],
                 'east': [((-1, 1), 0.1), ((1, 1), 0.1), ((-1, 0), 0.07), ((1, 0), 0.07), ((0, 2), 0.05),
                          ((-2, 0), 0.02), ((2, 0), 0.02), ((-1, -1), 0.01), ((1, -1), 0.01)]}

    curt_dust = field[x][y]
    stan_dust = curt_dust
    field[x][y] = 0
    seek_list = seek_info[direct]

    for coord, weight in seek_list:
        move_x, move_y = coord
        seek_x = x + move_x
        seek_y = y + move_y

        seek_dust = int(stan_dust * weight)
        curt_dust -= seek_dust

        if is_movable(seek_x, seek_y):
            field[seek_x][seek_y] += seek_dust
        else:
            total_flow += seek_dust

    move_x, move_y = dir_info[direct]
    next_x = x + move_x
    next_y = y + move_y

    if is_movable(next_x, next_y):
        field[next_x][next_y] += curt_dust
    else:
        total_flow += curt_dust

    return total_flow


def is_movable(next_x, next_y):
    if (0 <= next_x < N) and (0 <= next_y < N):
        return True
    return False

solve()