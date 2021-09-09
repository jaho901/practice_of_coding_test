
T = int(input())
for _ in range(1, T+1):
    N, M = map(int, input().split())
    data = list(map(int, input().split()))
    cake = []
    sub = []
    result = 0
    for i in range(len(data)):
        if data[i] == 10:
            result += 1
        elif data[i] != 10 and data[i]%10 == 0:
            cake.append(data[i])
        else:
            sub.append(data[i])
    cake = sorted(cake) + sub
    # print(cake)
    if cake:
        for j in range(len(cake)):
            if cake[j]%10==0:
                k = cake[j] // 10
                if k <= M+1:
                    result += k
                    M -= k-1
                else:
                    result += M
                    break
            else:
                k = cake[j] // 10
                if k <= M:
                    result += k
                    M -= k
                else:
                    result += M
                    break
            if M == 0:
                break
        print(result)
    else:
        print(result)






'''
# 완탐으로 풀기!!!
T = int(input())
for _ in range(1, T+1):
    N, M = map(int, input().split())
    data = list(map(int, input().split()))
    cake = []
    sub = []
    result = 0
    for i in range(len(data)):
        if data[i] == 10:
            result += 1
        elif data[i] != 10 and data[i]%10 == 0:
            cake.append(data[i])
        else:
            sub.append(data[i])
    cake = sorted(cake) + sub

    if cake:
        while M > 0:
            for i in range(len(cake)):
                while cake[i] > 10:
                    cake[i] -= 10
                    M -= 1
                    result += 1
                    if cake[i] == 10:
                        result += 1
                        break
                    if M == 0:
                        break
                if M == 0:
                    break
        print(result)
    else:
        print(result)
'''