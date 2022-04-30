move_info = {1: (0, 1), 2: (0, -1), 3: (-1, 0), 4: (1, 0)}


def solve():
    global N, K, field, horse_field

    N, K = map(int, input().split())
    field = []
    horse_field = [[[] for _ in range(N)] for _ in range(N)]

    # 칸 정보 입력
    for _ in range(N):
        line = list(map(int, input().split()))
        field.append(line)

    # 말 정보 입력
    for idx in range(K):
        x, y, d = map(int, input().split())
        horse_field[x - 1][y - 1].append((idx + 1, d))

    turns = 1
    while True:
        is_end = move_field()
        if is_end is True:
            print(turns)
            break
        if turns > 1000:
            print(-1)
            break
        turns += 1


def check_end(horse_field):
    global N

    for x in range(N):
        for y in range(N):
            horse_list = horse_field[x][y]
            if len(horse_list) >= 4:
                return True
    return False


def move_field():
    global N, K, field, horse_field

    for target_idx in range(1, K + 1):
        is_selected = False

        for x in range(N):
            for y in range(N):
                horse_list = horse_field[x][y]
                if is_selected is False:
                    # 해당칸에 해당말 있으면
                    for i in range(len(horse_list)):
                        idx, direct = horse_list[i]

                        if idx == target_idx:
                            is_selected = True

                            move_x, move_y = move_info[direct]
                            next_x = x + move_x
                            next_y = y + move_y

                            # 범위 검사
                            if (0 <= next_x < N) and (0 <= next_y < N):
                                # 해당 말 인덱스 다음 전부 가져오기
                                next_field = field[next_x][next_y]
                                move_list = horse_list[i:]

                                # 만약 하얀색 칸이면
                                if next_field == 0:
                                    horse_field[x][y] = horse_list[:i]
                                    # 다음 위치에 그대로 추가
                                    horse_field[next_x][next_y] += move_list
                                # 만약 빨간색 칸이면
                                elif next_field == 1:
                                    horse_field[x][y] = horse_list[:i]
                                    # 이동할 말 뒤집기
                                    move_list.reverse()
                                    horse_field[next_x][next_y] += move_list
                                # 만약 파란색 칸이면
                                elif next_field == 2:
                                    # 방향 뒤집고
                                    direct = reverse_direct(direct)

                                    # 한번 더 이동
                                    move_x, move_y = move_info[direct]
                                    next_x = x + move_x
                                    next_y = y + move_y

                                    # 뒤집은 방향 반영
                                    horse_list[i] = idx, direct
                                    # 이동할 목록 다시 가져오기
                                    move_list = horse_list[i:]

                                    # 범위 검사
                                    if (0 <= next_x < N) and (0 <= next_y < N):
                                        next_field = field[next_x][next_y]
                                        # 또 이동하려는 방향에 파란색블록 아니면
                                        if next_field != 2:
                                            # 만약 하얀색 칸이면
                                            if next_field == 0:
                                                horse_field[x][y] = horse_list[:i]
                                                # 다음 위치에 그대로 추가
                                                horse_field[next_x][next_y] += move_list
                                            # 만약 빨간색 칸이면
                                            elif next_field == 1:
                                                horse_field[x][y] = horse_list[:i]
                                                # 이동할 말 뒤집기
                                                move_list.reverse()
                                                horse_field[next_x][next_y] += move_list
                                        # 파란색 블록이면 이동하지 않기
                                        else:
                                            horse_field[x][y] = horse_list
                                    # 뒤집은 방향 그대로 저장
                                    else:
                                        horse_field[x][y] = horse_list
                            # 벗어나는 경우 방향 반대로
                            else:
                                # 방향 뒤집고
                                direct = reverse_direct(direct)

                                # 한번 더 이동
                                move_x, move_y = move_info[direct]
                                next_x = x + move_x
                                next_y = y + move_y

                                # 뒤집은 방향 반영
                                horse_list[i] = idx, direct
                                # 이동할 목록 다시 가져오기
                                move_list = horse_list[i:]

                                # 범위 검사
                                if (0 <= next_x < N) and (0 <= next_y < N):
                                    next_field = field[next_x][next_y]
                                    # 또 이동하려는 방향에 파란색블록 아니면
                                    if next_field != 2:
                                        # 만약 하얀색 칸이면
                                        if next_field == 0:
                                            horse_field[x][y] = horse_list[:i]
                                            # 다음 위치에 그대로 추가
                                            horse_field[next_x][next_y] += move_list
                                        # 만약 빨간색 칸이면
                                        elif next_field == 1:
                                            horse_field[x][y] = horse_list[:i]
                                            # 이동할 말 뒤집기
                                            move_list.reverse()
                                            horse_field[next_x][next_y] += move_list
                                    # 파란색 블록이면 이동하지 않기
                                    else:
                                        horse_field[x][y] = horse_list
                                # 뒤집은 방향 그대로 저장
                                else:
                                    horse_field[x][y] = horse_list
                            break
        is_end = check_end(horse_field)
        if is_end is True:
            return True
    return False

def reverse_direct(direct):
    if direct == 1:
        return 2
    elif direct == 2:
        return 1
    elif direct == 3:
        return 4
    elif direct == 4:
        return 3

solve()