## N자리 M진수 만들기
# 3자리 5진수
'''
000
001
002
003
004
010
011
...
444
'''
'''
# 1번 템플릿
# 완전탐색
n = int(input())
m = int(input())
data = [0]*n

# cur == 재귀의 깊이
def recur(cur):
    # 종료 조건!!
    if cur == n:
        print(data)
        return

    # 재귀호출부
    # 어떤 방법으로 재귀가 돌아가는지
    for i in range(m):
        data[cur] = i
        recur(cur+1)

recur(0)
'''


# 2번 템플릿
# nPm
# 순열 => 숫자에 중복은 없어야해!! but, 순서는 상관이없어
# 000, 101 -> 불가능
# 123, 321 -> 가능
n = int(input())
m = int(input())
data = [0]*n
visited = [False] * m

def recur(cur):
    # 종료 조건
    if cur == n:
        print(data)
        return

    for i in range(m):
        if visited[i] == True:
            continue

        visited[i] = True
        data[cur] = i
        recur(cur+1)
        visited[i] = False

recur(0)


'''
# 3번 템플릿
# 조합 => 중복도 불가능하고 순서도 상관이 있어!!
# nCm
# 어떤수든 3자리가 중복되면 결과는 불가능!!
# [1,2,3] => [3, 2, 1] 가능? X ==> 불가능 하나만 존재 가능!!
n = int(input())
m = int(input())
data = [0]*n

def recur(cur, start):
    # 종료 조건
    if cur == n:
        print(data)
        return

    # 재귀 호출부
    for i in range(start, m):
        data[cur] = i
        recur(cur+1, i+1)

recur(0, 0)
'''

# 4번 템플릿
# 조합!! => 횟수가 중요!!
# 쓴다 or 안쓴다
# append & pop

n = int(input())
m = int(input())
number = [1, 3, 5, 7, 9]
data = []

def recur(cur, cnt):
    # 종료조건 1
    if cnt == n:
        print(data)
        return

    # 종료조건 2
    if cur == m:
        return

    # 재귀호출부
    data.append(number[cur])
    recur(cur+1, cnt+1)
    data.pop()
    recur(cur+1, cnt)

recur(0, 0)