n = int(input())
dp = [1] * n
array = []
#2차원배열로 입력받기
for _ in range(n):
     a, b = map(int,input().split())
     array.append([a,b])
#첫번재 전기줄 기준으로 정렬
array = sorted(array, key=lambda x:x[0])

#정렬된 전기줄쌍에서 두번째 전기줄은 LIS(11053 가장 긴 증가하는 부분수열)를 사용하여 개수세기
for i in range(1,n):
    for j in range(0,i):
        if array[j][1] <= array[i][1]:
            dp[i] = max(dp[i], dp[j]+1)

#빼야하는 전기줄 = 원래 전기줄 개수 - 최대로 이을 수 있는 전기줄 
result = n - max(dp)
print(result)

