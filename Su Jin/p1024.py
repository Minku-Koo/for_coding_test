def find_point(array, n, a, l):

    #등차수열의 합
    result = int(l * (2*a + (l-1))/2) 

    #이미 계산된적이 있으면 -1반환
    if (result in array):
        return -1, -1

    #계산된 결과값 배열에 넣기
    array += [result]
    
    #결과값 반환
    if result == n:
        return a, l
    #결과값에 따라 첫째항(시작숫자)을 더하거나 뺌
    elif(result > n):
        return find_point(array,n, a-1, l)
    else:
        return find_point(array,n,a+1,l)


n, l = map(int,input().split())

#리스트의 최대개수 100개
for i in range(l,101):
    a = int(n/i)
    array = list()
    point,repeat = find_point(array, n, a, i)
    if point == -1:
        continue
    else:
        break

if point < 0: print(-1)
else:
    for _ in range(repeat):
        print(point, end = " ")
        point += 1