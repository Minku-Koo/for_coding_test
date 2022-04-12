#뒷자리 9 될때까지 빼줌
def wh(num, digit):
    count = [0 for _ in range(10)]
    while True:
        count[int(num%10)] += 10**(digit)
        num = num // 10
        if (num == 0):
            break
    return count

count = [0 for _ in range(10)]
num = int(input())
digit = 0

while True:
    if num % 10 != 9:   # 맨 뒷자리가 9가 아닐경우 9가 될때까지 빼줌 (그동안 나오는 수 개수도 세줌)
        count = [wh(num, digit)[i]+count[i] for i in range(len(count))]
        num -= 1
    elif num % 10 == 9: # 맨 뒷자리가 9일경우
        temp = [(num//10)+1 for i in range(len(count))]
        temp[0] -= 1
        temp = [temp[i] * (10**(digit)) for i in range(len(count))]
        count = [temp[i] + count[i] for i in range(len(count))]
        num = num // 10
        digit += 1
    if num == 0:
        break
for i in count:
    print(i, end=' ')
