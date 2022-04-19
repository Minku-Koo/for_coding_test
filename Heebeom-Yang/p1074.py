from sys import stdin

# 사분면을 구하는 함수
# input: 판별기준, 행, 열
# output: 어느 사분면인지의 수
def get_quadrant(standard, row, column):
    if row >= standard:
        if column >= standard:
            return 4
        else: return 3
    else:
        if column >= standard:
            return 2
        else: return 1


result = 0
N, r, c = list(map(int, stdin.readline().split()))

# N이 1까지 감소하면서 반복
while N != 0:
    # 배열의 크기
    size = 2 ** N
    # 기준으로 쓰일 크기의 반
    half = int(size / 2)

    # 사분면 구하기
    quadrant = get_quadrant(half, r, c)

    # 지나온 수 구하여 result에 더하기
    if N == 1:
        num = (half ** 2) * (quadrant)
    else:
        num = (half ** 2) * (quadrant - 1)
    
    result += num

    # N 감소하면서 배열 쪼개기
    N -= 1
    if r >= half: r -= half
    if c >= half: c -= half

print(result - 1)