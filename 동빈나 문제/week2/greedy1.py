# 모험가 길드

# 2 3 1 2 2 4 2
# 7
# 4 3 2 1 / 2 2
# 1 / 2 2 / 3 2 2 -> 이게 답이겠네!!
# 1의 개수 = a1 / 2의 개수 = a2 / 3의 개수 = a3 / 4의 개수 = a4
# a1의 개수를 모두 포함
# a2의 개수를 2로 나눈 몫을 포함, 나머지는 a3한테 기부
# a3의 개수 + a2의 나머지를 3으로 나눈 몫을 포함 나머지 a4에 기부
# a4의 개수 + a3의 나머지 ==> 존재하면 몫만 포함, 아니면 0

# 1 2 2 2 2 2 3 3 4 => 결과가 1 / 2 2 / 2 2 / 2 3 3 (4) / 로 4가 나와야함

# [1 5 2 1]
# 몫 = [1 2 0 0]
# 나 = [0 1 2 1]


def adventure(N, number):
    answer = []
    share = []
    rest = []
    result = 0

    number_list = list(map(int, number.split()))

    # 각각의 개수 분포 확인
    for i in range(1, N+1):
        answer.append(number_list.count(i))
    
    # 몫 구하기 -> 몫의 모든 값을 전부 result에 더하기
    for i in range(len(number_list)):
        share.append(answer[i]//(i+1))
    result += sum(share)

    # 나머지 구하기 -> 나머지를 계속 이월시키기
    for i in range(len(number_list)):
        rest.append(answer[i]%(i+1))
    
    # 이월시키는기
    for i in range(len(rest)-1):
        if rest[i]//(i+1) < 1:
            rest[i+1] += rest[i]
            rest[i] = 0
    for i in range(len(rest)):
        if rest[i]//(i+1) >= 1:
            result += rest[i]//(i+1)
        


    return result



a = int(input())
b = input()
print(adventure(a, b))













