N = int(input())
temp = []

for i in range(N):  #입력받기
    a, b = map(int,input().split(' '))
    temp.append([a,b])

temp.sort(key=lambda x:x[0])    # 정렬

l = [i[1] for i in temp]
dp = [1 for i in range(len(l))]

for i in range(1, len(dp)):
    temp = [j for j in l[:i] if j<l[i]] #현재 숫자보다 작은 숫자 배열
    if temp:    #temp 에 값이 있을때만
        dp[i] = max([dp[l.index(j)] for j in temp]) + 1 #현재 숫자보다 작은숫자중 dp최댓값 + 1

print(len(dp)-max(dp))