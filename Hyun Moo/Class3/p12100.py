N = int(input())
board = []

for i in range(N):
    temp = list(map(int, input().split(' ')))
    board.append(temp)

print(board)