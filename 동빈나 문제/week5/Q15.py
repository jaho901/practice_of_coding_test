from collections import deque
import sys
sys.stdin = open('Q15.txt')

def bfs(x, k):
    queue = deque()
    visited[x] = 1
    queue.append(x)
    value = 0
    while k > 0:
        x = queue.popleft()
        for j in arr[x]:
            if visited[j] == 0:
                queue.append(j)
                visited[j] = 1
        if not queue:
            break
        if value in queue:
            pass
        else:
            value = queue[-1]
            k -= 1
    return queue

N, M, K, X = map(int, input().split())
arr = [[] for _ in range(N+1)]
for i in range(M):
    x, y = map(int, input().split())
    arr[x].append(y)
visited = [1] + [0]*N
result = bfs(X, K)
result = sorted(result)
if result:
    for i in result:
        print(i)
else:
    print(-1)

    

    
    