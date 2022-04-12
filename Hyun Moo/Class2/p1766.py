N, M = map(int, input().split(' '))

degree = [0 for i in range(N+1)]
visited = [0 for i in range(N+1)]
info = {}
q = []
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
        q.append(i)
        visited[i] = 1

while q:
    if q[0] in info:
        visited[q[0]] = 1
        for i in info[q[0]]:
            degree[i] -= 1   
        answer.append(q.pop(0))

    else:
        visited[q[0]] = 1
        answer.append(q.pop(0))
    for i, d in enumerate(degree):
        if d == 0 and visited[i] == 0:
            q.append(i)
            visited[i] = 1
            
answer = map(str, answer[1:])
print(" ".join(answer))