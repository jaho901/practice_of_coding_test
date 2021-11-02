def recur(cur = 0, total = 0):
    global ans
    # ans = 0
    if cur == N:
        ans = max(ans, total)
        return

    if cur > N:
        return

    # 이번 재귀에서는 일을 하지 않고 그냥 넘어간다.
    recur(cur + 1, total)
    # 이번 재귀에서는 일을 처리하고, 기간도 점프한다.
    recur(cur + data[cur][0], total + data[cur][1])



N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]

ans = 0
recur(0, 0)
print(ans)