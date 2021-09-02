
def pl_or_pr(number):
    list_number = list(map(int, str(number)))
    result = 0
    
    idx = []
    for i in list_number:
        if i == 0:
            idx.append(0)
        else:
            idx.append(1)
    # idx.index(1)
    # 처음 숫자가 0일 때와 아닐때 지정
    # 처음 숫자가 0인 경우
    if list_number[0] == 0:
        # 처음 0이후 0이 아닌 처음 나온 값을 result에 저장
        result += list_number[idx.index(1)]
        # 그 이후 그 위치부터 끝까지 반복문 돌려서
        # 다음 숫자가 0이면 더하고 아니면 곱하기
        for i in range(idx.index(1), len(list_number)-1):
            if list_number[i+1] == 0:
                result += list_number[i+1]
            else:
                result *= list_number[i+1]
        return result
    
    # 처음 숫자가 0이 아닌경우 뒤에 수에 따라 바뀜
    else:
        result += list_number[0]
        for i in range(len(list_number)-1):
            if list_number[i+1] == 0:
                result += list_number[i+1]
            else:
                result *= list_number[i+1]
        return result

#         # 2, 3



# 0의 인덱스 찾기
# [0, x, x, 0, x, x]
# (((((0+x) * x) + 0) * x) * x)

# [0, 0, x, 0, x, x]

num = input()
print(pl_or_pr(num))



