

def solution(N, coin):
    N = int(N)
    coin = list(map(int, coin.split()))
    coin.sort()

    result = 1
    for i in coin:
        # coin에서 가장 작은 수보다 1이 작으면 1 반환
        # 그 이외에는 가장 작은 수부터 하나씩 더하기
        if result < i:
            break
        else:
            result += i

    return result


'''
    # 모든 경우의 수 어떻게 할까...
    # 1 1 2 3 9
    # 1+1 1+2 1+3 1+9
    # 1+2 1+3 1+9
    # 2+3 2+9
    # 3+9

    result = [i for i in coin]

    for i in range(len(coin)):
        for j in range(i+1, len(coin)):
            result.append(coin[i] + coin[j])

    result.sort()
    result = set(result)


    # 너무 무수히 많아질거같아...

    return result
'''

    

a = input()
b = input()
print(solution(a, b))


