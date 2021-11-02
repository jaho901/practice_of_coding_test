import sys
sys.stdin = open('input.txt')

N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]


def dfs(cur, total, i):
    global result

    if cur == N:
        if total > result:
            result = total
        return

    dfs(cur+1, total+data[cur][i], i)
    dfs(cur+1, total+data[cur][i+1], i+1)


result = 7
dfs(1, result, 0)
print(result)


