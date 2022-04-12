node = int(input())
edge = int(input())

info = []
q = [0]
visited = [0 for _ in range(node)]
infection = [0 for _ in range(node)]

for i in range(edge):
    temp = input()
    temp = temp.split(" ")
    temp = list(map(int, temp))
    temp[0], temp[1] = temp[0]-1, temp[1]-1
    temp.sort()
    info.append(temp)

temp = []

while q:
    temp = [i[1] if q[0] == i[0] else i[0] for i in info if q[0] in i]

    if len(temp) > 0:
        for i in temp:
            if visited[i] == 0:
                visited[i] = 1
                infection[i] = 1
                q.append(i)
    q.pop(0)
print(infection.count(1)-1)