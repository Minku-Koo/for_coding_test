def find_score(start_x, start_y):
    global field, N, M
    queue = [(start_x, start_y)]
    visited = []
    score = 0

    while queue:
        x, y = queue.pop(0)
        # 방문 검사
        if (x, y) not in visited:
            # 현재 위치 방문 기록
            visited.append((x, y))
            # 현재 위치 점수 담기
            score += field[x][y]
            for direct in range(4):
                move_x, move_y = move_info[direct]
                # 한칸 이동
                next_x, next_y = (x + move_x), (y + move_y)

                # overflow 및 underflow 검사
                if (0 <= next_x < N) and (0 <= next_y < M):
                    # 같은 값을 가지고 있는지 검사
                    if field[x][y] == field[next_x][next_y]:
                        queue.append((next_x, next_y))

    return score


def roll_dice(curt_diagram, direction):
    next_diagram = []

    for line in curt_diagram:
        next_diagram.append(line.copy())

    # 북쪽으로 굴리기
    if direction == 0:
        # 가운데 열 위쪽으로 이동
        next_diagram[3][1] = curt_diagram[0][1]
        next_diagram[2][1] = curt_diagram[3][1]
        next_diagram[1][1] = curt_diagram[2][1]
        next_diagram[0][1] = curt_diagram[1][1]
    # 동쪽으로 굴리기
    elif direction == 1:
        # 4자 모양으로 오른쪽으로 이동
        next_diagram[3][1] = curt_diagram[1][2]
        next_diagram[1][0] = curt_diagram[3][1]
        next_diagram[1][1] = curt_diagram[1][0]
        next_diagram[1][2] = curt_diagram[1][1]
    # 남쪽으로 굴리기
    elif direction == 2:
        # 가운데 열 아래쪽으로 이동
        next_diagram[3][1] = curt_diagram[2][1]
        next_diagram[2][1] = curt_diagram[1][1]
        next_diagram[1][1] = curt_diagram[0][1]
        next_diagram[0][1] = curt_diagram[3][1]
    # 서쪽으로 굴리기
    elif direction == 3:
        # 4자 모양으로 왼쪽으로 이동
        next_diagram[3][1] = curt_diagram[1][0]
        next_diagram[1][0] = curt_diagram[1][1]
        next_diagram[1][1] = curt_diagram[1][2]
        next_diagram[1][2] = curt_diagram[3][1]

    return next_diagram


def move_dice(dice_info):
    global field, move_info, N, M

    x, y = dice_info['x'], dice_info['y']
    diagram, direction = dice_info['diagram'], dice_info['direction']
    score = dice_info['score']

    move_x, move_y = move_info[direction]

    # 주사위 한 칸 이동
    next_x = x + move_x
    next_y = y + move_y

    # overflow 및 underflow 검사
    # 이동할 수 없으면 방향 반대로 바꾸기
    if (next_x < 0) or (next_x >= N) or (next_y < 0) or (next_y >= M):
        direction += 2
        if direction > 3:
            direction -= 4
        # 방향 반대로 바꿔서 다시 이동
        move_x, move_y = move_info[direction]
        # 주사위 한 칸 이동
        next_x = x + move_x
        next_y = y + move_y

    # 주사위 굴리기
    diagram = roll_dice(diagram, direction)

    # 점수 찾기
    score += find_score(next_x, next_y)

    # 맨 밑 숫자 꺼내기 (A)
    dice_num = diagram[3][1]
    # 필드 숫자 꺼내기 (B)
    field_num = field[next_x][next_y]

    # A > B 이면 시계 방향 90도 회전
    if dice_num > field_num:
        direction += 1
        if direction == 4:
            direction = 0
    # A < B인 경우 반시계 방향 90도 회전
    elif dice_num < field_num:
        direction -= 1
        if direction < 0:
            direction = 3

    return {'x': next_x, 'y': next_y, 'diagram': diagram,
            'direction': direction, 'score': score}


# 주사위 전개도
dice_diagram = [
    [0, 2, 0],
    [4, 1, 3],
    [0, 5, 0],
    [0, 6, 0]
]

# 주사위 정보
dice_info = {
    'x': 0, 'y': 0,
    'diagram': dice_diagram,
    'direction': 1,
    'score': 0
}

# 주사위 방향 이동정보
# 0: 북쪽, 1: 동쪽, 2: 남쪽, 3: 서쪽
move_info = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)}

# 필드 크기, 이동 횟수 입력
N, M, K = map(int, input().split())
field = []

# 필드 정보 입력
for _ in range(N):
    line = list(map(int, input().split()))
    field.append(line)

# 반복횟수만큼 주사위 굴리기
for _ in range(K):
    dice_info = move_dice(dice_info)

print(dice_info['score'])