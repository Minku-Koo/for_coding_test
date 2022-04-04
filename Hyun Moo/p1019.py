def wh(num, count):
    while (num//10 > 0):
        count[int(num%10)] += 1
        num = num // 10

    return count

count = [0 for _ in range(10)]

