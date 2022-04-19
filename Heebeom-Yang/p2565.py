from sys import stdin

# 간선 수 입력받기
link_num = int(stdin.readline())

# 간선 정보를 담을 배열 생성
link_list = []

# 간선 정보 입력받기
for _ in range(link_num):
    start, end = list(map(int, stdin.readline().split()))
    link_list.append((start, end))

# Start 기준으로 배열을 정렬하고, End로만 배열을 구성하기
link_list.sort()
arr = [second for _, second in link_list]

# 최장증가수열을 찾기 위해 DP 결과값을 담을 배열 생성
dp = [1] * link_num

# DP 계산하기
for i in range(1, link_num):
    for j in range(0, i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j] + 1)

# DP 테이블 중 가장 큰 값이 최장증가수열
result = max(dp)

# 총 간선의 수 - 연결가능한 간선 수 = 최소한으로 제거해야할 간선 수
print(link_num - result)