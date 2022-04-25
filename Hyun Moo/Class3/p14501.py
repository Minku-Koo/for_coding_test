N = int(input())
T = []
P = []
dp = [0 for i in range(N+1)]
m = 0

for i in range(N):
    temp = list(map(int, input().split(' ')))
    T.append(temp[0])
    P.append(temp[1])

for i in range(N):
    m = max(m, dp[i])
    if i+T[i] > N:
        continue
    dp[i+T[i]] = max(m+P[i], dp[i+T[i]])

print(max(dp))