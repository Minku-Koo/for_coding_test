def solve():
    global blue_field, green_field

    N = int(input())
    block_list = []

    # 파란색 필드
    blue_field = [[0, 0, 0, 0] for _ in range(6)]
    # 초록색 필드
    green_field = [[0, 0, 0, 0] for _ in range(6)]

    score = 0

    for _ in range(N):
        t, x, y = map(int, input().split())
        # 블록이 1x1인 경우
        if t == 1:
            block_list.append([(x, y)])
        # 블록이 1x2인 경우
        elif t == 2:
            block_list.append([(x, y), (x, y + 1)])
        elif t == 3:
            block_list.append([(x, y), (x + 1, y)])

    for block in block_list:
        move_blue_field(block[:])
        move_green_field(block[:])
        # for line in green_field:
        #     print(line)
        # print()
        score += check_line()
        check_overflow()
    print(score)
    block_sum = 0
    for x in range(2, 6):
        for y in range(4):
            if green_field[x][y] == 1:
                block_sum += 1
    for x in range(2, 6):
        for y in range(4):
            if blue_field[x][y] == 1:
                block_sum += 1
    print(block_sum)


# 빈 라인을 검사하는 함수
def check_overflow():
    global blue_field, green_field

    for x in range(2):
        for y in range(4):
            if blue_field[x][y] == 1:
                temp = [line[:] for line in blue_field[x:(6-x)]]
                for i in range(4):
                    blue_field[i + 2] = temp[i]
                blue_field[0] = [0, 0, 0, 0]
                blue_field[1] = [0, 0, 0, 0]

    for x in range(2):
        for y in range(4):
            if green_field[x][y] == 1:
                temp = [line[:] for line in green_field[x:(6-x)]]
                for i in range(4):
                    green_field[i + 2] = temp[i]
                green_field[0] = [0, 0, 0, 0]
                green_field[1] = [0, 0, 0, 0]


# 꽉 찬 라인을 검사하는 함수
def check_line():
    global blue_field, green_field
    score = 0

    for x in range(6):
        for y in range(4):
            if green_field[x][y] == 0:
                break
            # 만약 한줄이 다 있으면
            if y == 3:
                score += 1
                # 위에 줄 다 떙기기
                temp = [line[:] for line in green_field[0:x]]
                for prev_x in range(0, x):
                    green_field[prev_x + 1] = temp[prev_x][:]
                # 맨 위에줄 0으로
                green_field[0] = [0, 0, 0, 0]

    for x in range(6):
        for y in range(4):
            if blue_field[x][y] == 0:
                break
            # 만약 한줄이 다 있으면
            if y == 3:
                score += 1
                # 위에 줄 다 떙기기
                temp = [line[:] for line in blue_field[0:x]]
                for prev_x in range(0, x):
                    blue_field[prev_x + 1] = temp[prev_x][:]
                # 맨 위에줄 0으로
                blue_field[0] = [0, 0, 0, 0]

    return score


def move_blue_field(block):
    global blue_field

    col_sub = 0
    # 가장 작은 원소가 0보다 크게 맞춰주기 위해 계산
    for _, y in block:
        sub = 1
        while True:
            if (y - sub) < 0:
                is_end = True
                break
            if sub > col_sub:
                col_sub = sub
            sub += 1

        if is_end is True:
            break

    # 행 최솟값 맞춰주기
    for idx in range(len(block)):
        x, y = block[idx]
        # 행열 바꿔주면서 저장
        block[idx] = ((y - col_sub), x)

    is_end = False
    sum_num = 1

    while True:
        for idx in range(len(block)):
            x, y = block[idx]
            # 범위 및 블록 검사
            if ((x + sum_num) == 6) or (blue_field[x + sum_num][y] == 1):
                is_end = True
                break

        if is_end is True:
            break
        sum_num += 1

    sum_num -= 1
    # 결과값 반영하기
    for x, y in block:
        blue_field[x + sum_num][y] = 1


# 개별의 블록을 움직임
def move_green_field(block):
    global green_field
    row_sub = 0

    # 가장 작은 원소가 0보다 크게 맞춰주기 위해 계산
    for x, _ in block:
        sub = 1
        while True:
            if (x - sub) < 0:
                is_end = True
                break
            if sub > row_sub:
                row_sub = sub
            sub += 1

        if is_end is True:
            break

    # 행 최솟값 맞춰주기
    for idx in range(len(block)):
        x, y = block[idx]
        block[idx] = ((x - row_sub), y)
    is_end = False
    sum_num = 1

    # 초록색 필드 움직이기
    while True:
        for idx in range(len(block)):
            x, y = block[idx]
            # 범위 및 블록 검사
            if ((x + sum_num) == 6) or (green_field[x + sum_num][y] == 1):
                is_end = True
                break

        if is_end is True:
            break
        sum_num += 1

    sum_num -= 1
    # 결과값 반영하기
    for x, y in block:
        green_field[x + sum_num][y] = 1


solve()
