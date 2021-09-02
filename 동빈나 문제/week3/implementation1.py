def solution(N_list):
    if len(N_list)%2 == 0:
        n = len(N_list)//2
        sum_front = sum(N_list[0:n])
        sum_back = sum(N_list[n:])

    if sum_front == sum_back:
        return "LUCKY"
    else:
        return "READY"


N_list = list(map(int, input()))
print(solution(N_list))













