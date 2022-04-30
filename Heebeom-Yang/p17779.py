import sys

def solve():
    global N, total_pop, pop_field
    N = int(input())


    pop_field = []

    for _ in range(N):
        line = list(map(int, input().split()))
        pop_field.append(line)
    # 총 인구수 구하기
    total_pop = 0
    for line in pop_field:
        for elm in line:
            total_pop += elm

    min_gap = float('inf')

    for d1 in range(1, N):
        for d2 in range(1, N):
            for x in range(1, (N - d1 - d2) + 1):
                for y in range(d1 + 1, (N - d2) + 1):
                    field = draw_border(x, y, d1, d2)
                    pops = draw_field(field, x, y, d1, d2)
                    gap = max(pops) - min(pops)
                    if float(gap) < min_gap:
                        min_gap = float(gap)

    # 기준점 및 경계 길이 정하기
    print(int(min_gap))


def draw_field(field, x, y, d1, d2):
    global N, total_pop, pop_field
    pops = [0, 0, 0, 0, 0]

    # 1번 선거구 그리기
    for r in range(1, (x + d1)):
        for c in range(1, (y + 1)):
            # 경계선 만나면
            if field[r - 1][c - 1] == 5:
                break
            pops[0] += pop_field[r - 1][c - 1]
            field[r - 1][c - 1] = 1

    # 2번 선거구 그리기
    for r in range(1, (x + d2) + 1):
        for c in range(N, y, -1):
            # 경계선 만나면
            if field[r - 1][c - 1] == 5:
                break
            pops[1] += pop_field[r - 1][c - 1]
            # 다른 값 만나면 시작
            field[r - 1][c - 1] = 2

    # 3번 선거구 그리기
    for r in range((x + d1), N + 1):
        for c in range(1, (y - d1 + d2)):
            # 경계선 만나면
            if field[r - 1][c - 1] == 5:
                break
            pops[2] += pop_field[r - 1][c - 1]
            field[r - 1][c - 1] = 3

    # 4번 선거구 그리기
    for r in range((x + d2) + 1, N + 1):
        for c in range(N, (y - d1 + d2) - 1, -1):
            # 경계선 만나면
            if field[r - 1][c - 1] == 5:
                break
            pops[3] += pop_field[r - 1][c - 1]
            field[r - 1][c - 1] = 4
    pops[4] = total_pop - sum(pops)
    return pops


def draw_border(x, y, d1, d2):
    border_list = []
    field = [[0] * N for _ in range(N)]

    # 1번 경계선 그리기
    weight = 0
    while True:
        border_list.append((x + weight, y - weight))
        if (x + weight, y - weight) == (x + d1, y - d1):
            break
        weight += 1

    # 2번 경계선 그리기
    weight = 0
    while True:
        border_list.append((x + weight, y + weight))
        if (x + weight, y + weight) == (x + d2, y + d2):
            break
        weight += 1

    # 3번 경계선 그리기
    weight = 0
    while True:
        border_list.append((x + d1 + weight, y - d1 + weight))
        if (x + d1 + weight, y - d1 + weight) == (x + d1 + d2, y - d1 + d2):
            break
        weight += 1

    # 4번 경계선 그리기
    weight = 0
    while True:
        border_list.append((x + d2 + weight, y + d2 - weight))
        if (x + d2 + weight, y + d2 - weight) == (x + d2 + d1, y + d2 - d1):
            break
        weight += 1
    
    # 경계선 field에 그리기
    border_list = list(set(border_list))

    for x, y in border_list:
        field[x - 1][y - 1] = 5

    return field


solve()