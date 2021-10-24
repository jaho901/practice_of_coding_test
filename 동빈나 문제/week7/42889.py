
N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
'''
N = 4
stages = [4, 4, 4, 4, 4]
'''

def solution(N, stages):
    number = [0] * (N+1)
    result = [[0, i] for i in range(1, N+1)]
    length = len(stages)
    for i in range(length):
        idx = stages[i]
        if len(number) > idx:
            number[idx] += 1
    # print(number)
    i = 0
    while i < N:
        if number[i+1] == 0:
            result[i][0] = 0
        else:
            result[i][0] = number[i+1]/length
            length -= number[i+1]
        i += 1
    result = sorted(result, key=lambda x:-x[0])
    # print(result)
    total = [0]*(N)

    for i in range(len(result)):
        if result[i][1] != 0:
            total[i] = result[i][1]
    return total


print(solution(N, stages))


