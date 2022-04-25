def move(y, x, dy, dx):
    count = 0
    while board[y+dy][x+dx] != '#' and board[y][x] != 'O':
        y += dy
        x += dx
        count += 1
    return (y, x), count

def check(b, r):
    if (b,r) in visited:
        return False

    return True

N, M = map(int, input().split(' '))

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

visited = {}                # key : ((by, bx), (ry, rx)), value : (count)
board= []
q = []

for i in range(N):
    temp = input()
    if 'B' in temp:
        Blue = (i, temp.index('B'))
    if 'R' in temp:
        Red = (i, temp.index('R'))
    if 'O' in temp:
        Goal = (i, temp.index('O'))
    board.append(temp)
visited[Blue, Red] = 0
q.append((Blue, Red))       #Blue (y, x)        Red (y, x)

while q:
    count = visited[q[0]]
    print(q)
    for i in range(4):
        tmpB, B_Count = move(q[0][0][0], q[0][0][1], dy[i], dx[i])
        tmpR, R_Count= move(q[0][1][0], q[0][1][1], dy[i], dx[i])

        if tmpB == tmpR:
            if B_Count > R_Count:
                tmpB = list(tmpB)
                tmpB[0] -= dy[i]
                tmpB[1] -= dx[i]
                tmpB = tuple(tmpB)
            else:
                tmpR = list(tmpR)
                tmpR[0] -= dy[i]
                tmpR[1] -= dx[i]
                tmpR = tuple(tmpR)

        if tmpR == Goal:
            if R_Count < B_Count:
                continue

        if check(tmpB, tmpR) and tmpB != Goal:
            q.append((tmpB, tmpR))
            visited[tmpB, tmpR] = count+1
    q.pop(0)

answer = list((visited.keys()))
answer = [i for i in answer if i[1] == Goal]
print(f'visited : {visited}')
if len(answer) > 0:

    c = min([visited[i] for i in answer])

    print(c)
else:
    print(-1)
