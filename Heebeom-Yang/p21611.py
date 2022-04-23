# 방향에 따른 시작 인덱스
# 1 > 북쪽, 2 > 남쪽, 3: 서쪽, 4: 동쪽
direct_info = {1: 7, 2: 3, 3: 1, 4: 5}

# 폭발 정보를 담을 정보
# 각 인덱스는 몇번 구슬인지를 의미함 (1 > 1번 구슬)
explode_info = {1: 0, 2: 0, 3: 0}


# 블리자드를 쓸 때 해당되는 구슬의 인덱스 찾기
def find_index(direction, distance):
    result = []

    weight = direct_info[direction]
    result.append(weight)

    for _ in range(distance - 1):
        weight += 8
        num = result[-1] + weight
        result.append(num)

    return result


# 블리자드 시전
def blizzard(flat_field, direction, distance):
    kill_list = find_index(direction, distance)
    next_field = []

    for idx in range(len(flat_field)):
        if idx in kill_list:
            continue
        next_field.append(flat_field[idx])


    return next_field


# 연속한 구슬 폭발
def explode_bead(flat_field):
    global explode_info

    next_field = []
    explode_num = 0
    stan_num = flat_field[1]
    count = 0

    for idx in range(len(flat_field)):
        curt_num = flat_field[idx]
        # 기준숫자와 현재 숫자 같으면
        if stan_num == curt_num:
            count += 1
        # 그 둘이 다르면
        else:
            # 구슬이 4개 이상 연속이면
            if count > 3:
                weight = 1
                for _ in range(count):
                    # 폭발정보 입력
                    explode_info[stan_num] += 1
                    explode_num += 1
                    # 폭발한 구슬 임시로 표시
                    flat_field[idx - weight] = -1
                    weight += 1

            stan_num = curt_num
            count = 1

    # 새 배열에 폭발한 원소 제외하고 담기
    for idx in range(len(flat_field)):
        curt_num = flat_field[idx]
        if curt_num == -1:
            continue
        next_field.append(curt_num)

    return next_field, explode_num


# 구슬이 변화함
def trans_bead(flat_field):
    global N
    stan_num = flat_field[1]
    next_field = [0]
    count = 0

    for idx in range(1, len(flat_field)):
        curt_num = flat_field[idx]
        # 기준숫자와 현재 숫자 같으면
        if stan_num == curt_num:
            count += 1
        # 그 둘이 다르면
        else:
            # 새 배열에 정보 채워넣기
            next_field.append(count)
            next_field.append(stan_num)

            stan_num = curt_num
            count = 1

    for _ in range((N * N) - len(next_field)):
        next_field.append(0)

    # 흘러넘친 배열 슬라이싱
    return next_field[:(N * N)]


field = []
flat_field = []
blizzard_list = []

# 필드 크기 및 블리자드 횟수 입력
N, M = map(int, input().split())

# 구슬 정보를 담은 배열 입력받기
for _ in range(N):
    line = list(map(int, input().split()))
    field.append(line)

# 달팽이 배열 순회를 위한 변수
line_size = N
move = 1
x = 0
y = -1

# 달팽이 배열 순회하여 구슬정보 담기
for _ in range(N):
    for _ in range(line_size):
        y += move
        flat_field.append(field[x][y])
    line_size -= 1

    for _ in range(line_size):
        x += move
        flat_field.append(field[x][y])

    move *= -1

# 편 배열 역순으로 뒤집기
flat_field.reverse()


# 블리자드 정보 입력
for _ in range(M):
    d, s = map(int, input().split())
    blizzard_list.append((d, s))

for d, s in blizzard_list:
    # 블리자드 사용
    flat_field = blizzard(flat_field, d, s)
    while True:
        flat_field, explode_num = explode_bead(flat_field)
        if explode_num == 0:
            break

    flat_field = trans_bead(flat_field)

print(explode_info[1] + (explode_info[2] * 2) + (explode_info[3] * 3))