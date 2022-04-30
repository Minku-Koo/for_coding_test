from itertools import combinations
from collections import deque
def solve():
    global N, M, min_sec, blank_num

    N, M = map(int, input().split())
    field = []
    virus_list = []

    for _ in range(N):
        line = list(map(int, input().split()))
        field.append(line)
    blank_num = 0
    for x in range(N):
        for y in range(N):
            if field[x][y] == 0:
                blank_num += 1
            if field[x][y] == 2:
                virus_list.append((x, y))

    min_sec = float('inf')
    for active in combinations(virus_list, M):
        sec = activate_virus(field, active)
        if float(sec) <= min_sec:
            min_sec = float(sec)

    if min_sec == float('inf'):
        print(-1)
    else:
        print(int(min_sec))


def get_active(arr, n):
    result = []

    if n == 0:
        return [[]]
    for i in range(0, len(arr)):
        elm = arr[i]
        rest_arr = arr[i + 1:]
        for comb in get_active(rest_arr, n - 1):
            result.append([elm] + comb)
    return result


def activate_virus(input_field, virus_list):
    global N, min_sec, blank_num
    move_info = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)}

    queue = deque()
    visited = [[0] * N for _ in range(N)]

    for x, y in virus_list:
        queue.append((x, y, 0))
        visited[x][y] = 1
    max_depth = 0
    curt_blank = 0
    next_field = [[-1] * N for _ in range(N)]
    while queue:
        x, y, depth = queue.popleft()
        if curt_blank > blank_num:
            return max_depth
        if depth > min_sec:
            return float('inf')
        next_field[x][y] = depth
        if depth > max_depth:
            max_depth = depth
        for direct in range(4):
            move_x, move_y = move_info[direct]
            next_x = x + move_x
            next_y = y + move_y

            # 범위 검사
            if (0 <= next_x < N) and (0 <= next_y < N):
                # 방문 검사
                if visited[next_x][next_y] != 1:
                    visited[next_x][next_y] = 1
                    if input_field[next_x][next_y] != 1:
                        curt_blank += 1
                        queue.append((next_x, next_y, depth + 1))
    for line in next_field:
        print(line)
    if blank_num == 0:
        return 0

    # if curt_blank < blank_num:
    #     return float('inf')
    for x in range(N):
        for y in range(N):
            if next_field[x][y] == -1 and input_field[x][y] != 1 and input_field[x][y] != 2:
                return float('inf')
    return max_depth


solve()