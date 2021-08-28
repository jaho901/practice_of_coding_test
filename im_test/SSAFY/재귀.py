```python
# 1번 템플릿 (완전탐색)
# n자리 m진수
n = int(input())
m = int(input())
arr = [0] * n

def recur(cur): # cur => 재귀깊이 (보통 인덱스랑 매칭이됨)
    if cur == n: #종료조건, 행동을해 (없으면 재귀가 안끝나 재귀깊이 1000 recursion에러)
        print(arr)
        return
    
    #여기서는 이제 내가 뭘 할지 재귀호출부
    for i in range(m):
        arr[cur] = i
        recur(cur + 1)

recur(0)
#############################################################
# 순열 n자리 m진수인데 숫자중복이 없어 (순서는 의미가 있다)
# 000 001 002
# 012 013 014 021 023 024 031 032 034

n = int(input())
m = int(input())
arr = [0] * n
visited = [False] * m  # 방문처리를 한다

def recur(cur): # cur => 재귀깊이 (보통 인덱스랑 매칭이됨)
    if cur == n: # 기저 종료조건, 행동을해 (없으면 재귀가 안끝나 재귀깊이 1000 recursion에러)
        print(arr)
        return
    
    #여기서는 이제 내가 뭘 할지 재귀호출부
    for i in range(m):
        if visited[i]:
            continue

        visited[i] = True
        arr[cur] = i
        recur(cur + 1)
        visited[i] = False

recur(0)

# 어떤 문제가 나왔어
# 그 문제를 이 템플릿들중에 하나로 변형을 시킬수가 있어
# 1(완탐) 2(순열) 3(조합) 4(조합)
##############################################################
n = int(input())
m = int(input())
arr = [0] * n

def recur(cur, start): # cur => 재귀깊이 (보통 인덱스랑 매칭이됨)
    if cur == n: #종료조건, 행동을해 (없으면 재귀가 안끝나 재귀깊이 1000 recursion에러)
        print(arr)
        return
    
    #여기서는 이제 내가 뭘 할지 재귀호출부
    for i in range(start, m):
        arr[cur] = i
        recur(cur + 1, i+1)

recur(0, 0)
# 3번템플릿 조합
# 순열 012 013 014 021 023 024 031 032 034 041 042 043
# 순열 012 013 014 023 024 034 -> (순서까지 다 제거하려면)오름차순 으로 만들어

##################################################################################
#4번템플릿 조합
# n자리 m진수
n = int(input())
m = int(input())
arr = []

# 쓴다 안쓴다
def recur(cur, cnt): #cur = 0
    if cnt == n: # 숫자를 n번쓰면 여기서 걸려 cnt는 내가 숫자를 쓸때마다 1씩늘리니까 5개를 다 썼어? 그럼 출력
        for i in range(n):
            print(arr[i], end ='')
        print('')
        return

    if cur == m: #cur은 깊이인 동시에 그 사용할 숫자를 의미
        return

    arr.append(cur)
    recur(cur + 1 , cnt + 1) # 쓴다
    arr.pop() 
    recur(cur + 1 , cnt) # 안쓴다

recur(0, 0)
