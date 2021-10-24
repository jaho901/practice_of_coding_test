import sys
sys.stdin = open('4871.txt')

T = int(input())
for tc in range(1, T+1):
    v, e = map(int, input().split())
    node = [[] for _ in range(v+1)]

    for _ in range(e):
        a, b = map(int, input().split())
        node[a].append(b)
        node[b].append(a)
    print(node)

    start, end = map(int, input().split())
    q = []
    visited = [-1] * (v+1)
    result = 0

    def bfs(start):
        global result

        q.append(start)
        visited[start] = 0

        # while
        while q:
            x = q.pop(0)

            for i in node[x]:
                if visited[i] == -1:
                    visited[i] = visited[x] + 1
                    q.append(i)

    bfs(start)
    print(visited[end])


'''
    def dfs(cur, s):
        global result

        # 종료 조건
        if cur == v:
            return
        
        if s == end:
            result = 1
            return

        # 재귀호출부
        for i in node[s]:
            if visited[i] == False:
                visited[i] = True
                dfs(cur+1, i)
    dfs(0, start)


    arr = []
    def dfs(cur, s):
        global result

        # 종료 조건
        if cur == v:
            return

        # 재귀호출부
        for i in node[s]:
            if visited[i] == False:
                visited[i] = True
                arr.append(i)
                dfs(cur+1, i)
    dfs(0, start)
    if end in arr:
        result = 1


    print('#{} {}'.format(tc, result))
'''