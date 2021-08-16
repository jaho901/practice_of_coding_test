## 1946
# 신입사원

'''
import sys

tc = int(sys.stdin.readline().rstrip())
for i in range(tc):
    n = int(sys.stdin.readline().rstrip())
    arr = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
    
    arr.sort()

    cnt = 1
    temp = arr[0][1]
    for j in range(1,len(arr)):
       if arr[j][1] < temp:
           temp = arr[j][1]
           cnt += 1
    
    print(cnt)
'''
'''
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    apply = []
    for i in range(N):
        a = list(map(int, input().split()))
        apply.append(a)
'''



'''
    apply = sorted(apply, reverse=T)

    interview = []
    for i in apply:
        interview.append(i[1])

    result = 0
    for i in range(len(interview)):
        minimum = min(interview[i:])
        if interview[i] == minimum:
            result += 1
    print(result)
'''
    ## 포기


'''
    result = []
    for i in range(len(apply)):
        minimum_1 = apply[i][1]
        for j in range(i+1, len(apply)):
            if minimum_1 > apply[j][1]:
                minimum_1 = apply[j][1]
        if apply[i][1] == minimum_1:
            result.append(apply[i])
        else:
            pass
    
    print(len(result))
    '''




'''
    for i in range(len(apply)):
        for j in range(len(apply)):
            if apply[i][0] < apply[j][0] and apply[i][1] < apply[j][1]:
                apply[j] = [N+1, N+1]
    # print(apply)

    result = []
    for i in range(len(apply)):
        if apply[i] != [N+1, N+1]:
            result.append(i)

    print(len(result))
'''
 

    


## 10819

N = int(input())
number = list(map(int, input().split()))
number.sort()

result = []
i = 0
j = 1
k = len(number)//2

while k != 0:
    lenght = [0, len(result)+2]

    result.insert(lenght[i], number[-1])
    number.remove(number[-1])
    result.insert(lenght[j], number[0])
    number.remove(number[0])

    i = (i + 1) % 2
    j = (j + 1) % 2
    k -= 1

if len(number)%2 != 0:
    if abs(number[0] - result[0]) > abs(number[0] - result[-1]):
        result.insert(0, number[0])
    else:
        result.insert(len(result)+1, number[0])

    
summ = 0
for i in range(len(result)-1):
    summ += abs(result[i+1] - result[i])

print(summ)




