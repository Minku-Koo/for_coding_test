def solve():
    global N

    N, M, K = map(int, input().split())
    field = [[[] for _ in range(N)] for _ in range(N)]

    for _ in range(M):
        r, c, m, s, d = map(int, input().split())
        field[r - 1][c - 1].append((m, s, d))

    # 파이어볼 K만큼 이동
    for _ in range(K):
        field = move_fireballs(field)

    total_massive = 0

    # 파이어볼 질량 합치기
    for line in field:
        for elm_list in line:
            curt_massive = 0
            for elm in elm_list:
                curt_massive += elm[0]
            total_massive += curt_massive
    print(total_massive)


def move_fireballs(field):
    global N

    next_field = [[[] for _ in range(N)] for _ in range(N)]

    # 파이어볼 이동
    for x in range(N):
        for y in range(N):
            elm_list = field[x][y]
            for elm in elm_list:
                m, s, d = elm
                next_x, next_y = move_fireball(x, y, s, d)
                next_field[next_x][next_y].append((m, s, d))


    for x in range(N):
        for y in range(N):
            elm_list = next_field[x][y]
            elm_num = len(elm_list)
            # 만약 파이어볼이 2개 이상이면
            if elm_num > 1:
                # 일단 해당위치 파이어볼 모두 없애기
                next_field[x][y] = []
                
                # 파이어볼 모두 합치기를 위한 객체
                total_fireball = [0, 0, 0]
                # 파이어볼 모두 합치기
                for m, s, d in elm_list:
                    total_fireball[0] += m
                    total_fireball[1] += s
                    total_fireball[2] += d

                # 파이어볼 4개로 나누기
                divied_m = total_fireball[0] // 5
                divied_s = total_fireball[1] // elm_num
                # 모두 짝수 or 홀수 판별
                _, _, d = elm_list[0]

                # 첫 번째 원소 홀짝 판별
                is_all_same = True
                if d % 2 == 0: is_even = True
                else: is_even = False

                for _, _, d in elm_list:
                    if is_even:
                        # 짝수인데 홀수면
                        if d % 2 != 0:
                            is_all_same = False
                    else:
                        # 홀수인데 짝수이면
                        if d % 2 == 0:
                            is_all_same = False

                if is_all_same:
                    directs = [0, 2, 4, 6]
                else:
                    directs = [1, 3, 5, 7]

                for idx in range(4):
                    divied_fireball = (divied_m, divied_s, directs[idx])
                    if divied_m > 0:
                        next_field[x][y].append(divied_fireball)

    return next_field
    # for line in next_field:
    #     print(line)
    # print()


def move_fireball(x, y, s, d):
    global N
    # 이동정보
    move_info = {0: (-1, 0), 1: (-1, 1), 2: (0, 1), 3: (1, 1), 4: (1, 0), 5: (1, -1), 6: (0, -1), 7: (-1, -1)}

    move_x, move_y = move_info[d]

    next_x = x + (move_x * s)
    next_y = y + (move_y * s)

    return next_x % N, next_y % N


solve()