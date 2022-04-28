move_info = {1: (-1, 0), 2: (-1, -1), 3: (0, -1), 4: (1, -1), 5: (1, 0), 6: (1, 1), 7: (0, 1), 8: (-1, 1)}


def solve():
    field = [[0, 0, 0, 0] for _ in range(4)]

    for x in range(4):
        line = list(map(int, input().split()))
        y = 0
        for i in range(0, 8, 2):
            idx, direct = line[i:(i+2)]
            field[x][y] = (idx, direct)
            y += 1

    move_shark(field)


def move_shark(input_field):
    stack = [(0, 0, 0, input_field)]
    visited = []
    max_eat = 0

    while stack:
        x, y, sum_eat, field = stack.pop()

        # 방문 처리하기
        visited.append((x, y))

        # 현재 방향, 이동 정보 가져오기
        idx, direct = field[x][y]
        move_x, move_y = move_info[direct]

        # 현재 위치의 물고기 먹기
        sum_eat += idx
        # 현재 위치로 상어 이동
        field[x][y] = (-1, direct)

        if sum_eat > max_eat:
            max_eat = sum_eat

        # 물고기 이동
        field = move_fish(field)

        # 상어 현재 칸에서 떠나기
        field[x][y] = (0, 0)

        # 상어 이동
        next_x = x + move_x
        next_y = y + move_y

        # 다음 위치 찾기
        while (0 <= next_x < 4) and (0 <= next_y < 4):
            # 방문 검사
            # 다음 위치의 정보 가져오기
            next_idx, _ = field[next_x][next_y]
            # 다음 위치에 물고기가 있으면
            if next_idx > 0:
                stack.append((next_x, next_y, sum_eat, [line.copy() for line in field]))
            next_x += move_x
            next_y += move_y

    print(max_eat)


# 1 ~ 16번의 물고기가 이동하는 함수
def move_fish(field):
    next_field = [[0, 0, 0, 0] for _ in range(4)]

    # 1 ~ 16까지 반복 >> 물고기 번호
    for target_idx in range(1, 17):
        movable = False
        # 물고기 번호 찾기
        for x in range(4):
            for y in range(4):
                fish_idx, fish_direct = field[x][y]
                # 만약 찾는 물고기면
                if (fish_idx == target_idx) and (movable is False):
                    # 이동가능한지 8방향으로 조사
                    for _ in range(8):
                        # 먼저 이동정보 받아오기
                        move_x, move_y = move_info[fish_direct]
                        next_x = x + move_x
                        next_y = y + move_y
                        # 먼저 이동 가능한지 검사
                        movable = is_movable(field, next_x, next_y)

                        # 이동가능 하면 이동해주고 반복문 break
                        if movable is True:
                            # 다음 원소 가져오기
                            next_idx, next_direct = field[next_x][next_y]
                            # 현재 원소랑 서로 바꾸기
                            field[x][y] = (next_idx, next_direct)
                            field[next_x][next_y] = (fish_idx, fish_direct)
                            break

                        # 불가능하면 방향에 +1 해줘서 반시계 방향으로 회전하기
                        fish_direct += 1
                        # 방향 overflow 처리
                        if fish_direct == 9:
                            fish_direct = 1

    return field


def is_movable(field, next_x, next_y):
    # 인덱스 범위 검사
    if (0 <= next_x < 4) and (0 <= next_y < 4):
        # 이동할 칸 정보 가져오기
        next_idx, _ = field[next_x][next_y]
        # 상어 있는지 검사
        if next_idx != -1:
            return True

    return False


solve()