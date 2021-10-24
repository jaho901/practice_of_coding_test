N, K = map(int, input().split())
virus = [list(map(int, input().split())) for _ in range(N)]
S, X, Y = map(int, input().split())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def dfs(x, y):
    if x <= -1 or x >= N or y <= -1 or y >= N:
        return
    
    if virus[x][y] == 0:
        

    


