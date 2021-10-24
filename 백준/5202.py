import sys
sys.stdin = open('5202.txt')

n, m, s = map(int, input().split())
node = [[] for _ in range(n+1)]
# print(node)
for _ in range(m):
    u, v = map(int, input().split())
    node[u].append(v)
print(node)

result = []
visited = [False] * (n+1)
visited[s] = True
result.append(s)

def dfs(cur, start):
    global result

    if cur == n:
        return

    for i in node[start]:
        if visited[i] == False:
            visited[i] = True
            result.append(i)
            dfs(cur+1, i)

dfs(0, s)
print(result)