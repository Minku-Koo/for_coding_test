import copy


def is_movable(x, y):
    # overflow 및 underflow 검사
    if (0 <= x < 4) and (0 <= y < 4):
        # Shark 위치 검사
        if (x != shark[0]) or (y != shark[1]):
            # Smell 위치 검사
            if smell[x][y] == 0:
                return True
    return False


def move_fish():
    next_field = [[[], [], [], []] for _ in range(4)]

    for x in range(4):
        for y in range(4):
            for idx in range(len(field[x][y])):
                move_x, move_y = direct_info[field[x][y][idx]]
                # 임시로 한칸 이동
                next_x = x + move_x
                next_y = y + move_y

                # 이동가능한지 확인 >>
                for _ in range(8):
                    if is_movable(next_x, next_y) is True:
                        break
                    # 반시계방향으로 회전
                    field[x][y][idx] -= 1
                    # underflow 검사 및 처리
                    if field[x][y][idx] == 0:
                        field[x][y][idx] = 8

                    # 다시 임시로 한칸 이동
                    move_x, move_y = direct_info[field[x][y][idx]]
                    next_x = x + move_x
                    next_y = y + move_y

                # 이동가능하면 이동한 좌표값 반영하기
                if is_movable(next_x, next_y) is True:
                    next_field[next_x][next_y].append(field[x][y][idx])
                # 불가능하면 그대로 놓기
                else:
                    next_field[x][y].append(field[x][y][idx])

    return next_field


def move_shark(x, y, depth, eat, visited):
    global max_eat, shark_visited, shark

    if depth == 3:
        if eat > max_eat:
            max_eat = eat
            shark = (x, y)
            shark_visited = visited[:]
        return

    for direct in range(1, 5):
        move_x, move_y = shark_direct_info[direct]
        next_x = x + move_x
        next_y = y + move_y
        
        # overflow 및 underflow 검사
        if (0 <= next_x < 4) and (0 <= next_y < 4):
            if (next_x, next_y) not in visited:
                fish_count = len(field[next_x][next_y])
                visited.append((next_x, next_y))
                move_shark(next_x, next_y, depth + 1, eat + fish_count, visited)
                visited.pop()
            else:
                move_shark(next_x, next_y, depth + 1, eat, visited)


# 물고기 이동정보 테이블
direct_info = {1: (0, -1), 2: (-1, -1), 3: (-1, 0), 4: (-1, 1),
               5: (0, 1), 6: (1, 1), 7: (1, 0), 8: (1, -1)}

# 상어 이동정보 테이블
shark_direct_info = {1: (-1, 0), 2: (0, -1), 3: (1, 0), 4: (0, 1)}

# 물고기 위치정보 테이블
field = [[[], [], [], []] for _ in range(4)]
# 냄새 정보 테이블
smell = [[0, 0, 0, 0] for _ in range(4)]

# 물고기 수와 반복 수 입력
M, S = map(int, input().split())

# 물고기 정보 입력
for _ in range(M):
    x, y, direct = map(int, input().split())
    field[x - 1][y - 1].append(direct)

# 상어 정보 입력
x, y = map(int, input().split())
shark = (x - 1, y - 1)

for _ in range(S):
    # 물고기 복사 마법
    field_copy = copy.deepcopy(field)

    # 물고기 이동
    field = move_fish()

    # 상어 이동에 필요한 정보
    max_eat = -1
    shark_visited = []

    # 상어 이동
    move_shark(shark[0], shark[1], 0, 0, list())

    # 물고기 제거 및 냄새 새기기
    for coord in shark_visited:
        x, y = coord
        if len(field[x][y]) > 0:
            # 물고기 제거
            field[x][y] = []
            # 냄새 새기기
            smell[x][y] = 3

    # 냄새 제거
    for x in range(4):
        for y in range(4):
            if smell[x][y] > 0:
                smell[x][y] -= 1

    # 물고기 복제 반영하기
    for x in range(4):
        for y in range(4):
            for elm in field_copy[x][y]:
                field[x][y].append(elm)

# 결과 세기
result = 0
for x in range(4):
    for y in range(4):
        result += len(field[x][y])

print(result)