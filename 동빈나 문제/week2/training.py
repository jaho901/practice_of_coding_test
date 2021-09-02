def solution(n, lost, reserve):
    lost_1 = [l for l in lost if l not in reserve]
    reserve_1 = [r for r in reserve if r not in lost]

    print(lost_1, reserve_1)
    
    for r in reserve_1:
        if r-1 in lost_1:
            lost_1.remove(r-1)
        elif r+1 in lost_1:
            lost_1.remove(r+1)
                
    answer = n - len(lost_1)
    return answer
    


n1 = 5
n2 = 5
n3 = 3
lost1 = [2, 4]
lost2 = [2, 4]
lost3 = [3]
reserve1 = [1, 3, 5]
reserve2 = [3]
reserve3 = [1]
print(solution(n1, lost1, reserve1))
print(solution(n2, lost2, reserve2))
print(solution(n3, lost3, reserve3))














