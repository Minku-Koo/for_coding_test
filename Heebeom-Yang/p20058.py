import copy


def solve():
    global N, move_info
    field = []
    move_info = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)}

    N, Q = map(int, input().split())
    N = 2 ** N

    # 필드 입력받기
    for _ in range(N):
        line = list(map(int, input().split()))
        field.append(line)

    # 마법 길이 입력받기
    lengths = list(map(int, input().split()))

    for length in lengths:
        # 인접 얼음 검사하기
        field = divide_arr(field, 2 ** length)
        next_field = [[0] * (N) for _ in range(N)]
        for x in range(N):
            for y in range(N):
                curt_val = field[x][y]
                if curt_val > 0:
                    weight = 0
                    for direct in range(4):
                        move_x, move_y = move_info[direct]
                        next_x = x + move_x
                        next_y = y + move_y

                        if (0 <= next_x < N) and (0 <= next_y < N):
                            next_val = field[next_x][next_y]
                            if next_val > 0:
                                weight += 1

                    if weight >= 3:
                        next_field[x][y] = curt_val
                    else:
                        next_field[x][y] = curt_val - 1
                else:
                    next_field[x][y] = curt_val
        field = copy.deepcopy(next_field)

    sum_num = 0
    for line in next_field:
        for elm in line:
            sum_num += elm
    depth = find_biggest(next_field)
    print(sum_num)
    print(depth)


def find_biggest(arr):
    global move_info, N
    max_depth = 0
    queue = []
    visited = []

    for i in range(N):
        for r in range(N):
            if arr[i][r] != 0 and (i, r) not in visited:
                queue.append((i, r, arr[i][r]))
                depth = 0
                while queue:
                    x, y, value = queue.pop(0)

                    for direct in range(4):
                        move_x, move_y = move_info[direct]
                        next_x = x + move_x
                        next_y = y + move_y

                        if (0 <= next_x < N) and (0 <= next_y < N):
                            if (next_x, next_y) not in visited:
                                next_val = arr[next_x][next_y]
                                if next_val > 0:
                                    depth += 1
                                    visited.append((next_x, next_y))
                                    queue.append((next_x, next_y, value))

                if depth > max_depth:
                    max_depth = depth
    return max_depth

def divide_arr(arr, length):
    global N
    next_field = [[0] * (N) for _ in range(N)]

    for start_x in range(0, N, length):
        for start_y in range(0, N, length):
            divied = []
            rotated = []
            end_x = (start_x + length)
            end_y = (start_y + length)

            # 배열 시계방향 90도로 뒤집기
            for div_y in range(start_y, end_y):
                temp = []
                for div_x in reversed(range(start_x, end_x)):
                    temp.append(arr[div_x][div_y])
                rotated.append(temp)
            
            # 다음 배열에 집어넣기
            for x in range(len(rotated)):
                for y in range(len(rotated)):
                    next_field[start_x + x][start_y + y] = rotated[x][y]

    return next_field



solve()