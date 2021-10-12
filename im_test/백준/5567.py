import sys
sys.stdin = open('5567.txt')
from collections import deque

N = int(input())
M = int(input())
# 상근이의 학번은 1
# 친구 & 친구의 친구까지!!!

friend = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    friend[a].append(b)
    friend[b].append(a)

def bfs():
    visited = [0] * (N+1)
    visited[1] = 1
    queue = deque()
    queue.append(1)

    while queue:
        x = queue.popleft()

        for i in friend[x]:
            if not visited[i]:
                visited[i] = visited[x] + 1
                queue.append(i)
    return visited

result = bfs()
cnt = 0
# print(result)
for f in result:
    if 2 <= f <= 3:
        cnt += 1
print(cnt)