import heapq

N, M = map(int, input().split(' '))

degree = [0 for i in range(N+1)]
info = {}
heap = []
answer = []

for i in range(M):
    A, B = map(int, input().split(' '))
    
    if A in info:
        info[A] = info[A] + [B]
    else:
        info[A] = [B]
    degree[B] += 1

for i, d in enumerate(degree):
    if d == 0:
        heapq.heappush(heap, i)

while heap:
    temp = heapq.heappop(heap)
    if temp in info:
        for i in info[temp]:
            degree[i] -= 1
            if degree[i] == 0:
                heapq.heappush(heap, i)
    answer.append(temp)

answer = map(str, answer[1:])
print(" ".join(answer))