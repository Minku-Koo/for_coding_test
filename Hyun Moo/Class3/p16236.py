def findFish():
    info = []
    for i in range(N):
        for j in range(N):
            if board[i][j] < size and board[i][j] > 0 and board[i][j] < 9:
                info.append((i,j))
            elif board[i][j] == 9:
                q.append((i, j))
    return info

def findDP():
    visited = {}
    while q:
        y, x = q.pop(0)
        temp = []
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            print(q)
            if ny >= 0 and ny < N and nx >= 0 and nx < N:
                if board[ny][nx] == 0:
                    if dp[ny][nx] == 0 and (ny, nx) not in visited:
                        q.append((ny, nx))
                        visited[(ny,nx)] = 1
                    elif dp[ny][nx] != 0:
                        temp.append(dp[ny][nx])
                if len(temp) > 0 and board[y][x] != 9:
                    dp[y][x] = min(temp) + 1

    print(visited)
q = []
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
N = int(input())
board = []
size = 2
eat = 0
dp = [[0 for i in range(N)]] * N


for i in range(N):
    temp = list(map(int, input().split(' ')))
    board.append(temp)

info = findFish()
findDP()
print(dp)
