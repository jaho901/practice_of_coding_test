def solution(food_times, k):
    
    k = int(k)
    result = 0
    length = len(food_times)
       
    while k > 0:
        if food_times[result] > 0:
            food_times[result] -= 1
            
            result += 1
            if result == length:
                result = 0
            k -= 1

        # 0 2번 만난 경우 넘어가는 것만 해결하면 끝
        elif food_times[result] == 0:
            result += 1
            if result == length:
                result = 0
            next

    idx = []
    for i in food_times:
        if i == 0:
            idx.append('0')
        else:
            idx.append('1')
        
    if sum(food_times) == 0:
        return -1
    
    else:
        if result == length:
            return idx.index('1')
        else:
            return result + 1


a = [3, 1, 2]
a1 = [5, 2, 3, 6]
b = 5
b1 = 11
print(solution(a, b))
print(solution(a1, b1))
    


# [5, 2, 3, 6]  # 11번을 먹자
# 1. 4236
# 2. 4136
# 3. 4126
# 4. 4125
# 5. 3125
# 6. 3025
# 7. 3015
# 8. 3014
# 9. 2014
# 10. 2004
# 11. 2003

    