def solution(N, L):
    answer = []
    for i in range(L, 101):
        cons = [x for x in range(1, i)]
        cons = sum(cons)

        if (N - cons) % i != 0:
            continue
        else:
            for j in range(int((N-cons) / i), int((N-cons) / i) + i):
                answer.append(j)

            if sum(answer) != N:
                answer = []
                continue

            if answer[0] < 0:
                answer = [-1]
            
            return answer
    return [-1]

info = input()
N = int(info.split(" ")[0])
L = int(info.split(" ")[1])

answer = solution(N, L)

for i in answer:
    print(f"{i} ", end="")