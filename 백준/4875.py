import sys
sys.stdin = open('4875.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    
    # 출발점, 도착점 지정
    s_x, s_y = 0, 0
    e_x, e_y = 0, 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 3:
                s_x= i
                s_y = j
            if arr[i][j] == 2:
                e_x = i
                e_y = j

    # 방향벡터
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    # 방문목록
    visited = [[0]*N for _ in range(N)]
    # 최종 결과
    result = 0

    def dfs(s_x, s_y):
        global result

        # 종료 조건
        if s_x == e_x and s_y == e_y:
            result = 1
            return
        
        # 재귀호출부
        for k in range(4):
            nx, ny = s_x + dx[k], s_y + dy[k]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
                if arr[nx][ny] == 0 or arr[nx][ny] == 2:
                    visited[nx][ny] = 1
                    dfs(nx, ny)
    
    dfs(s_x, s_y)
    print(result)