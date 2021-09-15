# import sys
# sys.stdin = open('input.txt')
# sys.setrecursionlimit(10**6)
'''
id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2
id_list = ["con", "ryan"]
report = ["ryan con", "ryan con", "ryan con", "ryan con"]
k = 3

def solution(id_list, report, k):
    N = len(id_list)
    stop = [[] for _ in range(len(id_list))]
    cnt = [0] * N
    result = [0] * N
    report = list(set(report))

    for i in range(len(report)):
        x, y = report[i].split()
        stop[id_list.index(x)].append(y)
        cnt[id_list.index(y)] += 1

    for j in range(len(cnt)):
        if cnt[j] >= k:
            for i in range(len(stop)):
                if id_list[j] in stop[i]:
                    result[i] += 1

    return result
'''


n = 437674
k = 3
# n = 110011
# k = 10

def solution(n, k):
    answer = 0
    num = []
    while n != 0:
        num.insert(0, n % k)
        n = n//k

    result = []
    sub = []
    for i in range(len(num)):
        if 0 < i < len(num)-1 and num[i] == 1 and num[i+1] == 0 and num[i-1] == 0:
            sub = []
        elif i == 0 and num[i] == 1 and num[i+1] == 0:
            sub = []
        elif i == len(num) - 1 and num[i] == 1 and num[i-1] == 0:
            sub = []
        elif num[i] != 0:
            sub.append(num[i])
        else:
            if sub:
                result.append(int(''.join(map(str, sub))))
                sub = []
    result.append(int(''.join(map(str, sub))))

    for j in result:
        exist = False
        for x in range(2, j):
            if x * x > j:
                break

            if j % x == 0:
                exist = True

        if not exist:
            answer += 1

    return answer

print(solution(n, k))


'''
#
# fees = [180, 5000, 10, 600]
# records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
# fees = [120, 0, 60, 591]
# records = ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]
# fees = [1, 461, 1, 10]
# records = ["00:00 1234 IN"]


def solution(fees, records):
    car = []
    for i in records:
        t, c, io = i.split()
        if c not in car:
            car.append(c)
    car = sorted(car)
    time = [0] * len(car)
    exist = [False] * len(car)

    for i in records:
        t, c, io = i.split()
        idx = car.index(c)
        if io == 'IN':
            time[idx] += -(int(t[:2])*60 + int(t[3:]))
            exist[idx] = True
        elif io == 'OUT':
            time[idx] += (int(t[:2])*60 + int(t[3:]))
            exist[idx] = False

    for i in range(len(exist)):
        if exist[i]:
            time[i] += (23*60 + 59)

    result = [0] * len(car)
    for j in range(len(time)):
        if time[j] >= fees[0]:
            result[j] += fees[1]
            time[j] -= fees[0]
            if time[j] % fees[2] == 0:
                result[j] += fees[3] * (time[j] // fees[2])
            else:
                result[j] += fees[3] * ((time[j] // fees[2]) + 1)
        else:
            result[j] = fees[1]

    return result

print(solution(fees, records))
'''

'''
n = 5
info = [2,1,1,1,0,0,0,0,0,0,0]
# n = 1
# info = [1,0,0,0,0,0,0,0,0,0,0]
# n = 9
# info = [0,0,1,2,0,1,1,1,1,1,1]
# n = 10
# info = [0,0,0,0,0,0,0,0,3,4,3]

def solution(n, info):
    answer = 0
    result = []
    exist = False
    for i in range(10):
        info_2 = [0] * 11
        m = n
        for j in range(i, 10):
            if m >= info[j] + 1:
                info_2[j] = info[j] + 1
                m -= info[j] + 1
            else:
                if j == 10:
                    info_2[j] += m
                    m = 0
            if m == 0:
                peach, lion = 0, 0
                for k in range(10):
                    if info[k] == 0 and info_2[k] == 0:
                        continue
                    elif info[k] >= info_2[k]:
                        peach += (10-k)
                    elif info[k] < info_2[k]:
                        lion += (10-k)

                if answer < (lion - peach):
                    answer = lion - peach
                    result = info_2
                    exist = True
                else:
                    continue
                break

    if exist:
        return result
    else:
        return [-1]


print(solution(n, info))
'''

'''
board = [[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]]
skill = [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]
# board = [[1,2,3],[4,5,6],[7,8,9]]
# skill = 	[[1,1,1,2,2,4],[1,0,0,1,1,2],[2,2,0,2,0,100]]

def solution(board, skill):
    answer = 0
    for k in skill:
        for x in range(k[1], k[3] + 1):
            for y in range(k[2], k[4] + 1):
                if k[0] == 1:
                    board[x][y] -= k[5]
                elif k[0] == 2:
                    board[x][y] += k[5]

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] > 0:
                answer += 1

    return board

print(solution(board, skill))
'''


'''
info = [0,0,1,1,1,0,1,0,1,0,1,1]
edges = [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]
# info = [0,1,0,1,1,0,1,0,0,1,0]
# edges = [0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]

arr = [[0]*18 for _ in range(18)]
for i in edges:
    arr[i[0]][i[1]] = arr[i[1]][i[0]] = 1
ans = 0

def recur(s=0, total=0):
    global ans
    visited = [0] * 18
    i = s
    visited[i] = 1

    ans = max(ans, total)

    while True:
        for k in range(len(visited)):
            if total >= 1:
                if arr[i][k] == 1 and visited[k] == 0:
                    i = k
                    visited[i] = 1
                    if info[k] == 0:
                        recur(i, total + 1)
                    else:
                        recur(i, total - 1)
            else:
                pass
        return

recur(0, 0)
print(ans)
'''






















