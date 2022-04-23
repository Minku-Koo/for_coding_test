def solve():
    global direct_info, N, A
    direct_info = {1: (0, -1), 2: (-1, -1), 3: (-1, 0), 4: (-1, 1),
                   5: (0, 1), 6: (1, 1), 7: (1, 0), 8: (1, -1)}

    N, M = map(int, input().split())
    A = []

    move_list = []
    # 구름 정보
    cloud_list = [[0 for _ in range(N)] for _ in range(N)]

    # 초기 구름정보
    cloud_list[N - 1][0] = 1
    cloud_list[N - 1][1] = 1
    cloud_list[N - 2][0] = 1
    cloud_list[N - 2][1] = 1

    # 물 상태 입력
    for _ in range(N):
        line = list(map(int, input().split()))
        A.append(line)

    # 이동정보 입력
    for _ in range(M):
        d, s = map(int, input().split())
        move_list.append((d, s))

    for d, s in move_list:

        # 이동 정보를 이용해 구름 전부 이동
        next_cloud_list = [[0 for _ in range(N)] for _ in range(N)]
        for x in range(len(cloud_list)):
            for y in range(len(cloud_list)):
                if cloud_list[x][y] == 1:
                    # 거리만큼 이동
                    next_x, next_y = move_cloud(x, y, d, s)
                    next_cloud_list[next_x][next_y] = 1
                    # 이동한 곳에 비 내리기
                    A[next_x][next_y] += 1

        cloud_list = []
        # 새로운 구름 채우기
        for line in next_cloud_list:
            cloud_list.append(line)

        for x in range(len(cloud_list)):
            for y in range(len(cloud_list)):
                # 구름 있으면
                if cloud_list[x][y] == 1:
                    copy_water(x, y)

        new_cloud_list = [[0 for _ in range(N)] for _ in range(N)]

        for x in range(len(A)):
            for y in range(len(A)):
                if (A[x][y] >= 2) and (cloud_list[x][y] != 1):
                    new_cloud_list[x][y] = 1
                    A[x][y] -= 2

        # 구름 비우기
        cloud_list = []
        # 새로운 구름 채우기
        for line in new_cloud_list:
            cloud_list.append(line)

    result = 0
    # 정답 출력
    for line in A:
        for elm in line:
            result += elm

    print(result)


def copy_water(x, y):
    global A, N

    # 좌측 위 대각선 검사
    if (0 <= (x - 1) < N) and (0 <= (y - 1) < N):
        if A[x - 1][y - 1] > 0:
            A[x][y] += 1
    # 우측 위 대각선 검사
    if (0 <= (x - 1) < N) and (0 <= (y + 1) < N):
        if A[x - 1][y + 1] > 0:
            A[x][y] += 1
    # 좌측 아래 대각선 검사
    if (0 <= (x + 1) < N) and (0 <= (y - 1) < N):
        if A[x + 1][y - 1] > 0:
            A[x][y] += 1
    # 우측 아래 대각선 검사
    if (0 <= (x + 1) < N) and (0 <= (y + 1) < N):
        if A[x + 1][y + 1] > 0:
            A[x][y] += 1


# 구름 이동하기
def move_cloud(x, y, direct, distance):
    global direct_info, N
    move_x, move_y = direct_info[direct]

    next_x = x + (move_x * distance)
    next_y = y + (move_y * distance)

    next_x %= N
    next_y %= N

    # x좌표 검사
    if next_x == N:
        next_x = 0
    elif next_x < 0:
        next_x = (N - 1)

    # y좌표 검사
    if next_y == N:
        next_y = 0
    elif next_y < 0:
        next_y = (N - 1)

    return next_x, next_y


solve()
