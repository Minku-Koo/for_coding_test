def solve():
    global N, K

    # N: field 크기, M: 상어 마리수, K: 냄새가 유지시간
    N, M, K = map(int, input().split())
    # 결과를 담을 초
    sec = 0

    # 상어배열 선언
    field = []
    # 냄새배열 선언
    smell_field = [[(0, 0)] * N for _ in range(N)]

    # 상어배열 입력받기
    for _ in range(N):
        line = list(map(int, input().split()))
        field.append([[(i, 0)] for i in line])

    # 각 상어의 방향 입력받기
    shark_direct = list(map(int, input().split()))

    # 각 상어마다 방향 입력해주기
    for shark_idx in range(M):
        direct = shark_direct[shark_idx]
        shark_idx += 1
        # 상어 번호 찾아서 입력
        for x in range(N):
            for y in range(N):
                if field[x][y][0][0] == shark_idx:
                    field[x][y] = [(shark_idx, direct)]

    # 상어 우선순위 입력받기
    shark_prior = {}

    for shark_idx in range(M):
        shark_idx += 1
        prior_dict = {}
        for direct in range(4):
            direct += 1
            prior_info = tuple(map(int, input().split()))
            prior_dict[direct] = prior_info
        shark_prior[shark_idx] = prior_dict

    # 초기 냄새 남기기
    if K > 1:
        smell_field = leave_smell(field, smell_field)

    while True:
        # 상어 검사
        shark_list = []

        for x in range(N):
            for y in range(N):
                shark_idx = field[x][y][0][0]
                if shark_idx > 0:
                    shark_list.append(shark_idx)

        if len(shark_list) == 0:
            print(-1)
            break
        if len(shark_list) == 1:
            print(sec)
            break
        elif sec >= 1000 and len(shark_list) > 1:
            print(-1)
            break

        # 냄새 남기기
        if K > 1:
            smell_field = leave_smell(field, smell_field)

        # 상어 이동
        field = move_shark(field, smell_field, shark_prior)

        # 냄새 감소
        for x in range(N):
            for y in range(N):
                smell_idx, smell_strength = smell_field[x][y]
                # 냄새 아예 사라지기
                if smell_strength == 1 and smell_idx > 0:
                    smell_field[x][y] = (0, 0)
                # 냄새 1씩 깎기
                elif smell_strength > 0:
                    smell_field[x][y] = (smell_idx, smell_strength - 1)

        # 상어 없애기
        for x in range(N):
            for y in range(N):
                shark_list = field[x][y]
                # 만약 상어 두개 있으면
                if len(shark_list) > 1:
                    min_idx = shark_list[0][0]
                    min_dir = shark_list[0][1]
                    # 최소 인덱스 찾기
                    for curt_idx, curt_dir in shark_list:
                        if curt_idx < min_idx:
                            min_idx = curt_idx
                            min_dir = curt_dir

                    # 해당 인덱스로 갱신
                    field[x][y] = [(min_idx, min_dir)]

        sec += 1
        # for line in field:
        #     print(line)
        # print()
        #
        # for line in smell_field:
        #     print(line)
        # print()
        # print()


# 상어 이동하는 함수
def move_shark(field, smell_field, shark_prior):
    global N, K
    # 이동 정보
    move_info = {1: (-1, 0), 2: (1, 0), 3: (0, -1), 4: (0, 1)}
    next_field = [[[(0, 0)] for _ in range(N)] for _ in range(N)]

    for x in range(N):
        for y in range(N):
            shark_idx = field[x][y][0][0]
            shark_direct = field[x][y][0][1]
            # 냄새 없는 칸 담을 배열
            no_smell = []
            # 자신의 냄새 있는 칸 담을 배열
            my_smell = []
            result = []
            # 해당 칸에 상어가 없으면 skip
            if shark_idx > 0:
                # 4방향 냄새 검사하기
                for direct in range(4):
                    direct += 1
                    move_x, move_y = move_info[direct]
                    next_x = x + move_x
                    next_y = y + move_y

                    # 범위 검사
                    if (0 <= next_x < N) and (0 <= next_y < N):
                        smell_idx, smell_strength = smell_field[next_x][next_y]
                        # 상하좌우에 냄새 없는지 검사
                        if smell_strength == 0:
                            no_smell.append((next_x, next_y, direct))
                        if smell_idx == shark_idx:
                            my_smell.append((next_x, next_y, direct))

                # 냄새 있는 칸 있으면
                if len(no_smell) > 0:
                    result = no_smell
                else:
                    result = my_smell

                # 결과 여러개면
                if len(result) > 1:
                    # 현재 상어의 우선순위 가져오기
                    prior_info = shark_prior[shark_idx]
                    # 현재 보는 방향의 우선순위 가져오기
                    prior = prior_info[shark_direct]
                    min_prior = 3
                    for next_x, next_y, curt_direct in result:
                        for prior_idx in range(4):
                            # 현재 direct 가져오기
                            if curt_direct == prior[prior_idx]:
                                # 현재 우선순위가 높으면
                                if prior_idx <= min_prior:
                                    min_prior = prior_idx
                                    result = [(next_x, next_y, curt_direct)]
                if len(result) > 0:
                    result_x, result_y, result_dir = result[0]
                    if next_field[result_x][result_y][0] == (0, 0):
                        next_field[result_x][result_y] = [(shark_idx, result_dir)]
                    else:
                        next_field[result_x][result_y].append((shark_idx, result_dir))

    return next_field


# 상어의 냄새를 남기는 함수
def leave_smell(field, smell_field):
    global N, K
    next_smell_field = []

    # 현재 냄새 정보 결과 배열에 복사하기
    for line in smell_field:
        next_smell_field.append(line.copy())

    for x in range(N):
        for y in range(N):
            shark_idx = field[x][y][0][0]
            # 해당 칸에 상어가 없으면 skip
            if shark_idx > 0:
                # K만큼 냄새 남기기
                next_smell_field[x][y] = (shark_idx, K)

    return next_smell_field


solve()