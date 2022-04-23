def solve():
    global N, dir_info

    dir_info = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)}
    N = int(input())
    student_list = {}

    for _ in range(N ** 2):
        n, like_one, like_two, like_three, like_four = map(int, input().split())
        student_info = {'like': [like_one, like_two, like_three, like_four]}
        student_list[n] = student_info

    field = [[0 for _ in range(N)] for _ in range(N)]
    for student_no in student_list:
        like_list = student_list[student_no]['like']

        # 가장 좋아하는 학생 많은 자리 찾기
        result = find_most_like(field, like_list)
        # 결과가 2개 이상이면
        if len(result) > 1:
            # 가장 공백이 많은 자리 찾기
            result = find_biggest_blank(field, result)
            # 결과가 2개 이상이면
            if len(result) > 1:
                # 행이 가장 작은 칸 찾기
                result = find_minimum_row(result)
                # 결과가 2개 이상이면
                if len(result):
                    # 열이 가장 작은 칸 찾기
                    result = find_minimum_column(result)

        # 결과 반영하기
        result_x, result_y = result[0]
        field[result_x][result_y] = student_no

    score = 0

    # 만족도 조사하기
    for x in range(N):
        for y in range(N):
            curt_val = field[x][y]
            like_list = student_list[curt_val]['like']
            curt_result = []

            for direct in range(4):
                move_x, move_y = dir_info[direct]
                next_x = x + move_x
                next_y = y + move_y

                # overflow 및 underflow 검사
                if (0 <= next_x < N) and (0 <= next_y < N):
                    next_elm = field[next_x][next_y]
                    # 다음 원소가 좋아하는 사람이면
                    if next_elm in like_list:
                        curt_result.append((next_x, next_y))

            if len(curt_result) == 0:
                continue

            weight = len(curt_result) - 1
            score += 10 ** weight

    print(score)


def find_minimum_row(result_list):
    min_val = result_list[0][0]
    result = []

    for x, y in result_list:
        if x <= min_val:
            result.append((x, y))

    return result


def find_minimum_column(result_list):
    min_val = result_list[0][1]
    result = []

    for x, y in result_list:
        if y <= min_val:
            result.append((x, y))

    return result


def find_most_like(field, like_list):
    global N, dir_info
    result = {'coord': [], 'value': 0}

    for x in range(N):
        for y in range(N):
            curt_elm = field[x][y]
            # 좋아하는 사람을 담을 결과배열
            curt_like_list = []
            # 현재 위치가 빈칸인 경우만 실행
            if curt_elm == 0:
                for direct in range(4):
                    move_x, move_y = dir_info[direct]
                    next_x = x + move_x
                    next_y = y + move_y

                    # overflow 및 underflow 검사
                    if (0 <= next_x < N) and (0 <= next_y < N):
                        next_elm = field[next_x][next_y]
                        # 다음 원소가 좋아하는 사람이면
                        if next_elm in like_list:
                            curt_like_list.append((next_x, next_y))

                curt_val = len(curt_like_list)

                if curt_val > result['value']:
                    result['coord'] = [(x, y)]
                    result['value'] = curt_val
                elif curt_val == result['value']:
                    result['coord'].append((x, y))

    return result['coord']


def find_biggest_blank(field, find_list):
    global N, dir_info
    result = {'coord': [], 'value': 0}

    for x, y in find_list:
        curt_elm = field[x][y]
        # 공백을 담을 결과배열
        blank_list = []

        # 현재 위치가 빈칸인 경우만 실행
        if curt_elm == 0:
            # 사방향으로 진행
            for direct in range(4):
                move_x, move_y = dir_info[direct]
                next_x = x + move_x
                next_y = y + move_y

                # overflow 및 underflow 검사
                if (0 <= next_x < N) and (0 <= next_y < N):
                    # 다음 원소 가져오기
                    next_elm = field[next_x][next_y]
                    # 다음 원소가 빈칸이면 결과에 추가
                    if next_elm == 0:
                        blank_list.append((next_x, next_y))

            # 현재 결과와 비교연산
            curt_val = len(blank_list)

            if curt_val > result['value']:
                result['coord'] = [(x, y)]
                result['value'] = curt_val
            elif curt_val == result['value']:
                result['coord'].append((x, y))

    return result['coord']


solve()