from sys import stdin
import heapq

# 문제 개수, 짝 개수 입력받기
problem_num, pair_num = list(map(int, stdin.readline().split()))

# 진입차수를 담을 배열
indegree = [ 0 for _ in range(problem_num + 1) ]
indegree[0] = -1

# 간선 정보를 담을 배열
link_table = [ [] for _ in range(problem_num + 1) ]

# 최소 힙
min_heap = []

# 정답을 담을 배열
answer = []

# 짝 개수만큼 입력받기
for _ in range(pair_num):
    a, b = list(map(int, stdin.readline().split()))
    # 진입차수 입력
    indegree[b] += 1
    # 간선정보 입력
    link_table[a].append(b)


for idx, val in enumerate(indegree):
    # 진입차수가 0인 원소 최소 힙에 입력
    if val == 0:
        heapq.heappush(min_heap, idx)

# 최소 힙이 다 빌때까지 진행
while len(min_heap) != 0:
    # 최소 힙에서 pop한다음 정답 배열에 추가
    element = heapq.heappop(min_heap)
    answer.append(element)

    # 간선 정보 불러오기
    links = link_table[element]
    for link in links:
        # 연결된 간선들의 진입차수를 -1
        indegree[link] -= 1
        # 만약 진입차수 0됬으면 최소 힙에 추가
        if indegree[link] == 0:
            heapq.heappush(min_heap, link)

for i in answer:
    print(i, end=' ')