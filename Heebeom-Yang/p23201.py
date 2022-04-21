

# 배열에서 가장 큰 원소, 작은 원소의 차를 비교
# 해당 값이 기준(standard) 이하이면 True
def get_diff(arr):
    max_val = max(arr)
    min_val = min(arr)
    return (max_val - min_val)


# 배열에서 가장 작은 원소들에 1 더해주기
def step_one(arr):
    min_val = min(arr)

    for idx in range(len(arr)):
        if arr[idx] == min_val:
            arr[idx] += 1
    return arr


# 배열의 가장 왼쪽에 있는 수를 위로 올리기
def step_two(arr):
    result = []
    temp = [arr[0]]
    arr.pop(0)

    for _ in range(len(arr) - 1):
        temp.append(0)
    result.append(temp)
    temp = []
    for element in arr:
        temp.append(element)

    result.append(temp)

    return result


# 어항 쌓기
def step_three(arr):
    iters = 0
    while iters < 3:
        divide = []
        remain = []
        result = []

        # 나눌부분 검사
        for r in range(len(arr[0])):
            temp = []
            for i in range(len(arr)):
                if arr[i][r] != 0:
                    temp.append(arr[i][r])
            if len(temp) >= 2:
                divide.append(temp)
            else:
                remain.append(temp)

        # 나눈부분 위로 올리기
        for pair in divide:
            temp = []
            pair.reverse()
            for element in pair:
                temp.append(element)
            for _ in range(len(remain) - len(pair)):
                temp.append(0)
            result.append(temp)

        # 남은부분 맨 아래쪽에 추가
        temp = []
        for pair in remain:
            for element in pair:
                temp.append(element)
        result.append(temp)

        # 첫번째열보다 맨 밑줄이 작으면 끝
        if len(remain) < len(divide[0]):
            return arr
        # 아니면 결과저장하고 진행
        arr = result


# 물고기 분배하기
def step_four(arr):
    weight_arr = []

    # arr 크기의 증감배열 선언
    for line in arr:
        temp = []
        for element in line:
            if element != 0:
                temp.append(0)
        weight_arr.append(temp)

    # 배열 가로탐색해서 증감배열에 넣기
    for i in range(len(weight_arr)):
        line_size = len(weight_arr[i])
        for r in range(line_size):
            if r < (line_size - 1):
                element = arr[i][r]
                next_elm = arr[i][r + 1]
                diff = abs(next_elm - element)
                mod = diff // 5

                if mod > 0:
                    if element > next_elm:
                        weight_arr[i][r] -= mod
                        weight_arr[i][r + 1] += mod
                    else:
                        weight_arr[i][r] += mod
                        weight_arr[i][r + 1] -= mod

    # 배열 세로탐색해서 증감배열에 넣기
    for r in range(len(arr[0])):
        line_size = len(arr)
        for i in range(line_size):
            if i < (line_size - 1):
                element = arr[i][r]
                next_elm = arr[i + 1][r]

                # 0 끼어있으면 그냥 지나치기
                if element == 0 or next_elm == 0:
                    continue

                diff = abs(next_elm - element)
                mod = diff // 5

                if mod > 0:
                    if element > next_elm:
                        weight_arr[i][r] -= mod
                        weight_arr[i + 1][r] += mod
                    else:
                        weight_arr[i][r] += mod
                        weight_arr[i + 1][r] -= mod

    for i in range(len(weight_arr)):
        line_size = len(weight_arr[i])
        for r in range(line_size):
            arr[i][r] += weight_arr[i][r]

    return arr


# 배열 일자로 펴기
def step_five(arr):
    flat_arr = []
    result = []
    for r in range(len(arr[0])):
        temp = []
        line_size = len(arr)
        for i in range(line_size):
            elm = arr[i][r]
            if elm != 0:
                temp.append(elm)
        temp.reverse()
        flat_arr.append(temp)

    for pair in flat_arr:
        for elm in pair:
            result.append(elm)

    return result


# 배열 두번 접기
def step_six(arr):
    pivot = len(arr) // 2
    result = []

    # 첫번째 접기
    left_arr = arr[:pivot]
    right_arr = arr[pivot:]
    arr = []
    left_arr.reverse()
    arr.append(left_arr)
    arr.append(right_arr)

    pivot = len(arr[0]) // 2
    # 두번째 접기
    divide = []
    remain = []

    for i in range(len(arr)):
        left_arr = arr[i][:pivot]
        right_arr = arr[i][pivot:]

        divide.append(left_arr)
        remain.append(right_arr)

    divide.reverse()
    for pair in divide:
        pair.reverse()
        result.append(pair)

    for pair in remain:
        result.append(pair)

    return result


arr = []
N, K = map(int, input().split())

init_elements = map(int, input().split())
# 초기 원소 입력하기
for element in init_elements:
    arr.append(element)

result = 0

while True:
    arr = step_one(arr)
    arr = step_two(arr)
    arr = step_three(arr)
    arr = step_four(arr)
    arr = step_five(arr)
    arr = step_six(arr)
    arr = step_four(arr)
    arr = step_five(arr)
    result += 1

    diff = get_diff(arr)
    if diff <= K:
        break

print(result)