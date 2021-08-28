import sys
sys.stdin = open('2491.txt')
# 재귀로 run time error가 났을 때 주어주는 코드
sys.setrecursionlimit(10**6)

# 재귀 코드 (내가 재미로 풀어본것! 밑에 직관적 코드로 확인!!)
# 오름차순 확인 재귀
def recur_inc(cur = 0, result = 0):
    global ans_inc

    # 바로 다음나올 값과 비교하기 때문에 N-1로 지정
    if cur == N-1:
        # cur이 N-1인 경우의 result+1값과 ans_inc와의 max값 비교
        ans_inc = max(result + 1, ans_inc)
        return
    # 오름차순인 경우
    if data[cur] <= data[cur+1]:
        recur_inc(cur+1, result+1)
    # 아닌 경우
    else:
        ans_inc = max(result+1, ans_inc)
        recur_inc(cur+1, 0)

# 내림차순인 경우
def recur_dec(cur = 0, result = 0):
    global ans_dec

    if cur == N-1:
        ans_dec = max(result + 1, ans_dec)
        return

    if data[cur] >= data[cur+1]:
        recur_dec(cur+1, result+1)
    else:
        ans_dec = max(result+1, ans_dec)
        recur_dec(cur+1, 0)

N = int(input())
data = list(map(int, input().split()))

ans_inc = 0
ans_dec = 0
recur_inc(0, 0)
recur_dec(0, 0)
# recur함수 2개를 실행시켜줌으로써 ans_inc, ans_dec값이 변경되었을 것이다.
print(max(ans_inc, ans_dec))


# 직관적 코드
'''
n = int(input())
arr = list(map(int, input().split()))

# 모든 값들은 현재있는 위치에서 1의 값을 가진다.
asc, des = 1, 1
ans = 1

for i in range(1, n):
    # 오름차순인 경우 asc에 +1씩
    if arr[i] >= arr[i - 1]:
        asc += 1
    # 아닌 경우 다시 asc를 1로 시작
    else:
        asc = 1

    # 내림차순인 경우 dex에 +1씩
    if arr[i] <= arr[i - 1]:
        des += 1
    # 아닌 경우 다시 des를 1로 시작
    else:
        des = 1

    # i값이 달라질때마다 계속해서 최댓값을 갱신시켜준다.
    ans = max(ans, asc, des)

print(ans)
'''